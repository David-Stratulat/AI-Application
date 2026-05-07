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
        
        
def get_product_by_id(id):
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
    
def get_product_by_name(name):
    with get_connection() as con:
        cur = con.cursor()

        cur.execute(
            "SELECT * FROM products WHERE LOWER(name) LIKE LOWER(?)",
            (f"%{name}%",)
        )

        rows = cur.fetchall()

        if not rows:
            return []

        produse = []
        for row in rows:
            produse.append({
                "id": row[0],
                "name": row[1],
                "price": row[2]
            })

        return produse


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
    
def update_product_price(produs_id, new_price):
    with get_connection() as con:
        cur = con.cursor()
        cur.execute("SELECT id, name, price FROM products WHERE id = ?", (produs_id,))
        product = cur.fetchone()
        
        if not product:
            return None
            
        current_price = product[2]
        
        if float(new_price) == float(current_price):
            raise Exception(f"Noul pret ({new_price}) este identic cu pretul actual.")
        
        cur.execute("UPDATE products SET price = ? WHERE id = ? RETURNING id, name, price", (new_price, produs_id))
        row = cur.fetchone()
        return {
            "id": row[0],
            "name": row[1],
            "price": row[2]
        }