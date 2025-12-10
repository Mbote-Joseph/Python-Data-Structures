# for loops - execute a block of code a fixed number of times.
# You can iterate over a range, string, sequence etc

books = ["Think Big", "Gifted hands"]

for i in range(1, int(len(books))+1):
    print (f"Book {i} is {books[i]}")