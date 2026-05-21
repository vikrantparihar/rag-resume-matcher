# 🚀 AI Resume Matcher using RAG

An AI-powered Resume Matching System built with **Python, Streamlit, and Retrieval-Augmented Generation (RAG)** that analyzes resumes, compares them with job descriptions, and identifies missing skills required for target roles.

This project demonstrates practical implementation of **Natural Language Processing (NLP)** and **Generative AI workflows** for intelligent recruitment automation and ATS-style resume evaluation.

---

## 📌 Features

✅ Upload Resume in PDF Format  
✅ Extract Resume Text Automatically  
✅ Match Resume with Job Roles  
✅ Identify Missing Skills  
✅ AI-Powered Skill Analysis  
✅ Simple & Interactive Streamlit UI  
✅ Lightweight RAG Pipeline Implementation  
✅ Beginner-Friendly AI Project

---

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| Python | Core Development |
| Streamlit | Web Application UI |
| PyMuPDF | PDF Text Extraction |
| NLP | Skill & Text Processing |
| RAG Pipeline | Resume Matching Logic |

---

## 📂 Project Structure

```bash
rag-resume-matcher/
│
├── app.py                # Main Streamlit Application
├── rag_pipeline.py       # Resume Matching & RAG Logic
├── utils.py              # Utility Functions
├── jobs.txt              # Sample Job Descriptions
├── requirements.txt      # Project Dependencies
├── README.md             # Documentation
└── __pycache__/          # Python Cache Files


⚙️ Installation & Setup
1️⃣ Clone Repository
git clone https://github.com/vikrantparihar/rag-resume-matcher.git
2️⃣ Navigate to Project Folder
cd rag-resume-matcher
3️⃣ Install Dependencies
pip install -r requirements.txt
4️⃣ Run Streamlit Application
streamlit run app.py
🚀 How It Works
User uploads a resume in PDF format
System extracts resume text using PyMuPDF
Resume content is compared with predefined job roles
AI pipeline analyzes matching skills
Missing skills are identified and displayed
Final match results are shown in Streamlit UI
📸 Project Workflow
Resume Upload → Text Extraction → RAG Processing → Skill Matching → Missing Skill Detection → Result Display
🎯 Use Cases
AI Resume Screening
ATS Resume Evaluation
Skill Gap Analysis
Recruitment Automation
Career Guidance Platforms
HR Tech Solutions
🔮 Future Improvements
OpenAI / Gemini API Integration
Vector Database Support (FAISS / ChromaDB)
Multi-Resume Comparison
Resume Score Generation
Job Recommendation System
Deployment on Streamlit Cloud
Semantic Search Enhancement
