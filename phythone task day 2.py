name = input("enter your name: ")
age = input("emter your age: ")
sub1 = input("enter your favourate subject 1: ")
sub2 = input("emter your favourate subject 2: ")
sub3 = input("enter your favourate subject 3: ")
favorite_subject = [sub1 , sub2 , sub3]
rollno =input("enter your roll no: ") 
branch = input("enter your branch: ")
mark1 = input("enter maeks of sub 1; ")
mark2 = input("enter maeks of sub 2: ")
mark3 = input("enter marks of sub 3: ")
Marks = (mark1 , mark2 , mark3)
skill1 = input("enter your skill 1:  ")
skill2 = input("enter yoour skill 2: ")
skill3 = input("enter your skill 3: ")
Tech_Skills = {skill1 , skill2 , skill3}

print(" Name: ", name)
print("Age: ", age)
print(f"Favourite Subjects: {favorite_subject}")
print("Student info: ", rollno, ",", branch)
print(F"Marks: {Marks}")
print(f"Technical Skills: {Tech_Skills}")



