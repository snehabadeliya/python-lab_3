class class1:
    def M(self):
        print("In class1")

class class2(class1):
    pass

class class3(class1):
    def M(self):
        print("In class3")

class class4(class2, class3):
    pass

obg = class4()
obg.M()
