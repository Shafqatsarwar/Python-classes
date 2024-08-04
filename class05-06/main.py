def className():
    print("Learning Python")

    def get_user_name(age: int):
        my_name: str = input("Enter your name: ")
        print("Hello", my_name)
        return my_name

    new_user_name: str = get_user_name(21)
    print(f"Hello, {new_user_name}")

className()
