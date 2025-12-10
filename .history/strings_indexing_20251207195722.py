# indexing - accessing elements of a sequence using [] (indexing operator) [start : end : step]

credit_card_number = "1234-5678-9012-3456"

card_type = credit_card_number[0:4]

if card_type == "5678":
    print("The Card is VISA")
elif card_type == "5678":
    print("The card is Master Card")
elif card_type == "9123":
    print("The card is AMEX")
else:
    print(f"The card number {credit_card_number} is not valid")
