# indexing - accessing elements of a sequence using [] (indexing operator) [start : end : step]

credit_card_number = "5678-1234-9012-3456"

card_type = credit_card_number[0:4]

if card_type == "1234":
    print("The Card is VISA")
    print(f"{credit_card_number[0:4]} ... {credit_card_number[21:26]}")
elif card_type == "5678":
    print("The card is Master Card")
    print(f"{credit_card_number[0:4]} ... {credit_card_number[21:26]}")
elif card_type == "9123":
    print("The card is AMEX")
    print(f"{credit_card_number[0:4]} ... {credit_card_number[21:26]}")
else:
    print(f"The card number {credit_card_number} is not valid")
    print(f"{credit_card_number[0:4]} ... {credit_card_number[21:26]}")
