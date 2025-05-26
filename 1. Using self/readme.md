Student Class Explanation
Introduction:
Yeh Python ka simple code hai jo students ka data store karta hai (naam, marks, aur course) aur display karne ka kaam karta hai. Is code mein do functions hain:

__init__() — Data initialize karne ke liye.

display() — Data ko print karne ke liye.

Class Student:
Student ek class hai jisme student ke naam, marks, aur course ko store karte hain.

__init__() Function:
Yeh ek special method hai jo jab bhi hum class ka object banate hain, automatically call hota hai.

python
Copy
Edit
def __init__(self, name, marks, course):
    self.name = name
    self.marks = marks
    self.course = course
__init__() ka kaam:
__init__() function ke through, jab hum Student ka object banate hain, yeh automatically call hota hai aur us object ka data initialize kar leta hai.

self: Yeh keyword us object ko represent karta hai jisme data store ho raha hai. Jab tum student1 ya student2 banate ho, self us object ko represent karega.

name, marks, aur course parameters student ke data ko represent karte hain.

Data initialize ka matlab hai:

self.name: Yeh object ka name store karega.

self.marks: Yeh object ka marks store karega.

self.course: Yeh object ka course store karega.

display() Function:
Yeh ek normal method hai jisko hum manually call karte hain.

python
Copy
Edit
def display(self):
    print("Student Name:", self.name)
    print("Student Marks:", self.marks)
    print("Student Course:", self.course)
display() ka kaam:
display() function ko call karte hi, yeh student ke naam, marks, aur course ko print kar dega.

self.name, self.marks, aur self.course woh values hain jo humne __init__() function mein store ki thi.

Object Creation:
python
Copy
Edit
student1 = Student("Ali", 90, "Mathematics")
student2 = Student("Ramesha", 22, "Computer Science")
Object student1 aur student2 ka creation:
Jab hum student1 = Student("Ali", 90, "Mathematics") likhte hain, to yeh Student class ka object banata hai aur __init__() function ko call karta hai. Isme "Ali", 90, aur "Mathematics" parameters pass hotay hain.

"Ali" ko self.name mein store kar liya jata hai.

90 ko self.marks mein store kiya jata hai.

"Mathematics" ko self.course mein store kiya jata hai.

student2 ke liye bhi waise hi process hota hai, bas Ramesha, 22, aur Computer Science ke data ke saath.

Calling the display() function:
python
Copy
Edit
student1.display()
student2.display()
Jab hum student1.display() call karte hain, to display() function execute hota hai, jo student1 ke naam, marks, aur course ko print karta hai.

Output hoga:

yaml
Copy
Edit
Student Name: Ali
Student Marks: 90
Student Course: Mathematics
Jab hum student2.display() call karte hain, to display() function student2 ke naam, marks, aur course ko print karega.

Output hoga:

yaml
Copy
Edit
Student Name: Ramesha
Student Marks: 22
Student Course: Computer Science
Detailed Flow:
student1 = Student("Ali", 90, "Mathematics")

Student class ka ek new object student1 banta hai.

__init__() method call hota hai aur student1 ke liye data initialize hota hai.

name = "Ali", marks = 90, aur course = "Mathematics" store hotay hain.

student2 = Student("Ramesha", 22, "Computer Science")

Dusra object student2 banta hai.

name = "Ramesha", marks = 22, aur course = "Computer Science" store hotay hain.

student1.display()

student1 ka data print hota hai: Ali, 90, aur Mathematics.

student2.display()

student2 ka data print hota hai: Ramesha, 22, aur Computer Science.

Conclusion:
__init__() ka kaam hai object banate waqt uska data initialize karna. Yeh ek automatic function hai.

display() ka kaam hai object ka data display karna. Yeh manually call kiya jata hai jab tumhe data print karwana ho.

Yeh dono functions ek saath kaam karte hain: __init__() data store karta hai aur display() us data ko show karta hai.