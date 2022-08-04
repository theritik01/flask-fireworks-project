import mysql.connector
from numpy import product

cnx = mysql.connector.connect(user='root', password='password',host='localhost',database='fwork')
cur = cnx.cursor()
productId=10

cur.execute(' SELECT productId, name, price, description, image, stock FROM products WHERE productId = {};'.format(productId))
productData = cur.fetchone()
print(productData)

cnx.commit()
cnx.close()