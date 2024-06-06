# Google Coral Dev Board Setup

# 준비물

- Google Coral Dev Board
- 호스트 컴
    - Python3 설치됨
- 8GB 이상 microSD 카드
- USB-C 전원 어댑터
- USB-C to USB-A 케이블
- Windows 한정: Git Bash 추천됨

# OS 플래싱
SD카드 있을 때, 없으면 USB로 [플래싱](https://coral.ai/docs/dev-board/reflash/#flash-a-new-board) 가능

1. SD카드 이미지 [다운로드](https://dl.google.com/coral/mendel/enterprise/enterprise-eagle-flashcard-20211117215217.zip)

2. balenaEtcher 등으로 이미지 플래싱

3. ※ Dev Board에 전원 연결 없는 상태에서
    SD 카드 부팅 모드로 전환
    부팅모드 스위치를 1234 순서대로 위 아래 위 위 로 둠
    ![부트 스위치](https://coral.ai/static/docs/images/devboard/devboard-bootmode-sdcard.jpg)

4. SD카드 삽입

5. "PWR" USB-C 포트에 전원 연결
    빨간 LED 불 들어옴
    SD카드 이미지 읽어서 보드 플래싱 자동으로 함
    5~10분가량 소요, 끝나면 자동으로 LED 꺼짐

6. 끝나면 전원 뽑고 SD카드 제거

7. 부팅모드를 eMMC로 전환
    부팅모드 스위치를 1234 순서대로 위 아래 아래 아래 로 둠
    ![부트 스위치](https://coral.ai/static/docs/images/devboard/devboard-bootmode-emmc.jpg)

8. "PWR" USB-C 포트에 전원 연결
    Mendel Linux로 부팅됨
    초기 부팅 시 시간 좀 소요됨

# MDT 설치

호스트 컴퓨터에 MDT를 설치
Coral Dev Board와 상호작용할 수 있게 하는 도구

`python3 -m pip install --user mendel-development-tool`

`mdt`가 `PATH`가 아닌 다른 경로에 설치되었다고 할 시 환경변수에 넣어주기

# MDT를 통해 Dev Board Shell에 접속

Dev Board의 "OTG" USB-C 포트에 USB-C to USB-A 케이블로 호스트 컴퓨터 연결

`mdt devices`로 연결된 디바이스 확인
대충 `orange-horse        (192.168.100.2)` 이런식으로 나옴
디바이스 보이면 `mdt shell`로 쉘 접속

## SSH로 접속

최소 한번은 MDT로 접속해야 SSH 가능
SSH 키 생성 후 MDT로 퍼블릭 키 전송하면 그 뒤로 SSH로 접속 가능
```bash
ssh-keygen
# ssh 키 생성

mdt pushkey ~/.ssh/id_rsa.pub

ssh mendel@192.168.100.2
```

# 인터넷 접속

`nmcli dev wifi connect <NETWORK_NAME> password <PASSWORD> ifname wlan0`
위 명령어로 하고
`nmcli connection show`하면 연결된 네트워크 확인 가능