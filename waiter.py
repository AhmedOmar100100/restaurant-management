
import mysql.connector as connector


class Waiter:
    def __init__(self):
        self.conn = connector.connect(
            host="localhost", user="root", password="", database="restaurant")

    # insert data
    def insert_waiter(self, waiter_name, waiter_salary, waiter_phone):
        query = "INSERT INTO waiter(waiter_name,waiter_salary,waiter_phone) VALUES ('{}',{},'{}')".format(
            waiter_name, waiter_salary, waiter_phone)
        cur = self.conn.cursor()
        cur.execute(query)
        self.conn.commit()
        print("waiter inserted successfully")

    # fetch all
    def fetchAllWaiters(self):
        query = "SELECT * FROM waiter"
        cur = self.conn.cursor()
        cur.execute(query)
        for row in cur:
            print("Waiter id :", row[0])
            print("Waiter Name :", row[1])
            print("Waiter Salary :", row[2])
            print("Waiter Phone Number :", row[3])
            print("*******************************")

    # delete waiter
    def deleteWaiter(self, waiter_id):
        query = "DELETE FROM waiter WHERE waiter_id = {}".format(waiter_id)
        cur = self.conn.cursor()
        cur.execute(query)
        self.conn.commit()
        print("deleted")
    # update waiter data

    def updateWaiterName(self, waiter_id, new_name):
        query = "UPDATE waiter SET waiter_name = '{}' WHERE waiter_id = {}".format(
            new_name, waiter_id)
        cur = self.conn.cursor()
        cur.execute(query)
        self.conn.commit()
        print("updated name")

    def updateWaiterSalary(self, waiter_id, new_salary):
        query = "UPDATE waiter SET waiter_salary = {} WHERE waiter_id = {}".format(
            new_salary, waiter_id)
        cur = self.conn.cursor()
        cur.execute(query)
        self.conn.commit()
        print("updated salary")

    def updateWaiterPhone(self, waiter_id, new_phone):
        query = "UPDATE waiter SET waiter_phone = '{}' WHERE waiter_id = {}".format(
            new_phone, waiter_id)
        cur = self.conn.cursor()
        cur.execute(query)
        self.conn.commit()
        print("updated salary")
