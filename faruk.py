
# 11111111111111111111111111111111111111111111111111
# class Rectangle:
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height

#     def area(self):
#         return self.width * self.height

#     def perimeter(self):
#         return (self.width + self.height) * 2


# rectangle = Rectangle(4, 5)

# area = rectangle.area()
# perimeter = rectangle.perimeter()
# print(f"The area of the rectangle is {area}, and the perimeter is {perimeter}.")



# 22222222222222222222222222222222222222222222222222222
# class School:
#     def __init__(self, name, foundation_year):
#         self.name = name
#         self.foundation_year = foundation_year
#         self.students = []
#         self.teachers = []

#     def add_new_student(self, student_name, student_class):
#         self.students.append((student_name, student_class))
#         print(f"Student {student_name} added to the {student_class} class.")

#     def add_new_teacher(self, teacher_name, branch):
#         self.teachers.append((teacher_name, branch))
#         print(f"Teacher {teacher_name} added to the {branch} department.")

#     def view_student_list(self):
#         print("The list of the students:")
#         for student_name, student_class in self.students:
#             print(f"Name : {student_name} , Class : {student_class}")

#     def view_teacher_list(self):
#         print("The list of the teachers:")
#         for teacher_name, branch in self.teachers:
#             print(f"Name : {teacher_name} , Branch : {branch}")


# school = School("Amsterdam High School", 1984)
# school.add_new_student("Jan de Fries", "9A")
# school.add_new_teacher("Noah Poppel", "Chemistry")
# school.view_student_list()
# school.view_teacher_list()


# 333333333333333333333333333333333333333333333333333333333
# class Shape:
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height


# class Rectangle(Shape):
#     def calculate_area(self):
#         return self.width * self.height


# class Square(Shape): 
#     def __init__(self, side):
#         super().__init__(side, side)

#     def calculate_area(self):
#         return self.width * self.height


# rectangle = Rectangle(3, 4)
# square = Square(6)

# print(f"Rectangle area: {rectangle.calculate_area()}")
# print(f"Square area: {square.calculate_area()}")




# 4444444444444444444444444444444444444444444444444444444444
# class Vehicle:
#     def __init__(self, make, model, year):
#         self.make = make
#         self.model = model
#         self.year = year

#     def display_info(self):
#         print("Vehicle Information:")
#         print(f"Make: {self.make}")
#         print(f"Model: {self.model}")
#         print(f"Year: {self.year}")


# class OffRoadVehicle(Vehicle):
#     def __init__(self, make, model, year, four_wheel_drive):
#         super().__init__(make, model, year)
#         self.four_wheel_drive = four_wheel_drive

#     def display_info(self):
#         super().display_info()
#         print(f"Four Wheel Drive: {'Yes' if self.four_wheel_drive else 'No'}")


# class SportCar(Vehicle):
#     def __init__(self, make, model, year, max_speed):
#         super().__init__(make, model, year)
#         self.max_speed = max_speed

#     def display_info(self):
#         super().display_info()
#         print(f"Max Speed: {self.max_speed} km/h")


# suv = OffRoadVehicle("Land Rover", "Discovery", 2018, True)
# sports = SportCar("Audi", "TT", 2016, 250)

# suv.display_info()
# sports.display_info()




# 5555555555555555555555555555555555555555555555555555
class Shape:
    def __init__(self, width, height):
        self.width = width
        self.height = height


class Rectangle(Shape):
    def calculate_area(self):
        return self.width * self.height


class Square(Shape): 
    def __init__(self, side):
        super().__init__(side, side)

    def calculate_area(self):
        return self.width * self.height


rectangle = Rectangle(3, 4)
square = Square(6)

print(f"Rectangle area: {rectangle.calculate_area()}")
print(f"Square area: {square.calculate_area()}")
