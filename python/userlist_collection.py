from collections import UserList

class MyList(UserList):
    def append(self, item):
        print(f"Adding {item}")
        super().append(item)

ml = MyList([1, 2])
ml.append(3)  # Adding 3
