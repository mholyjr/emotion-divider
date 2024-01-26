from flask import Flask, render_template, request, jsonify
from app.controllers.openai_controller import OpenAIController
from app.controllers.emotions_controller import EmotionsController
from app.config import Config
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import text
from flask_migrate import Migrate
from app.database import db

def create_app():
    app = Flask(__name__)
    
    openai_controller = OpenAIController()
    emotions_controller = EmotionsController();
    app.config.from_object(Config)

    db.init_app(app)
    
    # Migrations
    from app.models.emotion import Emotion
        
    migrate = Migrate(app, db)

    @app.route('/', methods=['GET', 'POST'])
    def index():
        if request.method == 'POST':
            inputData = request.form['input_text']
            project = request.form['project']
            response = emotions_controller.load_emotions(inputData, project)
            print(project)
            return render_template('index.html', content=response)
        return render_template('index.html')
      
    @app.route('/emotions')
    def list_emotions():
        emotions = Emotion.query.all()
        return render_template('emotions.html', emotions=emotions)
      
    return app

