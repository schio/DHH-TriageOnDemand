import cognitive_face as CF
KEY = '67e3815efe6242239d810803fda9f202'

#KEY = '163da94d401643949e46c309c73d1d40'  # Replace with a valid Subscription Key here.
CF.Key.set(KEY)

BASE_URL = 'https://eastasia.api.cognitive.microsoft.com/face/v1.0/'  # Replace with your regional Base URL
CF.BaseUrl.set(BASE_URL)

img_url = 'https://raw.githubusercontent.com/Microsoft/Cognitive-Face-Windows/master/Data/detection1.jpg'
result = CF.face.detect(img_url)
print result
