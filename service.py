from database.db import get_connection

def get_allKnowledge():
    with get_connection() as con:
        cur = con.cursor() 
        cur.execute("SELECT * FROM products") 
        rows = cur.fetchall()
        if not rows:
            return [] 
        
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
        cur.execute(
        "SELECT * FROM products WHERE id = ?", (id,))
        row = cur.fetchone() 
        if not row:
            return None

        data = {
            "id":row[0],
            "name":row[1],
            "price":row[2]
        }
        return data

def add_knowledge(name, price):
    with get_connection() as con:
        cur = con.cursor()
        cur.execute(
        "SELECT 1 FROM products WHERE LOWER(name) = LOWER(?)",
        (name,)
        ) 
        if cur.fetchone():
            raise Exception("Product already exists") 
        cur.execute("INSERT INTO products (name, price) VALUES (?, ?) RETURNING id, name, price", (name, price))
        row = cur.fetchone()
        item = {
            "id": row[0],
            "name": row[1],
            "price": row[2]
        }
        return item 
    
def update_knowledge(id, name=None, price=None):
    with get_connection() as con:
        cur = con.cursor()

        cur.execute("SELECT * FROM products WHERE id = ?", (id,))
        row = cur.fetchone()

        if not row:
            return {
                "status": 400,
                "eroare": "Produsul nu exista"
            }

        if price is not None:
            cur.execute("UPDATE products SET price = ? WHERE id = ?", (price, id))

        con.commit()

        cur.execute("SELECT * FROM products WHERE id = ?", (id,))
        updated = cur.fetchone()

        return {
            "data": {
                "id": updated[0],
                "name": updated[1],
                "price": updated[2]
            }
        }

