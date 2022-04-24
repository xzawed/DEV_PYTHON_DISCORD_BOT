import json

import pymysql
#  호출부 구현
#  class개념

class MariaDB:
    #  MariaDB setting
    def sessionmysql(self):
        self.db = pymysql.connect(
                                    host='xzawed.iptime.org',
                                    port=13306,
                                    user='root',
                                    password='root',
                                    db='DEV_MARIADB',
                                    charset='utf8',
                                    autocommit=False,
                                    cursorclass=pymysql.cursors.DictCursor
                                 )
        #  DB와 관련된 커서 객체를 생성한다
        self.curs = self.db.cursor()
        #  self.curs = self.db.cursor()

    #  MariaDB 연결이후 SELECT, UPDATE, INSERT, DELETE 에 해당되는 내용을 호출처리
    def tempmysql(self, data):
        sql = "SELECT %s RESULT;"
        self.curs.execute(sql, data)
        result = self.curs.fetchall()
        for x in result:
            message = x['RESULT']

        print("정상적으로 "+message+" 되었습니다.")

    #  MariaDB 연결이후 SELECT, UPDATE, INSERT, DELETE 에 해당되는 내용을 호출처리
    def tokenmysql(self, data):
        sql = "SELECT TOKEN FROM BOT_TOKEN WHERE COMCD = %s AND BOT_ID = %s; "
        self.curs.execute(sql, data)
        token_list = self.curs.fetchall()

        for x in token_list:
            xzawed_token = x['TOKEN']

        return xzawed_token

    def logmysql(self, data):
        sql = "INSERT INTO BOT_LOG ( SEQ, WRITE_DATE, STATE, LOG, COMCD ) VALUES ( nextval(JOB_LOG_SEQ), SYSDATE(), %s, %s, 'DISCORD' ) "
        self.curs.execute(sql, data)
        self.db.commit()

    def closemysql(self):
        self.curs.close()

########################################################################################################################

########################################################################################################################
#  전역함수처리(외부에서 호출할때 쓰임)
def selmysql(opt, data):
        result = ""
        MariaDB.sessionmysql(MariaDB)

        if   opt == "TEMP":
            MariaDB.tempmysql(MariaDB, data)
        elif opt == "TOKEN":
            result = MariaDB.tokenmysql(MariaDB, data)
        elif opt == "LOG":
            MariaDB.logmysql(MariaDB, data)

        MariaDB.closemysql(MariaDB)

        return result
########################################################################################################################
