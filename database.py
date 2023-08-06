import sqlite3
from post_it import Postit
from typing import List

conn = sqlite3.connect('postit.db')
c = conn.cursor()

def create_table():
    c.execute('''CREATE TABLE IF NOT EXISTS postits (
              id integer PRIMARY KEY,
              text text,
              priority integer
            )''')
    
create_table()

def get_all_postits() -> List[Postit]:
    c.execute('select * FROM postits')
    results = c.fetchall()
    postits = []
    for result in results:
        postits.append(Postit(id=result[0], text=result[1], priority=result[2]))

    return postits

def insert_postit(postit: Postit):
    c.execute('select count(*) FROM postits')
    count = c.fetchone()[0]
    with conn:
        c.execute('INSERT INTO postits (text, priority) VALUES (?,?)',
                  (postit.text, postit.priority))
        
def delete_postit(id):
    c.execute('select count(*) FROM postits')
    count = c.fetchone()[0]
    with conn:
        c.execute('DELETE FROM postits WHERE id=:id', {'id':id})

def edit_priority(id, priority):
    with conn:
        c.execute('UPDATE postits SET priority = :priority WHERE id = :id',
                  {'id':id, 'priority':priority})
        
def edit_text(id, text):
    with conn:
        c.execute('UPDATE postits SET text = :text WHERE id = :id',
                  {'id':id, 'text':text})