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