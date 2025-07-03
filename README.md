# 🤖 AI Learning Assistant

An AI-powered educational assistant that helps learners by:
- Summarizing uploaded PDF notes or typed content  
- Generating quizzes to test understanding  
- Tracking progress visually  
- Supporting real-time text-based interaction

Built using **Streamlit**, **Python**, and **OpenAI's APIs**.

---

## 🚀 Features

- 📤 **PDF Upload**: Extracts and summarizes text from uploaded PDFs  
- 🧠 **AI Summarization**: Uses LLMs to generate concise summaries  
- ❓ **Quiz Generator**: Creates 3-question quizzes from the content  
- 📈 **Progress Tracker**: Visual feedback with a simple progress bar  
- ⌨️ **Text Input Mode**: Accepts typed content (alternative to voice)

---

## 🛠️ Technologies Used

- Python 3.10+  
- Streamlit  
- OpenAI API  
- dotenv  
- pdfplumber  

---

## 📦 Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/ai-learning-assistant.git
   cd ai-learning-assistant
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Create a `.env` file and add your OpenAI credentials:
   ```env
   OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
   OPENAI_API_BASE=https://api.openai.com/v1
   ```

4. Run the app:
   ```bash
   streamlit run app.py
   ```

---

## 📄 Sample PDF

Use the included `test_detailed_document.pdf` or upload your own notes to test the app.

---

## 📸 Screenshots

![AI Screenshot](https://i.imgur.com/example.png)

---

## 👨‍💻 Author

Built by [Pradhyumn Sharma](https://github.com/pradhyumn07)

---

## 📌 License

This project is licensed under the MIT License.
