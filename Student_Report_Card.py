class Student:
    def __init__(self,name,marks):
        self.name=name 
        self.marks=marks
        # self.average=0
        # self.sum=0
        

    def get_average(self):
        
        # self.sum+=self.marks[subject]
        # self.average=self.sum/len(self.marks)
        # return self.average
        total=sum(self.marks.values())
        return total/len(self.marks)


       
    def get_grade(self):

        average=self.get_average()

        if average>=90:
            self.grade="A"
        elif average>=80:
            self.grade="B"
        elif average>=70:
            self.grade="C"
        elif average>=60:
            self.grade="D"
        elif average>=50:
            self.grade="E"
        else:
            self.grade="F"
        return self.grade
        


s1=Student("Hannah",{"math":50,"eng":23,"hindi":56})
s2=Student("Garret",{"math":67,"eng":87,"hindi":34})
s3=Student("Logan",{"math":89,"eng":98,"hindi":93})


print("Testing Error Handling : \n")
s4=Student("Dean",{"math":50,"eng":"good","hindi":56})
s5=Student("Allie",{})

for student in [s1,s2,s3,s4,s5]:
    try:
            print(f"Result for {student.name}:\n")
            print(student.marks)
            print(student.get_average())
            print(student.get_grade())
            print("-----------------------")
    except TypeError as e:
            print(f"Invalid data: {e}")
    except ValueError as e:
            print(f"Error: {e}")
    except ZeroDivisionError:
        print("Error: marks cannot be empty")
        
     



  