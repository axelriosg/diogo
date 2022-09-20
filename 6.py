#Write a python program that reads a number n of values specified by the user and tells the end of the program how many values read are even.

def main():
    n = int(input("Enter the number of values: "))
    even = 0
    for i in range(n):
        value = int(input("Enter a value: "))
        if value % 2 == 0:
            even += 1
    print("Number of even values: ", even)



if __name__ == "__main__":
    main()

