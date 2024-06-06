# NVIDIA Jetson Nano setup

# 준비물

- Jetson Nano
- 호스트 컴
- microSD 카드(32GB 이상)
- Micro-USB 전원 어댑터(usb B타입, 옛날 안드로이드 폰 충전기): 5V-2A 추천
- USB 키보드, 마우스
- HDMI 모니터

# SD카드 굽기

- [Jetson Nano Developer Kit SD Card Image](https://developer.nvidia.com/jetson-nano-sd-card-image) 다운로드
- balenaEtcher 등으로 이미지 플래싱

# 셋업 및 부팅

※ HDMI 모니터 있을 때

1. Jetson Nano에 microSD 카드 삽입
    삽입 위치는 보드 위에 올라간 방열판쪽에 보면 있음
    ![microSD 카드 삽입 위치](https://d29g4g2dyqv443.cloudfront.net/sites/default/files/akamai/embedded/images/jetsonNano/gettingStarted/Jetson_Nano-Getting_Started-Setup-Insert_microSD-B01.png)

2. HDMI 모니터와 연결

3. 키보드, 마우스 연결

4. Micro-USB 전원 어댑터로 전원 연결
    녹색 LED가 켜지면 부팅 시작

5. 부팅이 완료되면 Ubuntu 화면이 나옴
    언어, 키보드, 시간대 선택
    사용자 생성
    APP 파티션 사이즈 선택, 최대치 추천

Jetson Nano에 기본적으로 무선랜이 없어서 무선랜카드 하나 꼽는게 편함

※ 모니터 없이 첫 부팅

1. Jetson Nano에 microSD 카드 삽입

2. 키보드, 마우스 연결

3. J48 핀을 점퍼선/점퍼캡으로 점퍼시킴
    ![J48 핀 위치](https://github.com/sleepncaffeine/sleepncaffeine/assets/101965838/e7d1287d-f7bc-40c8-9912-b491069bf7f1)

4. Micro-USB 포트와 컴퓨터 연결

5. J25 파워 잭에 DC 파워서플라이 연결
    ![J25](https://github.com/sleepncaffeine/sleepncaffeine/assets/101965838/e7d1287d-f7bc-40c8-9912-b491069bf7f1)
    꽂으면 자동으로 부팅됨, 1분 가량 소요

6. 호스트 컴에서 시리얼 포트 확인, 시리얼 연결 통해서 쉘 접속
    보드레이트 115200

