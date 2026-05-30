import requests

import requests

client_id = "xrUlqa5aKZBBKbrx3PJu"
client_secret = "lmyMjJ8qNM"

# 혹시 모를 공백 제거
client_id = client_id.strip()
client_secret = client_secret.strip()

print(repr(client_id))
print(repr(client_secret))
url = "https://openapi.naver.com/v1/datalab/search"
headers = {
    "X-Naver-Client-Id": client_id,
    "X-Naver-Client-Secret": client_secret,
    "Content-Type": "application/json"
}
body = {
    "startDate": "2025-01-01",
    "endDate": "2026-05-17",
    "timeUnit": "week",
    "keywordGroups": [
        {"groupName": "두바이초콜릿", "keywords": ["두바이초콜릿", "두쫀쿠"]}
    ]
}

response = requests.post(url, headers=headers, json=body)
print(response.json())