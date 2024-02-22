def say_hello(user_name):
    return f"Hi, there {user_name}!"

if __name__ == "__main__":
    user_name = input("What is your name? ")
    response = say_hello(user_name)
    print(response)