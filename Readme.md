# Mini ChatGPT Clone 🤖

A simple AI chatbot built using **Python**, **Streamlit**, and **Google Gemini API**.

## 🚀 Features

* ChatGPT-like UI using Streamlit
* Multi-turn conversation memory
* Clear Chat functionality
* Gemini 2.5 Flash integration
* Secure API key handling using `.env`
* Ready for Streamlit Cloud deployment

---

## 🛠️ Tech Stack

* Python
* Streamlit
* Google Gemini API
* python-dotenv

---

## 📂 Project Structure

```bash
Mini-ChatGPT/
│
├── app.py
├── requirements.txt
├── .gitignore
├── README.md
└── .env
```

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/mini-chatgpt.git
cd mini-chatgpt
```

### 2. Create virtual environment

```bash
python -m venv .venv
```

Activate environment:

### Windows

```bash
.venv\Scripts\activate
```

### Mac/Linux

```bash
source .venv/bin/activate
```

---

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

### 4. Create `.env` file

```env
GEMINI_API_KEY=your_api_key_here
```

---

### 5. Run the app

```bash
streamlit run app.py
```

---

## 🌐 Deployment

This project can be deployed easily on:

* Streamlit Cloud

Add your API key in Streamlit Secrets:

```toml
GEMINI_API_KEY="your_api_key_here"
```

---

## 📸 Preview

(Add screenshot here later)

---

## 🔒 Security Note

Do NOT upload your `.env` file to GitHub.

Make sure `.env` is added in `.gitignore`.

---

## 👨‍💻 Author

Yadvendra Malviya

LinkedIn: https://www.linkedin.com/in/yadvendra-malviya-45650424a/

GitHub: https://github.com/yadven7/Mini-ChatGPT-Clone
