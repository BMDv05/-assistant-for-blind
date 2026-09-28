from flask import Flask, render_template, jsonify
import json
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_data')
def get_data():
    if os.path.exists('data_log.json'):
        with open('data_log.json', 'r', encoding='utf-8') as f:
            return jsonify(json.load(f))
    return jsonify({"description": "بانتظار النظام...", "alerts": []})

if __name__ == '__main__':
    app.run(debug=True, port=5000)