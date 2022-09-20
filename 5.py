#a python function that reads a 20 integers from the user and prints a sum of all of them divided by 20.

def main():
    sum = 0
    for i in range(20):
        sum += int(input("Enter an integer: "))
    print("The sum of the 20 integers is", sum)
    print("The average of the 20 integers is", sum/20)



if __name__ == "__main__":
    main()
