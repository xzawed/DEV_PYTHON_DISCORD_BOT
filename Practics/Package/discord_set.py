
import pymysql
#  호출부 구현
#  class개념
class MariaDB:
    #  MariaDB setting
    def sessionmysql(self):
        self.db = pymysql.connect(
                                    host='dirtchamber.iptime.org',
                                    port=13306,
                                    user='root',
                                    password='root',
                                    db='DEV_MARIADB',
                                    charset='utf8',
                                    autocommit=False,
                                    cursorclass=pymysql.cursors.DictCursor
                                 )
        #  DB와 관련된 커서 객체를 생성한다
        self.dictcurs = self.db.cursor(pymysql.cursors.DictCursor)
        self.curs = self.db.cursor()

    #  MariaDB 연결이후 SELECT, UPDATE, INSERT, DELETE 에 해당되는 내용을 호출처리
    def tokenmysql(self):
        sql = "SELECT TOKEN FROM BOT_TOKEN"
        self.curs.execute(sql)
        result = self.curs.fetchall()
        xzawed_token = ""
        #for val in result:
        #    xzawed_token = val[0]
        print("정상적으로 토큰값이 조회 되었습니다.")
        return xzawed_token


    #  MariaDB Close
    def closemysql(self):
        self.curs.close()
########################################################################################################################

########################################################################################################################
#  전역함수처리(외부에서 호출할때 쓰임)
def selmysql(opt):
        MariaDB.sessionmysql(self=MariaDB)

        if   opt == "TOKEN":
            MariaDB.tokenmysql(self=MariaDB)

        MariaDB.closemysql(self=MariaDB)
########################################################################################################################

#  discord에서는 token정보가 직접노출되면 난리침..다른 방법을 사용해야함.
#  xzawed_token = "OTY1MTc5ODUyMzIxODgyMTMy.YlvbyA.TQETCCRsuwYCD-VAXioi7duDGeI"