import sqlite3 as sql

def get_db(name='main.db'):
    db = sql.connect(name)
    create_table(db)
    return db

def create_table(db):
    cur = db.cursor()
    
    cur.execute(
        '''CREATE TABLE IF NOT EXISTS player_stats (
        session TEXT PRIMARY KEY, 
        score INTEGER,
        q_answered INTEGER)'''
        )
    
    db.commit()

def add_to_main_db(db, session, score, q_answered):
    cur = db.cursor()
    cur.execute('INSERT into player_stats VALUES (?,?,?)', (session, score, q_answered))
    db.commit()

def show_db(db):
    cur = db.cursor()
    cur.execute('SELECT * FROM player_stats')
    rows = cur.fetchall()
    for i in rows:
        print(i)

def get_db_connection(db):
    conn = sql.connect(db)
    return conn

def get_q(db, id):
    cur = db.cursor()
    cur.execute('SELECT q_answered FROM player_stats WHERE session=?', (id,))
    rows = cur.fetchall()
    for i in rows:
        print(i)
    return rows[0][0]

def create_answer_table(db):
    cur = db.cursor()
    
    cur.execute(
        '''CREATE TABLE IF NOT EXISTS q_and_a (
        q INTEGER PRIMARY KEY, 
        a TEXT
        )'''
        )
    
    
    db.commit()
    
    with open('data.txt', 'r') as file:
        lst = file.readlines()


    print(f'q:{lst[0]} a:{lst[1]}')
    cur.execute('INSERT OR IGNORE into q_and_a VALUES (?,?)', (lst[0], lst[1]))
    db.commit()

    