for i in range(1, 4):
    for j in range(1, 4-i):
        print(" ", end="")
    for k in range(1, (2*i-1)+1):
        print("*", end="")
    print("\n")