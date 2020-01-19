# -*- conding: utf-8 -*-
# @Time      :2019/9/11 17:23
# Author     :chengjin
# @Email     :amazing2013@163.com
# @File      :do_mysql.py
import pymysql
class DoMysql:
    def get_data(self,sheet_name):
        conn = pymysql.connect(
            host="192.168.6.119",
            port=3306,
            user="root",
            passwd="123456",
            db="course"
        )
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM "+sheet_name)
        all_data= cursor.fetchall()

        row = []
        for i in all_data:
            a = 0
            index = {}
            for j in i:
                if a ==0:
                    index["case_id"]=eval(j)
                elif a==1:
                    index["model"] = j
                elif a==2:
                    index["title"] = j
                elif a==3:
                    index["url"] = j
                elif a==4:
                    index["params"] = j
                elif a==5:
                    index["header"] = j
                elif a==6:
                    index["http_method"] = j
                elif a==7:
                    index["data"] = j
                elif a==8:
                    index["excepted_code"] = eval(j)
                a += 1
            row.append(index)
        # print(row)

        cursor.close()
        conn.close()
        return row

if __name__ == '__main__':
    data  = DoMysql().get_data("review")

    print(data)
    print(type(data[0]))







