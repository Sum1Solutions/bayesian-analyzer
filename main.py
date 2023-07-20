from flask import Flask, render_template, request
import json

app = Flask(__name__)

# Hard-coded data for MVP. You might want to use a database in a real application
CONSPIRACY_THEORIES = [
    {
        "name": "9/11 Inside Job",
        "questions": [
            "Do you believe the US government has previously engaged in major covert operations?",
            "How trustworthy do you find mainstream media reporting on 9/11?"
        ]
    },
    # add more conspiracy theories here...
]

@app.route('/')
def home():
    return render_template('index.html', theories=CONSPIRACY_THEORIES)

@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.json
    theory_name = data['theory']
    answers = data['answers']
    # perform Bayesian analysis with the answers here...
    # dummy result for now
    result = 0.5

    return {"result": result}

if __name__ == '__main__':
    app.run(debug=True)
