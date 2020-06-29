import psycopg2

def create_table():
    conn=psycopg2.connect("dbname='db1' user='postgres' password='postgres123' host= 'localhost' port='5432'")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)")
    conn.commit()
    conn.close

def insert(item, quantity, price):
    conn=psycopg2.connect("dbname='db1' user='postgres' password='postgres123' host= 'localhost' port='5432'")
    cur=conn.cursor()
    cur.execute("INSERT INTO store VALUES(%s,%s,%s)", (item, quantity, price))
    conn.commit()
    conn.close

def view():
    conn=psycopg2.connect("dbname='db1' user='postgres' password='postgres123' host= 'localhost' port='5432'")
    cur=conn.cursor()
    cur.execute("SELECT * FROM store")
    rows=cur.fetchall()
    conn.close
    return rows

def delete(item):
    conn=psycopg2.connect("dbname='db1' user='postgres' password='postgres123' host= 'localhost' port='5432'")
    cur=conn.cursor()
    cur.execute("DELETE FROM store WHERE item=%s", (item,))
    rows=cur.fetchall()
    conn.close
    conn.commit()

def update(quantity, price, item):
    conn=psycopg2.connect("dbname='db1' user='postgres' password='postgres123' host= 'localhost' port='5432'")
    cur=conn.cursor()
    cur.execute("UPDATE store SET quantity=%s, price=%s WHERE item=%s",(quantity, price, item))
    conn.close
    conn.commit()

update(11, 6, "Apple")
create_table()
insert("Apple",10,15)
print(view())
delete("Apple")
