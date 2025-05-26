🚨 Custom Exception kyun banate hain?
Custom exception specific errors ko clearly represent karte hain — jaise yahan InvalidAgeError se pata chal raha hai ke age-related issue hua hai.

🛠 check_age(age) function:
Agar age 18 se choti ho to InvalidAgeError raise karta hai.

Agar age valid ho to message print karta hai: "Access granted."

🔁 try...except block:
Function call ko protect karta hai.

Agar exception raise ho to gracefully handle karta hai: "Custom Exception Caught: ..."

🧪 Sample Output:
yaml
Copy
Edit
Enter your age: 16
Custom Exception Caught: Invalid age: 16. You must be 18 or older.
