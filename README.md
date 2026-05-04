# follow_upqns
# 🎤 AI Interview Simulator

An interactive web-based interview practice system that evaluates user answers using Machine Learning.

---

## 🚀 Features

* 🎯 Topic-based interview (OOP, DBMS, AI/ML)
* 🤖 ML-based answer evaluation using TF-IDF + Cosine Similarity
* 📊 Smart scoring system (Incorrect / Weak / Partial / Good)
* 🔁 Follow-up question generation
* 🌐 Simple frontend using HTML + JavaScript
* ⚡ Fast backend using Flask

---

## 🛠️ Tech Stack

* **Frontend:** HTML, JavaScript
* **Backend:** Python (Flask)
* **Machine Learning:** Scikit-learn (TF-IDF, Cosine Similarity)

---

## 📁 Project Structure

```
follow_upqns/
│── app.py
│── index.html
│── README.md
```

---

## ⚙️ How It Works

1. User selects a topic
2. System generates a question
3. User submits an answer
4. ML model compares answer with ideal answer
5. System returns:

   * Result (Incorrect / Weak / Partial / Good)
   * Follow-up question
   * Score

---

## 🧠 ML Evaluation Logic

* Text preprocessing (lowercase + cleaning)
* TF-IDF vectorization
* Cosine similarity calculation
* Keyword matching boost
* Adaptive scoring thresholds

---

## ▶️ How to Run
### 1. Clone the repository

```
git clone https://github.com/lahariboddeda/follow_upqns.git
cd follow_upqns
```

---

### 2. Install dependencies

Make sure you are inside the project root folder, then run:

```
pip install -r requirements.txt
```

---

### 3. Run the Backend Server

Go to the backend folder:

```
cd backend
python app.py
```

The server will start at:

```
http://127.0.0.1:5000
```
### 4. Run the Frontend

Go to the frontend folder:

```
cd ../frontend
```

Now open `index.html` in your browser
OR use **Live Server (VS Code recommended)**

---

### ✅ Done!

* Select a topic
* Start interview
* Answer questions
* Get evaluation + score 🎯


## 📌 API Endpoints

* `GET /topics` → Get available topics
* `POST /start` → Start interview
* `POST /answer` → Submit answer

---

## 🧪 Example Topics

* OOP
* DBMS
* AI/ML

---

## 🎯 Future Improvements

* 🤖 GPT-based evaluation
* 🎤 Voice input support
* 📊 Performance analytics dashboard
* 🔐 User login system

---

## 🙌 Acknowledgements

Built as a learning project to simulate real interview environments using AI concepts.

---
