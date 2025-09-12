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
    cur.execute('INSERT into player_stats VALUES (?,?,?)', session, score, q_answered)
    db.commit()