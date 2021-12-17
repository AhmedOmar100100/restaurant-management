import mysql.connector as connector


class Customer:
    def __init__(self):
        self.conn = connector.connect(
            host="localhost", user="root", password="", database="restaurant")

    # insert data
    def insert_customer(self, customer_name, customer_address, customer_phone, waiter_id):
        query = "INSERT INTO customer(customer_name,customer_address,customer_phone,waiter_id) VALUES ('{}','{}','{}',{})".format(
            customer_name, customer_address, customer_phone, waiter_id)
        cur = self.conn.cursor()
        cur.execute(query)
        self.conn.commit()
        print("customer data inserted successfully")

    # fetch all
    def fetchAllCustomers(self):
        query = "SELECT * FROM customer"
        cur = self.conn.cursor()
        cur.execute(query)
        for row in cur:
            print("customer id :", row[0])
            print("customer Name :", row[1])
            print("customer address :", row[2])
            print("customer phone number :", row[3])
            print("*******************************")

    # delete customer
    def deleteCustomer(self, customer_id):
        query = "DELETE FROM customer WHERE customer_id = {}".format(
            customer_id)
        cur = self.conn.cursor()
        cur.execute(query)
        self.conn.commit()
        print("deleted")
    # update customer data

    def updateCustomerName(self, customer_id, new_name):
        query = "UPDATE customer SET customer_name = '{}' WHERE customer_id = {}".format(
            new_name, customer_id)
        cur = self.conn.cursor()
        cur.execute(query)
        self.conn.commit()
        print("updated name")

    def updateCustomerAddress(self, customer_id, new_address):
        query = "UPDATE customer SET customer_address = {} WHERE customer_id = {}".format(
            new_address, customer_id)
        cur = self.conn.cursor()
        cur.execute(query)
        self.conn.commit()
        print("updated address")

    def updateCustomerPhone(self, customer_id, new_phone):
        query = "UPDATE customer SET customer_phone = {} WHERE customer_id = {}".format(
            new_phone, customer_id)
        cur = self.conn.cursor()
        cur.execute(query)
        self.conn.commit()
        print("updated phone number")
