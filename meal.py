import mysql.connector as connector


class Meal:
    def __init__(self):
        self.conn = connector.connect(
            host="localhost", user="root", password="", database="restaurant")

    # insert data
    def insert_meal(self, meal_name, meal_price, chef_id):
        query = "INSERT INTO meal(meal_name,meal_price,chef_id) VALUES ('{}',{},{})".format(
            meal_name, meal_price, chef_id)
        cur = self.conn.cursor()
        cur.execute(query)
        self.conn.commit()
        print("meal inserted successfully")

    # fetch all
    def fetchAllMeals(self):
        query = "SELECT meal_id,meal_name,meal_price,chef_name FROM meal,chef WHERE meal.chef_id = chef.chef_id"
        cur = self.conn.cursor()
        cur.execute(query)
        for row in cur:
            print("meal id :", row[0])
            print("meal Name :", row[1])
            print("meal price :", row[2])
            print("chef name :", row[3])
            print("*******************************")

    # delete meal

    def deleteMeal(self, meal_id):
        query = "DELETE FROM meal WHERE meal_id = {}".format(meal_id)
        cur = self.conn.cursor()
        cur.execute(query)
        self.conn.commit()
        print("deleted")
    # update meal data

    def updateMealName(self, meal_id, new_name):
        query = "UPDATE meal SET meal_name = '{}' WHERE meal_id = {}".format(
            new_name, meal_id)
        cur = self.conn.cursor()
        cur.execute(query)
        self.conn.commit()
        print("updated name")

    def updateMealPrice(self, meal_id, new_price):
        query = "UPDATE meal SET meal_price = {} WHERE meal_id = {}".format(
            new_price, meal_id)
        cur = self.conn.cursor()
        cur.execute(query)
        self.conn.commit()
        print("updated salary")

    def updateMealChef(self, meal_id, new_chef):
        query = "UPDATE meal SET chef_id = {} WHERE meal_id = {}".format(
            new_chef, meal_id)
        cur = self.conn.cursor()
        cur.execute(query)
        self.conn.commit()
        print("updated meal chef")
