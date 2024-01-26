from app.models.emotion import Emotion

class EmotionsController:
    def load_emotions(self, str, project):
        normalized_list = self.normalize_string(str)
        list_of_emotions = normalized_list.split('\n')
        
        existing_emotions = Emotion.query.with_entities(Emotion.emotion).filter(Emotion.project == project).all()
        existing_emotions = [emotion[0] for emotion in existing_emotions]
        missing_in_db = [item for item in list_of_emotions if item not in existing_emotions]
        
        print(missing_in_db)
        
        return ""
    
    def normalize_string(self, str):
        return str.replace('\r\n', '\n').replace('\r', '\n')