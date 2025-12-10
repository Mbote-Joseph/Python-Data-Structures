# for loops - execute a block of code a fixed number of times.
# You can iterate over a range, string, sequence etc

books = ["Think Big", "Gifted hands"]

for i in range(0, len(books)):
    print (f"Book {i+1} is {books[i]}")
    
scores = [24, 56, 78, 89, 46, 87, 23, 90,100, 98]

total_scores = 0
for s in range(0, len(scores)):
    total_scores += scores[s]
    average = total_scores/len(scores)

print(f"The total scores is {total_scores} and the average score of {len(scores)} students is {average}")