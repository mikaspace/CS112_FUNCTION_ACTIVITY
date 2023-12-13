print("CS112 - FUNCTION ACTIVITY")
print("Myka Angelie Baclayo")
print('')
#function for computation
def nums(num1, num2, num3):
    result = 0
    if num1 == num2 == num3:
        result = num1 * num2 * num3
    elif num1 == num2 != num3:
        result = num1 * num2 + num3
    elif num1 != num2 == num3:
        result = num1 + num2 * num3
    else:
        num1 != num2 != num3
        result = num1 + num2 + num3
    return result

def prompt():
    while True:
        num1 = eval(input("Enter a number: "))
        num2 = eval(input("Enter a number: "))
        num3 = eval(input("Enter a number: "))
        print(nums(num1, num2, num3))

prompt()
