import pymysql
# Python connect with Mysql
con= pymysql.Connect(host="localhost", user="soussi", passwd="pass", db="python_db")

mycursor = con.cursor()

#mycursor.execute("INSERT INTO user(id,title,description,author) VALUES(3,'python and mysql2','connect python with Mysql','soussi');")

print("user inserted")
# creat table
querry="""CREATE TABLE FILM 
(
id int primary key,
title varchar(120),
gener varchar(50)
)"""

mycursor.execute(querry)
# update table
mycursor.execute("UPDATE user SET title ='kotlin for dev' WHERE id=3;")

# drop table
mycursor.execute("DELETE FROM user WHERE id=2;")

con.commit()
con.close()