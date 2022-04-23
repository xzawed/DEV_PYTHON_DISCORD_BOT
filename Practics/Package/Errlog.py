
import logging # log기록

import mysql

########################################################################################################################
#  전역변수
#  log 설정
Log = logging.getLogger('DEV_PYTHON_DICORD_LOG')

#  log Format
#  LogLevel = logging.ERROR
LogFileName = './Practics/log/DEV_PYTHON_DISCORD_Log.log'
#  LogFormat = logging.Formatter('[%(process)d | %(thread)d | %(levelname)s | %(filename)s:%(lineno)s] %(asctime)s: %(message)s')
LogFormat = logging.Formatter('[%(process)d | %(thread)d | %(filename)s:%(lineno)s] %(asctime)s: %(message)s')

#  Console = 콘솔화면에 출력
ConsoleHandler = logging.StreamHandler()
ConsoleHandler.setFormatter(LogFormat)

#  File = 파일에 저장처리
FileHandler = logging.FileHandler(LogFileName)
FileHandler.setFormatter(LogFormat)

#  log set
#  Log.setLevel(LogLevel)
Log.addHandler(ConsoleHandler)
Log.addHandler(FileHandler)
########################################################################################################################

########################################################################################################################
#  호출부 구현
def SaveLog(state,err):
    Log.error('MESSAGE : '+str(err))
    mysql.selmysql('LOG', (state, str(err)))
########################################################################################################################
