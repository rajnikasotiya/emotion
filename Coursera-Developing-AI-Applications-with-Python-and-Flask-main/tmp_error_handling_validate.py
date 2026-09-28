import types
import EmotionDetection.emotion_detection as ed
from server import app

class FakeResp:
    def __init__(self):
        self.status_code = 400
    def raise_for_status(self):
        raise Exception('Should not be called')
    def json(self):
        return {}
    @property
    def text(self):
        return ''

ed.requests = types.SimpleNamespace(post=lambda url, headers, json, timeout: FakeResp())
print('function result:', ed.emotion_detector(''))

with app.test_client() as client:
    response = client.get('/emotionDetector?textToAnalyze=')
    print('server status:', response.status_code)
    print('server body:', response.data.decode())
