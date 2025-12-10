def upper_case(n):
    def inner():
        return n().upper()
    return inner

@upper_case
def greetings(a):
    return f"Hello {a}"

print(greetings("Joseph"))