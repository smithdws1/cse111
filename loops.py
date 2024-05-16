def main():
    colors = ['red', 'orange', 'yellow', 'green', 'blue']
    for color in colors:
        print(color)

    for i in range(len(colors)):
            color = colors[i]
            print(color)
    print()

    for i in range(10):
        print(i)
    print()

    for i in range(5, 10):
        print(i)
    print()

    for i in range(0, 10, 2):
        print(i)

    for i in range(100, 69, -3):
        print(i)
    print()
    
    sum = 0

    for i in range(10):
         number = float(input("Please enter a number: "))
         if number == 0:
            break
         sum += number

    print(f"sum: {sum}")

    
if __name__ == "__main__":
    main()

