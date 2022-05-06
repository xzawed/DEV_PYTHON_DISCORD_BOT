
import logging # log기록

import mariadb
import traceback

########################################################################################################################
#  전역변수
#  log 설정
Log = logging.getLogger('DEV_PYTHON_DICORD_LOG')

#  log Format
#  LogLevel = logging.ERROR
LogFileName = './Practics/log/DEV_PYTHON_DISCORD_Log.log'
#  LogFormat = logging.Formatter('[%(process)d | %(thread)d | %(levelname)s | %(filename)s:%(lineno)s] %(asctime)s: %(message)s')
LogFormat = logging.Formatter('DISCORD|[%(process)d | %(thread)d | %(filename)s:%(lineno)s] %(asctime)s: %(message)s')

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
def saveLog(state):
    err = traceback.format_exc()
    if   state == "INFO":
        Log.info('MESSAGE : ' + str(err))
    elif state == "ERROR":
        Log.error('MESSAGE : '+ str(err))
    mariadb.selmysql('LOG', (state, str(err)))
########################################################################################################################
