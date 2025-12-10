def upper_case(n):
    return n().upper()

@upper_case
def greetings(a):
    return f"Hello {a}"

print(greetings("Joseph"))