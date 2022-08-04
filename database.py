import sqlite3

#Open database
conn = sqlite3.connect('database1.db')

# Create table
# conn.execute('''CREATE TABLE users 
# 		(userId INTEGER PRIMARY KEY, 
# 		password TEXT,
# 		email TEXT,
# 		firstName TEXT,
# 		lastName TEXT,
# 		address1 TEXT,
# 		address2 TEXT,
# 		zipcode TEXT,
# 		city TEXT,
# 		state TEXT,
# 		country TEXT, 
# 		phone TEXT
# 		)''')

conn.execute('''CREATE TABLE products
		(productId INTEGER PRIMARY KEY,
		name TEXT,
		price REAL,
		description TEXT,
		image TEXT,
		stock INTEGER,
		categoryId INTEGER,
		FOREIGN KEY(categoryId) REFERENCES categories(categoryId)
		)''')

# conn.execute('''CREATE TABLE kart
# 		(userId INTEGER,
# 		productId INTEGER,
# 		FOREIGN KEY(userId) REFERENCES users(userId),
# 		FOREIGN KEY(productId) REFERENCES products(productId)
# 		)''')

conn.execute('''CREATE TABLE categories
		(categoryId INTEGER PRIMARY KEY,
		name TEXT
		)''')

conn.execute('''INSERT INTO products (name, price, description, image, stock, categoryId) VALUES ('Anar', 20, 'Anardisc', 'anar.jpg', 400, 200)''')
conn.execute('''INSERT INTO products (name, price, description, image, stock, categoryId) VALUES ('Garland Crackers', 100, 'Garland Crackers disc', 'Garland Crackers.jpg', 40, 300)''')
conn.execute('''INSERT INTO products (name, price, description, image, stock, categoryId) VALUES ('Ground Chakkar', 10, 'Ground Chakkar Disc', 'Ground Chakkar.jpg', 50, 200)''')
conn.execute('''INSERT INTO products (name, price, description, image, stock, categoryId) VALUES ('sparklers', 60, 'sparklers Disc', 'sparklers.jpg', 100, 200)''')
conn.execute('''INSERT INTO products (name, price, description, image, stock, categoryId) VALUES ('Rockets', 30, 'Rockets Disc', 'Rockets.jpg', 90, 100)''')
conn.execute('''INSERT INTO products (name, price, description, image, stock, categoryId) VALUES ('Twinkling Star', 50, 'Twinkling Star Disc', 'Twinkling Star.jpg', 50, 300)''')
conn.execute('''INSERT INTO products (name, price, description, image, stock, categoryId) VALUES ('Aerial Cake', 40, 'Aerial Cake Disc', 'aerialcake.jpg', 50, 100)''')
conn.execute('''INSERT INTO products (name, price, description, image, stock, categoryId) VALUES ('Hand Torches', 45, 'Hand Torches Disc', 'handtorches.jpg', 96, 200)''')
conn.execute('''INSERT INTO products (name, price, description, image, stock, categoryId) VALUES ('Crackers', 100, 'Crackers Disc', 'crackers.jpg', 65, 009)''')
conn.execute('''INSERT INTO products (name, price, description, image, stock, categoryId) VALUES ('Dot Caps', 47, 'Dot Caps Disc', 'Dotaps.jpg', 69, 200)''')
conn.execute('''INSERT INTO products (name, price, description, image, stock, categoryId) VALUES ('Gift Box', 57, 'Gift Box Disc', 'gift box.jpg', 79, 011)''')
conn.execute('''INSERT INTO products (name, price, description, image, stock, categoryId) VALUES ('Black Serpent Eggs', 54, 'Eggs Disc', 'black serpent eggs.jpg', 49, 200)''')
conn.execute('''INSERT INTO products (name, price, description, image, stock, categoryId) VALUES ('Square Green', 65, 'Square Green Disc', 'square green.jpg', 96, 013)''')
conn.execute('''INSERT INTO products (name, price, description, image, stock, categoryId) VALUES ('Fancy Areal Repeaters', 56, 'Ariel repeaters  Disc', 'arieal.jpg', 94, 100)''')




conn.execute('''INSERT INTO categories
		(categoryId ,
		name
		) VALUES(100,'Air-Works')
        ''')

conn.execute('''INSERT INTO categories
		(categoryId ,
		name
		) VALUES(200,'Ground-Works')
        ''')
conn.execute('''INSERT INTO categories
		(categoryId ,
		name
		) VALUES(300,'Series')
        ''')

# conn.execute('''UPDATE products SET categoryId = 5000 WHERE Age<25;''')
# conn.execute('''DROP TABLE products''')
# conn.execute('''DROP TABLE categories''')
conn.commit()


conn.close()

