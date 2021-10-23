import psycopg2

connection = psycopg2.connect('dbname=example')

curser = connection.curser()

curser.execute('''
CREATE TABLE table2 (
    id INTERGER PRIMARY KEY,
    completed BOOLEAN NOT NULL DEFAULT False
    );
    ''')

curser.execute('INSERT INTO table2 (id, completed) VALUES(1, true);')

connection.commit()

connection.close()
curser.close()