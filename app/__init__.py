from flask import Flask, render_template, request, jsonify
from app.controllers.openai_controller import OpenAIController
from app.config import Config
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import text
from flask_migrate import Migrate

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    
    openai_controller = OpenAIController()
    app.config.from_object(Config)

    db.init_app(app)
    
    # Migrations
    with app.app_context():
        from app.models.emotion import Emotion
        
    migrate = Migrate(app, db)

    @app.route('/', methods=['GET', 'POST'])
    def index():
        if request.method == 'POST':
            inputData = request.form['input_text']
            response = openai_controller.call_openai_api(inputData)
            return render_template('index.html', content=response)
        return render_template('index.html')
      
    @app.route('/emotions')
    def list_emotions():
        emotions = Emotion.query.all()
        return render_template('emotions.html', emotions=emotions)
      
    return app

