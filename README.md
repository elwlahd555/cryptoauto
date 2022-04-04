# cryptoauto

## Windows 인공지능 (Prophet) 자동매매 환경 설치 방법

<summary>아나콘다(https://www.anaconda.com/) 설치</summary>
<summary>pip install pyupbit</summary>
<summary>pip install schedule</summary>
<summary>conda install -c conda-forge fbprophet</summary>
<summary>pip install pystan --upgrade</summary>

## Ubuntu 20.4 인공지능 (Prophet) 자동매매 환경 설치 방법

<summary>4GB이상 RAM 필요 (AWS t2.medium 이상)</summary>
<summary>sudo apt update</summary>
<summary>sudo ln -sf /usr/share/zoneinfo/Asia/Seoul /etc/localtime</summary>
<summary>sudo apt install python3-pip</summary>
<summary>pip3 install pyupbit</summary>
<summary>pip3 install schedule</summary>
<summary>pip3 install pystan==2.19.1.1</summary>
<summary>pip3 install convertdate</summary>
<summary>pip3 install fbprophet</summary>

## Ubuntu 서버 명령어

<summary>(\*추가)한국 기준으로 서버 시간 설정: sudo ln -sf /usr/share/zoneinfo/Asia/Seoul /etc/localtime</summary>
<summary>현재 경로 상세 출력: ls -al</summary>
<summary>경로 이동: cd 경로</summary>
<summary>vim 에디터로 파일 열기: vim bitcoinAutoTrade.py</summary>
<summary>vim 에디터 입력: i</summary>
<summary>vim 에디터 저장: :wq!</summary>
<summary>패키지 목록 업데이트: sudo apt update</summary>
<summary>pip3 설치: sudo apt install python3-pip</summary>
<summary>pip3로 pyupbit 설치: pip3 install pyupbit</summary>
<summary>백그라운드 실행: nohup python3 bitcoinAutoTrade.py > output.log &</summary>
<summary>실행되고 있는지 확인: ps ax | grep .py</summary>
<summary>프로세스 종료(PID는 ps ax | grep .py를 했을때 확인 가능): kill -9 PID</summary>
