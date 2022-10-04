# add new student 
# add marks 
# get avg


from typing_extensions import Self


class student:
    def __init__(self,name):
        print(f"Welcome {name}")

s1 = student("islam")
print(f"Welcome {Self.name}")