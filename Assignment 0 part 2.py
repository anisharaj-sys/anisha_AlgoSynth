count = 0
while count < 5:
    a = input(f"Enter number {count + 1}:")
    if int(a) % 2 ==0:
        print("Even")
    else:
        print("Odd")

    count += 1