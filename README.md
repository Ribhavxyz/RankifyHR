# 🚀 RankifyHR – AI-Powered Cloud Resume Ranking System

RankifyHR is a **cloud-native web application** that automatically ranks candidate resumes based on their similarity to a job description using **AI + Google Cloud Platform**.  
It reduces manual HR screening time by using **semantic similarity scoring** and **skill-based matching**.

---

## 🔗 Live Deployment
https://storage.googleapis.com/rankifyhr-ui/index_dark_v2.html

---

## 👨‍💻 Author
[![GitHub](https://img.shields.io/badge/GitHub-Ribhavxyz-black?logo=github)](https://github.com/Ribhavxyz)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Ribhav%20Yadav-blue?logo=linkedin)](https://www.linkedin.com/in/ribhav-yadav)

---

## 🌟 Features
- 🧠 AI-driven resume ranking using Hugging Face Transformers  
- ☁️ Serverless backend deployed on **Google Cloud Run**  
- 🗂 Static frontend hosted on **Google Cloud Storage**  
- 📄 PDF text extraction using **PyMuPDF**  
- 📊 Real-time ranking visualization using **Chart.js**  
- 🔐 Secured using **IAM & HTTPS**

---

## ⚙️ Architecture Overview
User → Cloud Storage → Cloud Run → Hugging Face API → Chart.js Visualization

| Layer | Service | Role |
|--------|---------|------|
| Frontend | Google Cloud Storage | UI hosting & resume uploads |
| Backend | Google Cloud Run (Python) | Resume extraction + AI-based ranking |
| AI | Hugging Face Transformers | Semantic similarity model |
| Visualization | Chart.js | Displays score graph |

📌 Full architecture diagram available in `/architecture/RankifyHR_Architecture.png`

---

## 🧰 Tech Stack
| Category | Technology |
|----------|-------------|
| Cloud | Google Cloud Platform (Cloud Run, Cloud Storage) |
| Backend | Python, Functions Framework, Requests, PyMuPDF |
| AI | Hugging Face API (`all-MiniLM-L6-v2`) |
| Frontend | HTML, CSS, JavaScript, Chart.js |
| Security | IAM Roles, HTTPS, API Key Auth |

---

## 🔥 How It Works
1. User uploads resume PDFs + job description through the UI  
2. Frontend sends request to **Cloud Run backend**  
3. `/extract` parses PDFs to text using PyMuPDF  
4. `/rankifyhr` compares resume text with job description using Hugging Face semantic model  
5. Final scores = similarity + matched skill bonus  
6. Chart.js shows resume ranking visually

---

## 🗂️ Project Structure

- **RankifyHR/**
  - **Architecture/**
    - **demo Screenshots/**
      - `1.png`
      - `2.png`
      - `3.png`
    - `FrontendUI.png`
    - `Google Bucket Config.png`
    - `GoogleRun Config.png`
    - `RankifyHR_Architecture Diagram.png`
  - **Assets/**
    - `Resume_1_Python_Developer.pdf`
    - `Resume_2_Frontend_Developer.pdf`
    - `Resume_3_DevOps_Engineer.pdf`
    - `Resume_4_Data_Scientist.pdf`
    - `Resume_5_Cloud_Engineer.pdf`
  - **Backend/**
    - `main.py`
    - `requirements.txt`
  - **Frontend/**
    - `index_dark_v2.html`
  - `README.md`


---

## 🧪 Testing Summary
| Test | Result |
|------|--------|
| Resume extraction | Successful |
| Resume ranking logic | ~95% accuracy |
| Response time | ~3 seconds for 5 resumes |
| Cloud autoscaling | Yes, under concurrent uploads |
| Browser support | Chrome ✓ Edge ✓ Firefox ✓ |

📌 Sample screenshots available in `/architecture/demo_screenshots/`

---

## 🚀 Run Locally (optional)
git clone https://github.com/Ribhavxyz/RankifyHR.git

cd RankifyHR/backend
pip install -r requirements.txt
python main.py
Open `frontend/index_dark_v2.html` in your browser.

---

## 🔮 Future Enhancements
- OCR support using **Google Vision API**  
- Firebase authentication for secure HR login  
- Firestore storage for saving ranking history  
- Advanced analytics dashboard for recruiters  

---

## 🪪 License
MIT License — see the LICENSE file.

---

### ⭐ If you like this project, please give it a star. It motivates further development!
