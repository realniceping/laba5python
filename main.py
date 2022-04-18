from classes import *  
from main_menu import Mani_menu

def Show_All_Object_With_Id(persons: Person):
    if len(persons) == 0:
        print("For the first time create some one object!")
    else:
        counter: int = 0
        for person in persons:
            counter += 1
            print(str(counter) + "." + person.__str__())

def Show_All_Object_Whit_No_Id(persons: Person):
    if len(persons) == 0:
        print("For the  first tine create some one object!")
    else:
        for person in persons:
            print(person.__str__())

def Show_Some_Obeject(persons: Person):
    lenght = len(persons)
    position: int 
    if lenght == 0:
        print("For first time create some one object!")
    else:
        print(f"Select your object by number (from {1} to {lenght})")
        position = int(input(">> "))
        if (position in range(1, lenght + 1)):
            print(persons[position - 1].__str__())
        else:
            print("Unknown id")

def Add_Object(persons: Person):
    submenu: int 
    submenu = int(input("Which type of Person you want to add?(1. Person/2. Student/ 3. Teacher)"))
    if submenu == 1:
        age: int 
        age = int(input("How old you person?>> "))
        persons.append(Person(age))
    elif submenu == 2:
        flag: bool = False
        age: int
        id: int 
        avg_mark: float 
        while flag != True:
             
            age = int(input("How old your student?>> "))
            
            id = int(input("Set ID of your student>> "))
            
            avg_mark = float(input("Set averange point of your student>> "))
            if age < 7 or age > 100:
                print("impossible age, try again")
                continue

            if avg_mark < 2 or avg_mark > 5:
                print("Impossible average mark, try again!")
                continue

            for person in persons:
                if type(person) is Student:
                    if id == Student.id:
                        print("Some student have same id, try again")
                        continue
            persons.append(Student(age, id, avg_mark))
            flag = True

    

    elif submenu == 3:
        age: int 
        working_stage: int
        flag:bool = False
        while flag != True:
            age = int(input("How old your teacher?>> "))
            working_stage = int(input("How much time your teacher working?>> "))
            if age < 18 or age > 100:
                print("Impossinble age! Try again")
                continue
            elif working_stage > 80:
                print("Impossible working stage! Try again")
                continue
            else:
                flag = True

        persons.append(Teacher(age, working_stage))
        
def Edit_Object(persons: Person):
    
    Show_All_Object_With_Id(persons)
    submenu: int
    flag: bool = False
    age: int  
    id: int 
    counter: int = 0
    avg_mark: int
    working_stage: int 
    submenu = int(input("Select object which you want to edit>> ")) # dont forget to edit it 
    while flag != True:
        if type(persons[submenu - 1]) is Person:
            age = int(input("How many age you want to set to your person?> "))
            if age < 1 or age > 100:
                print("Impossible age! Try again")
                continue
            else:
                person[submenu - 1] = Person(age)
                flag = True

        elif type(persons[submenu - 1]) is Student:
            age = int(input("How many age you want to set to your Student?> "))
            
            if age < 1 or age > 100:
                print("Impossible age! Try again")
                continue

            id = int(input("Set new ID to you student>> "))

            for person in persons:
                if person is Student:
                    if id == Student.id and counter != submenu:
                        print("Some student have same id, try again")
                        counter = 0
                        continue
            avg_mark = float(input("Set averang mark to your student>> "))

            if avg_mark < 2 or avg_mark > 5:
                print("Impossible average mark! Try again")
                continue

            persons[submenu - 1] = Student(age, id, avg_mark)
            flag = True

        elif type(persons[submenu - 1]) is Teacher:
            age = int(input("How many age you want to set to your Student?> "))

            if age < 1 or age > 100:
                print("Impossible age! Try again")
                continue

            working_stage = int(input("How many years your teacher working?>> "))

            if working_stage < 0 or working_stage > 80:
                print("Impossible working stage! Try again")
                continue

            persons[submenu - 1] = Teacher(age, working_stage)
            flag = True

def Shearch(persons):
    submenu: int 
    value: str
    print("What fact you remember about your Person?")
    print("1.age")
    print("2.working stage")
    print("3.StudentID")
    print("4.average point")
    submenu = int(input(">> "))
    value = str(input("Set value>> "))
    for person in persons:
        if submenu == 1:
            if person.age == int(value):
                print(person.__str__())
        elif submenu == 2:
            if type(person) is Teacher:
                if person.working_stage == int(value):
                    print(person.__str__()) 
        elif submenu == 3:
            if type(person) is Student:
                if person.id == int(value):
                    print(person.__str__())

        elif submenu == 4:
            if type(person) is Student:
                if person.avg_mark == float(value):
                    print(person.__str__()) 

        else:
            print("Invalid number")

if __name__ == "__main__":
    print("welcome to my programm")
    print("this program can create object of classes(Student <--- Person ---> Teacher)")
    persons: Person = []
    persons.append(Person(12))
    persons.append(Teacher(50, 25))
    persons.append(Student(18, 202020, 4.5))

    print(type(persons[0]))
    print(type(persons[1]))
    print(type(persons[2]))

    for person in persons:
        print(person.__str__())


    menu: int = 9

    while menu != 0:
        Mani_menu()
        menu = int(input("What you want to do?>>  "))
        
        if menu == 1:
            Add_Object(persons)

        elif menu == 2:
            Edit_Object(persons)

        elif menu == 3:
            Show_Some_Obeject(persons)

        elif menu == 4:
            Shearch(persons)
            pass
    
        elif menu == 5:
            Show_All_Object_Whit_No_Id(persons)
        
        elif menu == 0:
            print("Thx for using my programm. bye-bye")