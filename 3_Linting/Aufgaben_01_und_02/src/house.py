class House:
    def __init__(self):
        print("New house was builded")
    
    def login(self):
        username = "admin"
        password = "admin"

        input_username = input("Enter username: ")
        input_password = input("Enter password: ")

        if input_username == username and input_password == password:
            print("Login successful")
            return True
        else:
            print("Login failed")
            return False

    def get_name(self):
        print(self.name)
        return self.name

    def set_name(self, name):
        if(type(name) is not str):
            raise TypeError("name must be a string")

        self.name = name

    def get_price(self):
        price = 50
        text = f"{price} CHF"
        print(text)