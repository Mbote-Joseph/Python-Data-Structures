# Dictionary - a collection of {key:value} pairs ordered and changeable. No duplicates

capitals = {"USA": "Washington D.C", "Kenya":"Nairobi", "Uganda":"Kampala", "Rwanda":"Kigali"}

print(len(capitals))

print(capitals.get("USA"))

for key in capitals.keys():
    print(f"The capital city of {key} is : {capitals.get(key)}")