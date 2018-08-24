# Jacob Meadows
# Computer Programming, 4th Period
# August 22nd, 2018


class Person:
    def __init__(self, name, age, city, phone_num):
        self.name = name
        self.age = age
        self.city = city
        self.phone_num = phone_num

    def __str__(self):
        return f"{self.name} is {self.age} years old, lives in {self.city}, and their phone number is {self.phone_num}"


def main():
    name = input("Name: ")
    age = input("Age: ")
    city = input("City: ")
    phone_num = get_phone_num()
    print(Person(name, age, city, phone_num))


def get_phone_num():
    try:
        phone_num = int(input("Phone Number: "))
    except ValueError:
        print("Invalid phone number; please input numbers only.")
        phone_num = get_phone_num()
    return phone_num


main()
