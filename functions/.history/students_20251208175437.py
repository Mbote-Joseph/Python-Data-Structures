def print_info(**info):
    for key, value in info.items():
        print(f"{key}:{value}")
        
print_info(name="Joseph Mbote", age=28, course = "BSc. Computer Science")