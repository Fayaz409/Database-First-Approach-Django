from django.db import connections

def get_connection(alias='default'):
    """
    Return a Django DB‑API connection for the given DATABASES alias.
    """
    return connections[alias]

def fetch_orders_with_details_raw(alias='default'):
    """
    Run a raw‑SQL INNER JOIN across Orders, Order Details, Customers and Products.
    Returns a list of dicts, one per joined row.
    """
    conn = get_connection(alias)
    with conn.cursor() as cursor:
        cursor.execute("""
            SELECT
                a.OrderID,
                a.OrderDate,
                b.CompanyName,
                c.ProductName,
                d.UnitPrice,
                d.Quantity,
                (d.UnitPrice * d.Quantity) AS BillAmount
            FROM `orders` AS a
            INNER JOIN `order details` AS d
                ON a.OrderID = d.OrderID
            INNER JOIN `customers` AS b
                ON a.CustomerID = b.CustomerID
            INNER JOIN `products` AS c
                ON d.ProductID = c.ProductID;
        """)
        cols = [col[0] for col in cursor.description]
        rows = cursor.fetchall()

    return [dict(zip(cols, row)) for row in rows]
