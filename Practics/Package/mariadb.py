
import pymysql
#  개별적 으로 생성한 내용

import Errlog
#  호출부 구현
#  class 개념


class MariaDB:

    sql = ""
    db = type(None)
    curs = type(None)
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
        #  DB와 관련된 커서 객체를 생성 한다
        self.curs = self.db.cursor()
        #  self.curs = self.db.cursor()

    #  MariaDB 연결 이후 SELECT, UPDATE, INSERT, DELETE 에 해당 되는 내용을 호출 처리
    def tempmysql(self, data):
        self.sql = "SELECT %s RESULT;"
        self.curs.execute(self.sql, data)
        result = self.curs.fetchall()
        message = ""
        for x in result:
            message = x['RESULT']

        print("정상적 으로 " + message + " 되었 습니다.")

    #  MariaDB 연결 이후 SELECT, UPDATE, INSERT, DELETE 에 해당 되는 내용을 호출 처리
    def tokenmysql(self, data):
        self.sql = "SELECT TOKEN FROM BOT_TOKEN WHERE COMCD = %s AND BOT_ID = %s; "
        self.curs.execute(self.sql, data)
        token_list = self.curs.fetchall()
        xzawed_token = ""
        for x in token_list:
            xzawed_token = x['TOKEN']

        return xzawed_token

    def logmysql(self, data):
        self.sql = "INSERT INTO BOT_LOG ( SEQ, WRITE_DATE, STATE, LOG, COMCD ) VALUES ( nextval(JOB_LOG_SEQ), SYSDATE(), %s, %s, 'DISCORD' ) "
        self.curs.execute(self.sql, data)
        self.db.commit()

    def closemysql(self):
        self.curs.close()


########################################################################################################################

########################################################################################################################
#  전역 함수 처리( 외부 에서 호출 할 때 쓰임)
class MYSQL(MariaDB):

    def selmysql(self, opt, data):
        try:
            result = ""
            super(MYSQL, self).sessionmysql(self)
            #  print("정상적 으로 MariaDB에 연결 되었 습니다.")
            if   opt == "TEMP":
                super(MYSQL, self).tempmysql(self, data)
            elif opt == "TOKEN":
                result = super(MYSQL, self).tokenmysql(self, data)
            elif opt == "LOG":
                super(MYSQL, self).logmysql(self, data)

            super(MYSQL, self).closemysql(self)
            #  print("정상적 으로 MariaDB에 연결 해제 되었 습니다.")

            return result
        except Exception:
            Errlog.savelog('ERROR')
########################################################################################################################
