# DDokDDok(똑똑)
==============
## DDokDDok Is..
* Python 기반의 유튜브 API입니다.
* Python 2.7+, Python 3.5+에서 동작하는것을 확인했습니다.
* 독립적으로 실행할 수 있으나, 배포판에서는 통합 UI를 제공합니다.(javafx사용)

## Dependency
* Python 3.5+ 이상 사용자.
```
pip3 install oauth2client python-dateutil httplib2 google_auth_oauthlib google-api-python-client
```
* Python 2.7+ 이상 사용자.
```
pip install oauth2client python-dateutil httplib2 google_auth_oauthlib google-api-python-client
```

## Prerequisite
* Youtube Chatbot을 사용하는 모든 사용자는 `Youtube API`와 `Google OAuth`에 등록(사용 신청)되어 있어야 합니다.

### API Key, OAuth2.0 ID
* (https://console.developers.google.com/apis)[Google API Console]에 접속해서 왼쪽 사이드 메뉴의 `라이브러리`를 선택합니다.
* 라이브러리에서 Youtube Data API를 신청하고, 원래 메뉴로 돌아와 API Key를 발급받습니다.
* 그 후, `OAuth 2.0 클라이언트 ID`를 발급받습니다.
 * OAuth의 어플리케이션은, `기타 어플리케이션`을 사용합니다.
 * ID를 발급 받은 후, 화면 상단의 `JSON 다운로드` 버튼을 눌러 `client_secrets.json`파일로 저장합니다.

### OAuth2.0 Token 발급받기
* repository에 있는 `get_auth.py`를 실행해줍니다. 이때, 위에서 발급받은 `client_secrets.json`이 같은 폴더에 있어야 합니다.

### 실행하기
* Token을 발급받았다면. 다음과 같은 명령어로 chatbot을 실행할 수 있습니다.
```python3 bot.py <BROADCAST_ID>```

## 참고
* Youtube OAuth2.0 구현에 대한 사항은 이곳을 참고하시면 좋습니다.
* (https://developers.google.com/youtube/v3/guides/authentication?hl=ko)[Implement Youtube OAuth2.0]
