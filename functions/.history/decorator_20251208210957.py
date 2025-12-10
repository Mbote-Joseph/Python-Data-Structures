def upper_case(n):
    def inner():
        return n().upper()
    return inner

@upper_case
def greetings():
    return f"Hello"

print(greetings())