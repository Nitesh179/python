class Student:
    def __init__(this,name,age,city):
        this.name=name
        this.age=age
        this.city=city

    def talk(this):
        return (f"student name : {this.name}\nStudent age : {this.age}\nStudent city : {this.city}\n")


s1=Student("Nitesh",21,"indore")
print(s1.talk())

this=10
print(this)