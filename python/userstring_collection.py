from collections import UserString

#Custom string wrapper.
class MyString(UserString):
    def upper(self):
        return self.data.upper() + "!"

s = MyString("hello")
print(s.upper())  # HELLO!
