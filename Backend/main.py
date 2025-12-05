import functions_framework
import requests
import json
import base64
import fitz  # PyMuPDF
import re
import io

# ---------------- CONFIG ----------------
HF_API_URL = "https://api-inference.huggingface.co/models/sentence-transformers/all-MiniLM-L6-v2"
HF_HEADERS = {"Authorization": "Bearer <YOUR_HF_API_KEY>"}  # Replace with your real HF key

SKILLS = [
    "python", "java", "javascript", "node", "react", "flask", "django", "spring",
    "rest api", "sql", "mongodb", "postgresql", "docker", "kubernetes", "aws",
    "gcp", "azure", "git", "microservices", "tensorflow", "pytorch", "nlp",
    "machine learning", "data analysis"
]


def get_similarity(job_desc, resume):
    try:
        payload = {"inputs": {"source_sentence": job_desc, "sentences": [resume]}}
        res = requests.post(HF_API_URL, headers=HF_HEADERS, json=payload, timeout=30)
        result = res.json()
        return float(result[0]) if isinstance(result, list) else 0.0
    except Exception:
        return 0.0


def extract_skills(text):
    return sorted(set(s for s in SKILLS if s in text.lower()))


def score_resume(job_desc, resume):
    sim = get_similarity(job_desc, resume)
    jd_skills = extract_skills(job_desc)
    rs_skills = extract_skills(resume)
    overlap = len(set(jd_skills) & set(rs_skills))
    bonus = (overlap / max(1, len(jd_skills))) * 0.1
    total = round((sim + bonus) * 100, 2)
    return {
        "similarity": round(sim * 100, 2),
        "bonus": round(bonus * 100, 2),
        "final_score": total,
        "matched_skills": sorted(set(jd_skills) & set(rs_skills))
    }


@functions_framework.http
def rankifyhr(request):
    """Unified entry point for both /rankifyhr and /extract"""
    import urllib.parse

    headers = {
        "Access-Control-Allow-Origin": "*",
        "Access-Control-Allow-Methods": "POST, OPTIONS",
        "Access-Control-Allow-Headers": "Content-Type",
        "Content-Type": "application/json"
    }

    # Handle preflight
    if request.method == "OPTIONS":
        return ("", 204, headers)

    # Determine path
    path = request.path
    print("Request path:", path)

    # ---------- Handle /extract ----------
    if "/extract" in path:
        try:
            data = request.get_json(silent=True)
            pdf_data = (data.get("pdf") or "").strip()
            if not pdf_data:
                return (json.dumps({"error": "No PDF data received"}), 400, headers)

            pdf_data = re.sub(r"\s+", "", pdf_data)
            missing_padding = len(pdf_data) % 4
            if missing_padding:
                pdf_data += "=" * (4 - missing_padding)

            pdf_bytes = base64.b64decode(pdf_data, validate=False)
            text = ""
            with fitz.open(stream=io.BytesIO(pdf_bytes), filetype="pdf") as doc:
                for page in doc:
                    text += page.get_text("text") or ""

            if not text.strip():
                text = "[No extractable text found – scanned image PDF]"

            print("Extracted text preview:", text[:150])
            return (json.dumps({"text": text}), 200, headers)
        except Exception as e:
            print("Extract error:", str(e))
            return (json.dumps({"error": str(e)}), 500, headers)

    # ---------- Handle /rankifyhr ----------
    else:
        try:
            data = request.get_json(silent=True)
            jd = data.get("job_description", "")
            resumes = data.get("resumes", [])

            if not jd or not resumes:
                return (json.dumps({"error": "Missing job_description or resumes"}), 400, headers)

            results = []
            for i, resume in enumerate(resumes):
                s = score_resume(jd, resume)
                results.append({
                    "resume_id": i + 1,
                    "preview": resume[:150] + "..." if len(resume) > 150 else resume,
                    **s
                })

            results.sort(key=lambda x: x["final_score"], reverse=True)
            return (json.dumps({"results": results}), 200, headers)
        except Exception as e:
            print("Ranking error:", str(e))
            return (json.dumps({"error": str(e)}), 500, headers)
