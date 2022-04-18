class Person:

    def __init__(self, age: int):
        self.__age = age

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


class Student(Person):

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


class Teacher(Person):

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


if __name__ == "__main__":

