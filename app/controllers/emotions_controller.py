from app.models.emotion import Emotion

class EmotionsController:
    def load_emotions(self, str):
        normalized_list = self.normalize_string(str)
        list_of_emotions = normalized_list.split('\n')
        print(list_of_emotions)
        
        return ""
    
    def normalize_string(self, str):
        return str.replace('\r\n', '\n').replace('\r', '\n')