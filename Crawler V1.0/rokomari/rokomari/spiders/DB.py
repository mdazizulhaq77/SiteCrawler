import mysql.connector
import mysql.connector.locales.eng.client_error
class DB(object):
    cnx = None

    def __init__(self):
        print("Construct....")
        self.cnx = mysql.connector.connect(user='crawler', password='forfun',
                              host='127.0.0.1',
                              database='beshilove_crawler')

    def exec(self, sql, param):
        cursor = self.cnx.cursor();
        #sql = ( "insert into products(product_name, category, author, imageid, company) "
        #    "values('test', 'test', 'test', 'tesy', 'test') ")
        cursor.execute(sql, param);
        cursor.close()


    def __del__(self):
        self.cnx.close();    

    def close(self):
        self.cnx.close();    
