from emotion_detection import emotion_detector

print('import ok')
try:
    result = emotion_detector('I am so happy I am doing this.')
    print('result:', result)
except Exception as e:
    print('function error:', type(e).__name__, e)
