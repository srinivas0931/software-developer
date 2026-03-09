from flask import Flask, request, jsonify
import google.generativeai as genai

app = Flask(__name__)

genai.configure(api_key="YOUR_GEMINI_API_KEY")

model = genai.GenerativeModel("gemini-pro")

@app.route('/generate-curriculum', methods=['POST'])
def generate_curriculum():

    data = request.json

    course = data["courseName"]
    level = data["educationLevel"]
    duration = data["courseDuration"]
    skills = data["skills"]

    prompt = f"""
    Create detailed study notes for a course.

    Course: {course}
    Level: {level}
    Duration: {duration}
    Topics: {skills}

    For each module include:
    - module title
    - explanation
    - key concepts
    - examples
    - summary
    """

    response = model.generate_content(prompt)

    return jsonify({
        "course": course,
        "notes": response.text
    })

if __name__ == "__main__":
    app.run (host="0.0.0.0",port=8000, debug=True)