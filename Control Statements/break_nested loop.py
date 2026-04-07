#break in nested loop
for i in range(3):
    for j in range(3):
        if j == 1:
            break        # exits inner loop only
        print(i, j)
