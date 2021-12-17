import mysql.connector as connector


class Orders:
    def __init__(self):
        self.conn = connector.connect(
            host="localhost", user="root", password="", database="restaurant")

    def makeOrder(self, customer_id, meal_id):
        query = "INSERT INTO orders(customer_id,meal_id) VALUES ({},{})".format(
            customer_id, meal_id)
        cur = self.conn.cursor()
        cur.execute(query)
        self.conn.commit()
        print("order inserted successfully")

    def fetchAllOrders(self):
        query = "SELECT * FROM orders"
        cur = self.conn.cursor()
        cur.execute(query)
        for row in cur:
            print("customer id :", row[0])
            print("meal id:", row[1])

            print("*******************************")
