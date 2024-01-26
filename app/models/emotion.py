from app.database import db

class Emotion(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    emotion = db.Column(db.Text)
    project = db.Column(db.String(255))
    sentiment = db.Column(db.String(255))
