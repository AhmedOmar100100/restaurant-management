# school management system
# students , teachers , employees , subjects
# 10/1 compiler
# 13/1 computer vision
# 25/1 parallel
# 26/1 machine learning
# 29/1 human rights
# 31/1 wireless
# star uml
import mysql.connector as connector


class Chef:
    def __init__(self):
        self.conn = connector.connect(
            host="localhost", user="root", password="", database="restaurant")

    # insert data
    def insert_chef(self, chef_name, chef_salary):
        query = "INSERT INTO chef(chef_name,chef_salary) VALUES ('{}',{})".format(
            chef_name, chef_salary)
        cur = self.conn.cursor()
        cur.execute(query)
        self.conn.commit()
        print("chef inserted successfully")

    # fetch all
    def fetchAllChefs(self):
        query = "SELECT * FROM chef"
        cur = self.conn.cursor()
        cur.execute(query)
        for row in cur:
            print("chef id :", row[0])
            print("chef Name :", row[1])
            print("chef Salary :", row[2])
            print("*******************************")

    # delete chef
    def deleteChef(self, chef_id):
        query = "DELETE FROM chef WHERE chef_id = {}".format(chef_id)
        cur = self.conn.cursor()
        cur.execute(query)
        self.conn.commit()
        print("deleted")
    # update chef data

    def updateChefName(self, chef_id, new_name):
        query = "UPDATE chef SET chef_name = '{}' WHERE chef_id = {}".format(
            new_name, chef_id)
        cur = self.conn.cursor()
        cur.execute(query)
        self.conn.commit()
        print("updated name")

    def updateChefSalary(self, chef_id, new_salary):
        query = "UPDATE chef SET chef_salary = {} WHERE chef_id = {}".format(
            new_salary, chef_id)
        cur = self.conn.cursor()
        cur.execute(query)
        self.conn.commit()
        print("updated salary")
