import json
import types
import emotion_detection

class FakeResp:
    def __init__(self):
        self._payload = json.dumps({'anger': 0.0, 'disgust': 0.0, 'fear': 0.0, 'joy': 0.95, 'sadness': 0.05})

    def raise_for_status(self):
        pass

    def json(self):
        return {'text': self._payload}

    @property
    def text(self):
        return self._payload

emotion_detection.requests = types.SimpleNamespace(post=lambda url, headers, json, timeout: FakeResp())
print('import ok')
print(emotion_detection.emotion_detector('I am so happy I am doing this.'))
