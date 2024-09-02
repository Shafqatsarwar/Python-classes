class PIAIC:
    # Attribute
    course: str = "Gen Ai"
    
    # Constructor
    def __init__(self, course="Gen Ai"):
        self.course = course
    
    # Method to display course
    def display(self) -> None:
        print("Hello PIAIC World of", self.course)
    
    # Method to set course name
    def setCourseName(self, course):
        self.course = course
    
    # Method to get course name
    def getCourseName(self):
        return self.course

# Initialize the class
student = PIAIC()
print(student.course)

student1 = PIAIC()
print(student1.course)

student1.setCourseName("cloud computing")
print(student1.getCourseName())

student2 = PIAIC()
print (student2.course)


# class Car():
#     color : str = "Red"
#     model : str = "Honda"
#     #constructor function
#     def __init__(self, color, model):
#         self.color = color
#         self.model = model
#     def speed(self):
#         print ("increase car speed at 5 km/h")
    
#     def displayCarcolor(self):
#         print ("Car color is ", self.color)

#     def displayCarmodal(self):
#         print ("Car model is ", self.model)

# car : Car = Car ("Red", "Honda")
# print ("Car.color")
# car.displayCarcolor()
# car.displayCarmodal()
# car.speed()






# class PIAIC:
#     # Attribute
#     course: str = "Gen Ai"
    
#     # Method
#     def display(self) -> None:
#         print("Hello PIAIC World of", self.course)

# # Initialize the class
# student = PIAIC()

# # Call the method
# student.display()

# # Call method
# student.display()   