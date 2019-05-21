# DDokDDok(똑똑)

## DDokDDok이란?
* Python 기반의 유튜브 API입니다.
* Python 2.7+, Python 3.5+에서 동작하는것을 확인했습니다.
* 독립적으로 실행할 수 있으나, 배포판에서는 통합 UI를 제공합니다.(javafx사용)

## What this project does
* 시청자가 입력한 !<명령> 에 반응하는 Chatbot입니다.
* 비속어 필터링은 본 모듈에는 부착되어 있지 않으며, Java 통합 모듈에서만 동작합니다.
* 기본적으로 !업타임 명령어가 탑재되어 있습니다.

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
* [Google API Console](https://console.developers.google.com/apis)에 접속해서 왼쪽 사이드 메뉴의 `라이브러리`를 선택합니다.
* 라이브러리에서 Youtube Data API를 신청하고, 원래 메뉴로 돌아와 API Key를 발급받습니다.
* 그 후, `OAuth 2.0 클라이언트 ID`를 발급받습니다.
 * OAuth의 어플리케이션은, `기타 어플리케이션`을 사용합니다.
 * ID를 발급 받은 후, 화면 상단의 `JSON 다운로드` 버튼을 눌러 `client_secrets.json`파일로 저장합니다.

> Release Version(Javafx)을 사용하시는 분께서는, 이 곳 까지만 진행하시면 됩니다.

### OAuth2.0 Token 발급받기
* repository에 있는 `get_auth.py`를 실행해줍니다. 이때, 위에서 발급받은 `client_secrets.json`이 같은 폴더에 있어야 합니다.
* 브라우저가 실행되면, 로그인을 한 후 발급되는 API Key를 Console/Popup Window에 입력해 oauth_cred파일을 생성합니다.
### 실행하기
* Token을 발급받았다면. 다음과 같은 명령어로 chatbot을 실행할 수 있습니다.
```python3 bot.py <BROADCAST_ID>```
* 본 bot에 대한 명령어와, 대응은 `DDokDDokCommand.py`에서 수정하실 수 있습니다. 기본적으로는 `!업타임` 명령어가 탑재되어있습니다.
* 그 외, 함수화된 모듈을 사용하는 법은 [Developement Reference Docs]()를 참고해주십시오. (* TODO *)

### For Developer
* 각 모듈에 대한 설명
 * `get_auth_key.py`모듈은 `client_secrets.json`파일의 정보를 기반으로, OAuth2.0 Key를 생성해줍니다. 왜냐하면, API를 Call할 때 마다 OAuth인증을 받기엔 번거로우므로, 파일로 저장해 3600초(1시간)동안 유효하게 하면 bot을 사용하는 동안은 직접적인 갱신 없이 사용 가능하기 때문입니다.
 * `bot.py`는 bot을 실제로 Youtube Streaming Livechat에 반응하게 하는 모듈입니다. `python bot.py <BROADCAST_ID>`형식으로 실행해야 합니다.
 * `youtubechat`은 YoutubeLiveStream Library가 제공하는 API들을 기능별로 세분화해서 함수화 해둔 라이브러리입니다. bot.py를 작동하는데 사용됩니다.

## 참고
* Youtube OAuth2.0 구현에 대한 사항은 이곳을 참고하시면 좋습니다.
* [Implement Youtube OAuth2.0](https://developers.google.com/youtube/v3/guides/authentication?hl=ko)
