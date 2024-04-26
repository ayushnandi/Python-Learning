# class Car:
#     def __init__(self, door , color):
#         self.door = door
#         self.color = color 




# car1 = Car(4,"red")
# car2 = Car(2,"blue")
# print(car1.door)
# print(car2.color)





# class Car:
#     def __init__(self , modal , color):
#         self.color = color
#         self.modal = modal 
#     def DisplayCar(self):
#         print(self.modal)
#         print(self.color)
# car1 = Car("haundy", "black")
# car1.DisplayCar()
# car2 = Car("tesla", "galaxyblack")
# car2.DisplayCar()
# car3 = Car("tata mahindra", "white")







class Car:
    def __init__(self , modal , color):
        self.color = color
        self.modal = modal 
    def Display(self):
        print(self.modal)
        print(self.color)

    # @staticmethod
    def Details():
        print("xxxxxxxxxxx sex")



car1 = Car("haundy", "black")
car1.Display()
car2 = Car("tesla", "galaxyblack")
car2.Display()
car3 = Car("tata mahindra", "white")
Car.Details()
