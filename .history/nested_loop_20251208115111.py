# nested loop - A loop within another loop (outer, inner)
# outer loop:
#   inner loop:

rows = int(input("Enter the number of rows: "))

for i in range (0, rows):
    print(f"{i} "* i+1)