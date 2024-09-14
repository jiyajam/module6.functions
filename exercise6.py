###############1
import random
def roll():
        return random.randint(1,6)
def main():
    result = 0
    while result != 6:
        result = roll()
        print(f"rolled {result}")
        if result == 6:
            print ("yay! you finally rolled a 6")

main()

###############2
import random
def roll(sides):
        return random.randint(1,sides)

def main():
    sides = int(input("Enter the number of sides on  the dice: "))
    result = 0
    while result != sides:
        result = roll(sides)
        print(f"rolled and got the side {result}")
        if result == sides:
            print("yay you finally got " , sides)
main()

##############3
def litres(gallons):
    return gallons * 3.79

def main():
    while True:
        gallons = float(input("enter the Gallons: "))
        if gallons < 0:
            print(f"{gallons} is less than zero")
            break
        converted = litres(gallons)
        print (f"{gallons} gallons is equal to  {converted:.2f} litres")
        break
main()





#################4
def sum(list):
    total = 0
    for x in list:
        total += x
    return total
list = [1,2,3,4,5]
result = sum(list)
print(result)


##############5
def evenlist(numbers):
    evenlist =[]
    for x in numbers:
        if x % 2 ==0:
            evenlist.append(x)
    return evenlist
numbers = [1,2,3,4,5,6,9,12,23,54]
result = evenlist(numbers)
print(f"the original list is {numbers} and the even number list is {result}")

##############6
import math
def pizza(diameter,price):
    radius_meter = (diameter/2)/ 100
    area = math.pi*radius_meter**2
    price_square_meter = price/area
    return price_square_meter

user_input_diameter1 = float(input("Enter the diameter of the pizza 1: "))
user_input_price1 = float(input("Enter the price of the pizza 1: "))
user_input_diameter2 = float(input("Enter the diameter of the pizza 2: "))
user_input_price2 = float(input("Enter the price of the pizza 2: "))



if pizza(user_input_diameter1,user_input_price1) < pizza(user_input_diameter2,user_input_price2):
    print("the first pizza is a better deal")
elif  pizza(user_input_diameter1,user_input_price1) > pizza(user_input_diameter2,user_input_price2):
    print("the second pizza is a better deal")
else :
    print("both pizza are equal")