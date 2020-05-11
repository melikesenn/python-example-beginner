class Person():
    def __init__(self,name):
        print("insan sınıfı oluştu")
        self.name = name


class student(Person):
    def __init__(self):
        #tanımlama yapmazsak sudent initi personu ezer bunun için yazdık ezsin ama çalışsın
        Person.__init__(self) #personun initide çalıştı
        print('student oluştu')

p1 = Person("meli")
s2 = student()
