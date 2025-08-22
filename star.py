rows = 5  

for i in range(1, rows + 1):  
    for j in range(rows - i):  # Print spaces
        print(" ", end=" ")  
    for k in range(2 * i - 1):  
        if k == 0 or k == 2 * i - 2 or i == rows:  # Print stars at borders
            print("*", end=" ")  
        else:  
            print(" ", end=" ")  # Print spaces inside
    print()
