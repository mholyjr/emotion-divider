from flask import Flask, render_template, request, jsonify
import requests
import os
from app.controllers.openai_controller import OpenAIController

def create_app():
    app = Flask(__name__)
    openai_controller = OpenAIController()

    @app.route('/', methods=['GET', 'POST'])
    def index():
        if request.method == 'POST':
            inputData = request.form['input_text']
            response = openai_controller.call_openai_api(inputData)
            return render_template('index.html', content=response)
        return render_template('index.html')
      
    return app
