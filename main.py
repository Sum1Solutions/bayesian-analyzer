from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

conspiracies = [
    {
        "name": "Covid from Lab",
        "questions": [
            "Has there been any credible evidence of a lab leak?",
            "What is the level of security in the lab?",
            "Has there been any significant cover-up or misinformation?"
        ],
        "prior": 0.1,
        "year": 2019
    },
    {
        "name": "Deep State",
        "questions": [
            "What evidence supports the existence of a deep state?",
            "What actions have been attributed to the deep state?",
            "How reliable are the sources of information?"
        ],
        "prior": 0.2,
        "year": 2016
    },
    {
        "name": "JFK Assassination",
        "questions": [
            "What inconsistencies exist in the official investigation?",
            "What evidence supports alternative theories?",
            "What credibility do the alternative theories have?"
        ],
        "prior": 0.3,
        "year": 1963
    },
    {
        "name": "9/11 Inside Job",
        "questions": [
            "What evidence challenges the official explanation?",
            "What alternative explanations exist?",
            "How well-supported are the alternative explanations?"
        ],
        "prior": 0.4,
        "year": 2001
    },
    {
        "name": "Was the Presidency Stolen from Trump?",
        "questions": [
            "What evidence supports the claim that the election was stolen?",
            "What investigations or court cases have been conducted?",
            "What credibility do the claims have?"
        ],
        "prior": 0.5,
        "year": 2020
    }
]

@app.route('/')
def index():
    sorted_conspiracies = sorted(conspiracies, key=lambda c: c['year'], reverse=True)
    return render_template('index.html', conspiracies=sorted_conspiracies)

@app.route('/conspiracy/<name>', methods=['GET', 'POST'])
def conspiracy(name):
    conspiracy = next((c for c in conspiracies if c['name'] == name), None)
    if request.method == 'POST':
        likelihood = calculate_likelihood(conspiracy, request.form)
        return jsonify({'likelihood': likelihood})
    return render_template('conspiracy.html', conspiracy=conspiracy)

def calculate_likelihood(conspiracy, answers):
    prior = conspiracy['prior']
    likelihood = prior
    for question in conspiracy['questions']:
        likelihood *= answers.get(question, 0.5)  # Use a default value of 0.5 if answer not provided
    return likelihood

if __name__ == '__main__':
    app.run()
