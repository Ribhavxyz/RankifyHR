# 🚀 RankifyHR – AI-Powered Cloud Resume Ranking System

RankifyHR is a **cloud-native web application** that automatically ranks candidate resumes based on their similarity to a job description using **AI + Google Cloud Platform**.  
The system reduces manual HR screening time by leveraging **semantic similarity models** and **skill-based scoring**.

---

### 🔗 Live Deployment
https://storage.googleapis.com/rankifyhr-ui/index_dark_v2.html

yaml
Copy code

---

## 🧑‍💻 Author
[![GitHub](https://img.shields.io/badge/GitHub-Ribhavxyz-black?logo=github)](https://github.com/Ribhavxyz)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Ribhav%20Yadav-blue?logo=linkedin)](https://www.linkedin.com/in/ribhav-yadav)

---

## 🌟 Features
- 🧠 AI-based resume ranking using Hugging Face Transformers  
- ☁️ **Serverless backend** running on Google Cloud Run  
- 🗂 Static **frontend hosted on Google Cloud Storage**  
- 📄 PDF resume text extraction using **PyMuPDF**  
- 📊 **Chart.js visualization** for ranking results  
- 🔐 **Secure deployment** using IAM & HTTPS  

---

## ⚙️ Architecture Overview
```text
User → Cloud Storage → Cloud Run → Hugging Face API → Chart.js Visualization
Layer	Service	Role
Frontend	Google Cloud Storage	UI hosting & resume uploads
Backend	Google Cloud Run (Python)	Resume text extraction + ranking
AI	Hugging Face Transformer API	Semantic similarity scoring
Visualization	Chart.js	Graph of similarity scores

📌 Architecture diagram available in /architecture/RankifyHR_Architecture.png

🧰 Tech Stack
Category	Technology
Cloud	Google Cloud Platform
Backend	Python, Functions Framework, Requests, PyMuPDF
AI	Hugging Face (all-MiniLM-L6-v2)
Frontend	HTML, CSS, JavaScript, Chart.js
Security	IAM, HTTPS

🔥 How It Works
User uploads resume PDFs and enters a job description.

Frontend sends the request to Cloud Run.

/extract endpoint converts PDF to text using PyMuPDF.

/rankifyhr endpoint sends text to Hugging Face AI model.

Backend calculates final ranking scores based on similarity + skills.

Results and bar graph are displayed to the user.

🛠 Project Structure
css
Copy code
RankifyHR/
│
├── backend/
│   ├── main.py
│   ├── requirements.txt
│
├── frontend/
│   ├── index_dark_v2.html
│   ├── script.js
│   ├── styles.css
│
├── architecture/
│   ├── RankifyHR_Architecture.png
│   └── demo_screenshots/
│
└── README.md
🧪 Testing Summary
Test	Result
Resume extraction	Success
Ranking accuracy	~95%
Processing time	~3 seconds for 5 resumes
Autoscaling	Cloud Run scaled automatically
Browser support	Chrome ✓ Edge ✓ Firefox ✓

📌 Sample screenshots available in /architecture/demo_screenshots

🚀 Run Locally (Optional)
bash
Copy code
git clone https://github.com/Ribhavxyz/RankifyHR.git
cd RankifyHR/backend
pip install -r requirements.txt
python main.py
Then open frontend/index_dark_v2.html in browser.

🔮 Future Enhancements
OCR for scanned resumes using Google Vision API

Firebase Authentication for secure HR login

Ranking history storage in Firestore

Full analytics dashboard

🪪 License
MIT License — see LICENSE file.

⭐ If this project helped you, please give it a star on GitHub!
