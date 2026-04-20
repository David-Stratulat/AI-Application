from database.db import get_connection
from exceptions import DuplicateException

def get_allKnowledge():
    with get_connection() as con:  
        cur = con.cursor()
        cur.execute(
            "SELECT * FROM products" 
        )
        rows = cur.fetchall() 
        if not rows:
            return None 
        
        content = []
        for row in rows:
            content.append({
                "id": row[0],
                "name":row[1],
                "price":row[2]
            }) 

        return content
        
def get_knowledge(id):
    with get_connection() as con:
        cur = con.cursor()
        cur.execute("SELECT * FROM products WHERE id = ?", (id,))
        row = cur.fetchone()

        if not row:
            return None

        return {
            "id": row[0],
            "name": row[1],
            "price": row[2]
        }   

def add_knowledge(name, price):
    with get_connection() as con:
        cur = con.cursor()

        # verificam duplicatul
        cur.execute(
            "SELECT 1 FROM products WHERE LOWER(name) = LOWER(?)",
            (name,)
        )
        if cur.fetchone():
            raise DuplicateException("Product already exists")

        # inseram
        cur.execute(
            "INSERT INTO products (name, price) VALUES (?, ?)",
            (name, price)
        )

        new_id = cur.lastrowid

        return {
            "id": new_id,
            "name": name,
            "price": price
        }