
class Person:

    __age: int 

    def __init__(self, age: int):
        self.__age = age
        print("obj succesfully created")

    def __del__(self):
        print("object successfuly deleted")

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age: int):
        if age in range(1, 100):
            self.__age = age
        else:
            print("invalid age")

    def __str__(self):
        return "This is a person was " + str(self.age) + " years old"

class Student(Person):

    __id: int 
    __avg_mark: float

    def __init__(self, age: int,  id: int, avg_mark: float):
        super().__init__(age)
        self.__id = id
        self.__avg_mark = avg_mark

    def __del__(self):
        print("object successfuly deleted")

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id: int):
        if id in range(100000, 999999):
            self.__id = id
        else:
            print("invalid identificator")

    @property
    def avg_mark(self):
        return self.__avg_mark

    @avg_mark.setter
    def avg_mark(self, avg_mark):
        if avg_mark in range(2, 5):
            self.__avg_mark = avg_mark

    def __str__(self):
        return super().__str__() + " this person is a Student, with average point = " + str(self.__avg_mark) + " and id: " + str(self.__id)

class Teacher(Person):

    __working_stage: int 

    def __init__(self, age: int, working_stage: int):
        super().__init__(age)
        self.__working_stage = working_stage

    def __del__(self):
        print("object successfuly deleted")

    @property
    def working_stage(self):
        return self.__working_stage

    @working_stage.setter
    def working_stage(self, working_stage: int):
        if working_stage in range(1, 70):
            self.__working_stage = working_stage
        else:
            print("invalid working stage")
    
    def __str__(self):
        return super().__str__() + " this person is Teacher. They working " + str(self.working_stage) + " years"

    