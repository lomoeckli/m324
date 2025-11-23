class House:
    def __init__(self):
        print("New house was builded")
    
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