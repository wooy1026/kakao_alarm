import requests
import json
from PyKakao import Message

API = Message(service_key = "d3478140dfe991d07a51a6f6b53e54b0") # API키 (우영)

# # 1번째
# print("인증 확인 주소: " , API.get_url_for_generating_code())

# # 2번째
# newtoken = API.get_access_token_by_redirected_url("https://localhost:5000/?code=lmIm80qvnV1leQS2wUGdRSswb0Xkqv74JhfrXV9V_cObDrEPW_wq9gAAAAQKKiWPAAABj8jbN-akJA3lYdtGWQ") 토큰 생성주소
# print("새로운토큰: ", newtoken)

# 메시지 전송 파트
url = "https://kapi.kakao.com/v2/api/talk/memo/default/send"

token = "3KE1W18GSAUAZCOGJIsAS7TWaYU9qXlUAAAAAQo9dNoAAAGPyNw-u5gXPJRhmZ-F" # 변경된 토큰 대입

headers = {"Authorization": "Bearer " + token}

data = {
    "template_object": json.dumps({
        "object_type": "feed",
        "content": {
            "title": "차량 경고",
            "description": "차량이 범위 밖으로 이동했습니다.",
            "image_url": "https://play-lh.googleusercontent.com/P672xJ5oytm7jhBP59o4hMQfqErBhXsLD7n_PJG3qcGAaPqxpTHzHYOhPNYMlOaUwAV-", # 이미지 URL
            "link": {}
        },
        "buttons": [{"title": "차량의 위치를 확인해주세요","link": {}}]
    })
}

response = requests.post(url, headers=headers, data=data)
print(response.status_code, ", 알림 발송")