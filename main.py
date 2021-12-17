from chef import Chef
from customer import Customer
from waiter import Waiter
from meal import Meal
from orders import Orders
# main coding


def main():
    print("***************** Welcome To Restaurant management System **************************\n\n")
    userName = input("Enter Your Name: ")
    print()

    while True:
        print("Choose what do you want to do , ", userName, " ? ")
        print("==================================")
        print("Press 1 to manage chefs")
        print("Press 2 to manage customers")
        print("Press 3 to manage waiter")
        print("Press 4 to manage Meals")
        print("Press 5 to manage orders")
        print("press 6 to exit the program !")
        print("==================================")

        try:
            choice = int(input("Enter Choice : "))
        except:
            print("invalid try again!")
        if choice == 1:
            chef = Chef()

            print(
                "You are now in chef management dashboard\nwhat do you want to do?")
            print("1. Insert new chef to restaurant")
            print("2. Delete existing chef from restaurant by his id")
            print("3. update name of existing chef")
            print("4. update salary of existing chef")
            print("5. generate report for all chefs in the restaurant")

            try:
                chef_choice = int(input("My choice is : "))
                if chef_choice == 1:
                    try:
                        chefName = input("Enter Chef Name: ")
                        chefSalary = float(input("Enter Chef Salary: "))
                        chef.insert_chef(chefName, chefSalary)

                    except:
                        print("please enter valid data:(!!!!!")
                elif chef_choice == 2:
                    try:
                        chefId = int(input("Enter Chef Id: "))
                        chef.deleteChef(chefId)
                    except:
                        print("Invalid id !!")
                elif chef_choice == 3:

                    try:
                        chefId = int(input("Please enter chef id: "))
                        chefNewName = input("Please Insert New name : ")
                        chef.updateChefName(chefId, chefNewName)
                    except:
                        print("enter valid data")
                elif chef_choice == 4:
                    try:
                        chefId = int(input("Please enter chef id: "))
                        chefNewSalary = float(
                            input("Please Insert New salary for the chef : "))
                        chef.updateChefSalary(chefId, chefNewSalary)
                    except:
                        print("Enter valid data")
                elif chef_choice == 5:
                    chef.fetchAllChefs()

            except:
                print("invalid input try entering valid one")
        elif choice == 2:
            customer = Customer()

            print(
                "You are now in customer management dashboard\nwhat do you want to do?")
            print("1. Insert new customer to restaurant")
            print("2. Delete existing customer from restaurant by his id")
            print("3. update name of existing customer")
            print("4. update address of existing customer")
            print("4. update phone of existing customer")
            print("5. generate report for all customer in the restaurant")

            try:
                customer_choice = int(input("My choice is : "))
                if customer_choice == 1:
                    try:
                        customerName = input("Enter Customer Name: ")
                        customerAddress = input("Enter customer address: ")
                        customerPhone = input("Enter customer phone: ")
                        waiterId = int(input("Enter waiter id: "))
                        customer.insert_customer(
                            customerName, customerAddress, customerPhone, waiterId)

                    except:
                        print("no lol")

                elif customer_choice == 2:
                    try:
                        customerId = int(input("Enter Customer Id: "))
                        customer.deleteCustomer(customerId)
                    except:
                        print("Invalid id !!")
                elif customer_choice == 3:

                    try:
                        customerId = int(input("Please enter customer id: "))
                        customerNewName = input("Please Insert New name : ")
                        customer.updateCustomerName(
                            customerId, customerNewName)
                    except:
                        print("enter valid data")
                elif customer_choice == 4:
                    try:
                        customerId = int(input("Please enter customer id: "))
                        customerNewAddress = input(
                            "Please Insert New address for the customer : ")
                        customer.updateCustomerAddress(
                            customerId, customerNewAddress)
                    except:
                        print("Enter valid data")
                elif customer_choice == 5:
                    customer.fetchAllCustomers()

                elif customer_choice == 6:
                    customer.fetchAllCustomers()

            except:
                print("invalid input try entering valid one")
        elif choice == 3:
            waiter = Waiter()
            print(
                "You are now in Waiter management dashboard\nwhat do you want to do?")
            print("1. Insert new Waiter to restaurant")
            print("2. Delete existing Waiter from restaurant by his id")
            print("3. update name of existing Waiter")
            print("4. update salary of existing Waiter")
            print("5. update phone of existing Waiter")
            print("6. generate report for all Waiter in the restaurant")

            try:
                waiter_choice = int(input("My choice is : "))
            except:
                print("invalid input try entering valid one")
            if waiter_choice == 1:

                wName = input("Enter Waiter Name: ")
                wSalary = float(input("Enter waiter Salary: "))
                wPhone = input("Enter Waiter phone: ")

                waiter.insert_waiter(wName, wSalary, wPhone)

            elif waiter_choice == 2:
                try:
                    waiterId = int(input("Enter Waiter Id: "))
                except:
                    print("Invalid id !!")
                waiter.deleteWaiter(waiterId)

            elif waiter_choice == 3:
                try:
                    waiterId = int(input("Please enter waiter id: "))
                    waiterNewName = input("Please Insert New name : ")

                except:
                    print("enter valid data")
                waiter.updateWaiterName(waiterId, waiterNewName)
            elif waiter_choice == 4:
                try:
                    waiterId = int(input("Please enter waiter id: "))
                    waiterNewSalary = float(
                        input("Please Insert New salary for the waiter : "))

                except:
                    print("Enter valid data")
                waiter.updateWaiterSalary(
                    waiterId, waiterNewSalary)
            elif waiter_choice == 5:
                try:
                    waiterId = int(input("Please enter waiter id: "))
                    waiterNewPhone = input(
                        "Please Insert New phone for the waiter : ")
                    waiter.updateWaiterPhone(waiterId, waiterNewPhone)
                except:
                    print("Enter valid data")
            elif waiter_choice == 6:
                waiter.fetchAllWaiters()

        elif choice == 4:
            meal = Meal()
            chef = Chef()

            print("You are now in meal management dashboard\nwhat do you want to do?")
            print("1. Insert new meal to restaurant")
            print("2. Delete existing meal from restaurant by his id")
            print("3. update name of existing meal")
            print("4. update price of existing meal")
            print("5. update chef of existing meal")
            print("6. generate report for all meals in the restaurant")

            try:
                meal_choice = int(input("My choice is : "))
                if meal_choice == 1:
                    try:
                        mealName = input("Enter meal Name: ")
                        mealPrice = float(input("Enter meal price: "))
                        print("choose chef From Here: ")
                        chef.fetchAllChefs()
                        chef_id = int(input("Enter Chef ID for the meal: "))
                        meal.insert_meal(mealName, mealPrice, chef_id)

                    except:
                        print("please enter valid data:(!!!!!")
                elif meal_choice == 2:
                    try:
                        mealId = int(input("Enter Meal Id: "))
                        chef.deleteChef(mealId)
                    except:
                        print("Invalid id !!")
                elif meal_choice == 3:

                    try:
                        mealId = int(input("Please enter meal id: "))
                        mealNewName = input("Please Insert New name : ")
                        meal.updateMealName(mealId, mealNewName)
                    except:
                        print("enter valid data")
                elif meal_choice == 4:
                    try:
                        mealId = int(input("Please enter meal id: "))
                        mealNewPrice = float(
                            input("Please Insert New Price for the Meal : "))
                        meal.updateMealPrice(chefId, mealNewPrice)
                    except:
                        print("Enter valid data")
                elif meal_choice == 5:
                    try:
                        mealId = int(input("Please enter meal id: "))
                        mealNewPrice = float(
                            input("Please Insert New Price for the Meal : "))
                        meal.updateMealPrice(mealId, mealNewPrice)
                    except:
                        print("Enter valid data")
                elif meal_choice == 6:
                    meal.fetchAllMeals()

            except:
                print("invalid input try entering valid one")

        elif choice == 5:
            print(
                "You are now in order management dashboard\nwhat do you want to do?")
            print("1. make new order to restaurant")
            print("2. show all orders")
            orderChoice = int(input("enter choice : "))
            orders = Orders()
            if orderChoice == 1:
                customerId = int(input("enter customer id: "))
                mealId = int(input("enter meal id: "))
                orders.makeOrder(customerId, mealId)
            elif orderChoice == 2:
                orders.fetchAllOrders()

        elif choice == 6:
            break
        else:
            print("invalid input , please choose valid choice")


if __name__ == "__main__":
    main()
