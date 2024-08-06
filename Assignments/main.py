def className():
    print("Learning Python")

    def get_user_name(age: str):
        my_name: str = input("Enter your name: ")
        age = input("Enter your age!")
        print("Hello", my_name)
        return my_name
    new_user_name: str = get_user_name()
    print(f"Hello, {new_user_name}")
className()
