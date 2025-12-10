# nested loop - A loop within another loop (outer, inner)
# outer loop:
#   inner loop:

rows = int(input("Enter the number of rows: "))
columns = int(input("Enter the number of columns: "))
symbol = input("Enter a symbol to use:")

for i in range(rows):
    for j in range(columns):
        print(symbol, end=" ")
    print()