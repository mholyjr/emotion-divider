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
    
    with app.app_context():
        # Import your models here
        from app.models.emotion import Emotion
        
    migrate = Migrate(app, db)


    @app.route('/', methods=['GET', 'POST'])
    def index():
        if request.method == 'POST':
            inputData = request.form['input_text']
            response = openai_controller.call_openai_api(inputData)
            return render_template('index.html', content=response)
        return render_template('index.html')

  
    @app.route('/test_db')
    def test_db():
      try:
        # Obtain a connection and execute a simple query
        with db.engine.connect() as connection:
            result = connection.execute(text("SELECT 1"))
            for row in result:
                print("Query result:", row)
            return 'Database connection successful.'
      except Exception as e:
        # If an exception occurred, return the error
        return f'Database connection failed: {e}'
          
    return app

