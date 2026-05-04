from flask import Flask, request, jsonify
from flask_cors import CORS
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import re

app = Flask(__name__)
CORS(app)

# Topics with questions + ideal answers (keywords-based)
topics = {
    "OOP": [
        {
            "q": "What is OOP?",
            "ideal": "object oriented programming classes objects encapsulation inheritance polymorphism"
        },
        {
            "q": "What is Encapsulation?",
            "ideal": "wrapping data methods single unit restrict access"
        }
    ],

    "DBMS": [
        {
            "q": "What is DBMS?",
            "ideal": "database management system store manage retrieve data"
        },
        {
            "q": "What is normalization?",
            "ideal": "organizing data reduce redundancy improve integrity"
        }
    ],

    "AI/ML": [
        {
            "q": "What is Machine Learning?",
            "ideal": "machine learning subset artificial intelligence systems learn from data"
        },
        {
            "q": "What is supervised learning?",
            "ideal": "machine learning trained using labeled data"
        }
    ]
}

current_questions = []
current_index = 0
score = 0


# 🔹 Clean text
def preprocess(text):
    text = text.lower()
    text = re.sub(r'[^a-z\s]', '', text)
    return text


# 🔹 Improved evaluation
def evaluate_answer(user_answer, ideal_answer):
    user_answer = preprocess(user_answer)
    ideal_answer = preprocess(ideal_answer)

    vectorizer = TfidfVectorizer(stop_words='english')
    vectors = vectorizer.fit_transform([user_answer, ideal_answer])

    similarity = cosine_similarity(vectors[0], vectors[1])[0][0]

    # 🔥 Keyword boost
    keywords = ideal_answer.split()
    match_count = sum(1 for word in keywords if word in user_answer)

    if match_count >= len(keywords) // 2:
        similarity += 0.2

    return similarity


@app.route('/topics', methods=['GET'])
def get_topics():
    return jsonify({"topics": list(topics.keys())})


@app.route('/start', methods=['POST'])
def start():
    global current_questions, current_index, score

    data = request.json
    topic = data.get("topic")

    current_questions = topics.get(topic, [])
    current_index = 0
    score = 0

    if not current_questions:
        return jsonify({"error": "Invalid topic"})

    return jsonify({
        "question": current_questions[current_index]["q"],
        "progress": f"Question 1/{len(current_questions)}"
    })


@app.route('/answer', methods=['POST'])
def answer():
    global current_index, score

    data = request.json
    user_answer = data.get("answer", "")

    ideal = current_questions[current_index]["ideal"]

    similarity = evaluate_answer(user_answer, ideal)

    # 🔥 Improved thresholds
    if similarity < 0.1:
        result = "Incorrect answer"
        intent = "correction"

    elif similarity < 0.3:
        result = "Weak answer"
        intent = "clarification"
        score += 3

    elif similarity < 0.6:
        result = "Partial answer"
        intent = "deep_dive"
        score += 6

    else:
        result = "Good answer"
        intent = "strong"
        score += 10

    follow_up = f"Can you explain more about {current_questions[current_index]['q']}?"

    current_index += 1

    if current_index < len(current_questions):
        return jsonify({
            "result": result,
            "intent": intent,
            "follow_up": follow_up,
            "next_question": current_questions[current_index]["q"],
            "progress": f"Question {current_index+1}/{len(current_questions)}"
        })
    else:
        return jsonify({
            "result": result,
            "intent": intent,
            "final_score": score,
            "message": "Interview Completed 🎉"
        })


if __name__ == '__main__':
    app.run(debug=True)