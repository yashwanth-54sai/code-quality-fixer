
# 🚀 AI-Powered Code Quality Analyzer & Error Fixer  

An intelligent web-based application that analyzes user-written source code in real time, detects errors, warnings, inefficiencies, evaluates code quality metrics, and provides AI-generated optimized solutions. Built using Streamlit, Python static analyzers, and LLM-based AI models.

---

## 📌 Features  

- Real-time Code Editor Interface  
- Python & Java Code Analysis  
- Syntax Error Detection  
- Logical Issue Detection  
- Code Quality Scoring  
- Performance Improvement Suggestions  
- Time & Space Complexity Estimation  
- Duplicate Code Detection  
- Security & Best Practice Warnings  
- AI-Powered Code Fix Suggestions  
- Downloadable Analysis Report  

---

## 🎯 Project Objective  

The primary goal of this project is to help developers:

- Improve code quality instantly  
- Identify bugs early  
- Learn best coding practices  
- Optimize performance  
- Reduce debugging time  
- Get AI-assisted refactored code  

This platform focuses on live code input analysis instead of file uploads, making it ideal for learning, interviews, and rapid testing.

---

## 🏗️ System Architecture  

User Input Code  
        ↓  
Streamlit UI Editor  
        ↓  
Language Detector  
        ↓  
Static Code Analyzer  
        ↓  
Quality Metrics Engine  
        ↓  
AI Optimization Engine  
        ↓  
Final Report Generator  
        ↓  
Results Display  

---

## ⚙️ Technology Stack  

Frontend UI      : Streamlit  
Backend          : Python  
AI Integration   : Groq API / Google Generative AI  
Static Analysis  : Custom Python Modules  
Code Editor      : streamlit-code-editor  
Vector Search    : FAISS  
Embeddings       : Sentence Transformers  
Visualization    : Matplotlib  

---

## 📁 Project Folder Structure  

CodeQualityFixer/
│  
├── app.py  
├── analyzers/  
│   ├── python_analyzer.py  
│   └── java_analyzer.py  
├── scoring/  
│   └── quality_score.py  
├── ai_engine/  
│   └── ai_suggestions.py  
├── utils/  
│   └── helpers.py  
├── requirements.txt  
└── README.md  

---

## 🛠️ Installation Guide  

### Step 1: Clone Repository  

git clone https://github.com/your-username/CodeQualityFixer.git  
cd CodeQualityFixer  

### Step 2: Create Virtual Environment  

python -m venv venv  

Activate:

Windows:
venv\Scripts\activate  

Linux/Mac:
source venv/bin/activate  

### Step 3: Install Dependencies  

pip install -r requirements.txt  

### Step 4: Add API Keys  

Create .env file:

GROQ_API_KEY=your_api_key_here  
GOOGLE_API_KEY=your_api_key_here  

### Step 5: Run Application  

streamlit run app.py  

---

## 📊 Supported Languages  

- Python  
- Java  

Future support planned:

- JavaScript  
- C++  
- PHP  

---

## 🔐 Security Measures  

- No permanent code storage  
- Secure API key usage  
- Local execution supported  
- No file uploads allowed  

---

## 🌱 Future Enhancements  

- Multi-language support  
- Cloud deployment  
- PDF report export  
- Authentication system  
- GitHub integration  
- CI/CD support  

---

## 🎓 Use Cases  

- Students learning programming  
- Developers improving code quality  
- Interview preparation  
- Debugging practice  
- Automated code review  

---

## 👨‍💻 Developer  

Sai Yashwanth Angadi  
Aspiring Data Analyst & AI Developer  
India  

---

## 📜 License  

This project is licensed under the MIT License.

---

⭐ If you like this project, don't forget to star the repository!
