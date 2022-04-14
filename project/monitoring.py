# import telegram
# from telegram.ext import Updater
# from telegram.ext import MessageHandler, Filters
import configparser
import subprocess
import logging
from threading import Timer 
import os

### config 관련 코드
def read_config():
    # config파싱 객체 생성
    properties = configparser.ConfigParser()
    # config.ini 파일 읽기
    properties.read('./config.ini')

    # 섹션 값 읽기
    system_config = properties['SYSTEM']
    timeout = system_config['TIMEOUT'] # 모니터링 주기
    port = system_config['PORT'] # 포트 번호
    
    return timeout, port



### netstat 명령어 관련 코드
def execute_netstat():
    # 실행할 os명령어
    cmd = 'netstat -an | find /I /N "0.0.0.0:{}"'.format(PORT)
    # 실행 결과 읽기
    sysMsg = subprocess.getstatusoutput(cmd)[1]

    # 실행결과 로그 생성
    if sysMsg: 
        logger.info(sysMsg)
    # 포트 닫혀있을 때 (명령어 결과값이 공백일 때)
    elif sysMsg == '': 
        logger.error('%s 포트가 닫혀 있습니다.', PORT)

    # 반복 실행
    # Timer(int(read_config()[0]), execute_netstat).start()



### 로그파일 모니터링 관련 코드
def monitor_log():
    print(os.path.abspath(__file__))
    f = open("log.txt")



### 로그 관련 코드 
#로그 객체 생성
logger = logging.getLogger()

# 로그출력 기준설정
logger.setLevel(logging.INFO)

# 로그 출력 형식 지정 및 출력
formatter = logging.Formatter('%(asctime)s %(levelname)s - %(message)s')
stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)
logger.addHandler(stream_handler)

# 로그 파일에 저장
file_handler = logging.FileHandler('log.txt', encoding='UTF8')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)








### 텔레그램 관련 코드
# token = '5136451453:AAGARgxHpZkFZLYMSkQTJa1k1374uKp5FHw'
# id = '5275000604'

# bot = telegram.Bot(token = token)

        



### __main__
if __name__=="__main__":
    TIMEOUT = read_config()[0]
    PORT    = read_config()[1]

    logger.info('========== MONITORING START ==========')
    logger.info('[CONFIG] 환경설정 READ [SYSTEM-TIMEOUT : %s] - 모니터링 주기 시간', TIMEOUT)
    logger.info('[CONFIG] 환경설정 READ [SYSTEM-PORT : %s] - 포트 번호', PORT)

    execute_netstat()
    monitor_log()