from collections import UserString

#custom string wrapper
class MyString(UserString):
    def upper(self):
        return self.data.upper() + "!"

s = MyString("hello")
print(s.upper())  # HELLO!
