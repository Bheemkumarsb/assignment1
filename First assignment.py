Q1 : Explain the key features of Python that make it a popular choice for programming
ANS : Python was a general purpose language used at any junction of the software, it has many pro's over the other programming languages, that are:
     ease of use, we can access lot no of libraries(i,e over 137000 codes), Data industry mostly uses the python, python can be connected to multiple tools, it         has a high active community and directly executes the code instead of translating.
         
Q2 : Describe the role of predefined keywords in Python and provide examples of how they are used in a program
ANS : Predefined keywords in Python are reserved words with specific meanings and cannot be used as variable names or function names.Used for control flow, loops, and decision-making.

Q3 : Compare and contrast mutable and immutable objects in Python with examples
ANS : i) Mutable objects can be changed after they are created. This means you can modify their content without changing their identity. #objects / containers are          whose value or state can be changed after they are created are called as #mutable objects or containers.
      Ex : Lists, dictionaries, sets, and custom classes.
           #list is a type of object that support item assignment
          Use Cases: Useful when you need to modify the size or content of the object frequently.
    We can change the elements of lits via +ve indeces or -ve indeces i,e a = ["Kumar"] here, a[0] = K, a[1] = u or a[-1] = r, a[-2] = a.
    Ex code : list_cont = [1, 2, 3+4j, "Kumar", True, 7.8]
        list_cont
        [1, 2, (3+4j), 'Kumar', True, 7.8]
    list_cont[-3] = "Anil"
[1, 2, (3+4j), 'Anil', True, 7.8] 

   ii)Immutable objects or containers >> objects / containers are whose value or state can not be changed after they are created are called as 
      #immutable objects or containers.
    Ex :Tuple, Strings are type of objects that doesn't support item assignment.
        Ex code : Str1 = "Bengluru"
                  Str1[2] = K
                print(Str1)
 We are getting error like "NameError: name 'K' is not defined"

Q4: Discuss the different types of operators in Python and provide examples of how they are used.

Ans : In Python programming, Operators in general are used to perform operations on values and variables. These are standard symbols used for logical and              arithmetic operations to do more computations and data manipulation.

     i} Arithmatic operators : These are used to perform are used to perform basic mathematical operations like addition, subtraction, multiplication, and division.
         lets define a =5 and b = 2 for all following cases: a and b are two variables then a + b(Addoition), a - b(Subtraction),a*b(Multiplication),                     a/b(Division), a%b(Modulus operator), a**b(exponential operator), a//b(floor operator).
   Ex: (5+2=7), (5-2=3), (5*3=15),(5/2=2.5), (5%2=1),(5**2=25),(5//2=2)

    ii} Comparison Operators in Python >> In Python, comparison operators are used to compare the values of two operands (elements being compared).
                                Ex: (5 == 5: True - Equality operator), (5!=2 : True - inequalty opearator), (5>2: True - Greater than operator), (5<2 : False -                                 Lesser than operator), (5>=2: True - Greater than or equal operator) and (5<=2 : False - Lesser than or equal operator).

    iii} Logical operators: These are used in conditional statements (either True or False). They perform Logical AND, Logical OR, and Logical NOT operations.
         Logical AND(&) >>a = 10(1010) and b =10(1010)then 10&10 results in true o/p is 10(1010) i,e (1010) * (1010)- Returns True if both the operands are true
         Logical OR (!) >> a = 35 (100011) OR b = 42(101010) then 35!42 results in 43(101011) -Returns True if either of the operands is true.
         Logical Not (Returns True if the operand is false) - (!a) = 10 then not (a) then results is False.

    iv} Bitwise Operators -Bitwise operators are used to perform bitwise calculations on integers.The integers are first converted into binary and then                                     operations are performed on each bit or corresponding pair of bits, hence the name bitwise operators. The result is then returned in                             decimal format.
    a)Bitwise AND operator(a^b) >> 5^3 results in 6
    b)Bitwise OR operator (a|b) >> 5|3 results in 7
    c)Bitwise XOR Operator (a^b) >> 5^3 results in 6
    d) Bitwise NOT Operator (~a) >> ~5 results in -6
    e)Python Bitwise Right Shift(a>>) 5>>2 results in 1
    f} Python Bitwise Left Shift(a<<) 5<<2 results in 20

  V} Assignment Operators in Python - These are used to assign a value to an variable.
   Ex : a = 5, b = 3+4j

  Vi} Membership operators >> Python membership operators test for the membership of an object in a sequence, such as strings, lists, or tuples. Python offers                                 two membership operators to check or validate the membership of a value.
They are as follows: a) in Operator - Returns True if the value exists in a sequence, else returns False 
               Ex:if c = "Bheemkumar" 
                          "B" in c results>> True 
                    d = "Kumar"
                   "Kr" in d results >> false 
                b) not in Operator - Returns False if the value exists in a sequence, else returns True
                         Ex: if e = "Bengaluru"
                                "B"in e results >> False
                            if d = "Square"
                          "B" in c results >> True
   Vii} Identity Operators - Operators are used to compare the objects if both the objects are actually of the same data type and share the same memory                                       location. There are different identity operators such as:
                      ** is Operator - Returns True if both objects refers to same memory location, else returns False i,e obj1 is obj2.
                           Ex : a = 5  b = 7 Then a is b results False
                      ** is not Operator - Returns False if both object refers to same memory location, else returns True i,e obj1 is not obj2
                         Ex : a = 8 b = 7 then a is not b results True and a is b results False


Q5:  Explain the concept of type casting in Python with examples?
 Ans : Type cating is the process of changing the data types o value or variable.
      Type catsing used because while executing compuatation using operators there can be mismatch between the data.There are two types of typecatings are there:
       i> Implicit typecating : let num: number = 123;  // Explicit type annotation
       ii> Explicit typecating: let num = 123;  // Type is implicitly inferred as `number`

     Ex: a = "7", here a is a string if we execute type(int(a)) it will results 7 i,e an integer.
        i> Implicit typecating - In this method, Python converts the datatype into another datatype automatically. Users don’t have to involve in this process. 
     a = 5
         b = "3" then a+b =10
      type(int(a+b)) >> int but we can change this one by executing type(float(a+b)) >> 10.0 i,e float datatype.

      ii> Explicit typecating - In this method, Python needs user involvement to convert the variable data type into the required data type. 
         if a = 5 then n = float(a), print(n) >> print(type(n)) results 5.0  <class 'float'>
         
---->>> Even python Converts string to int: a = "5"
                                           print(type(a))
                                           print(type(int(a))) results <class 'str'>  <class 'i

Q6 : How do conditional statements work in Python? Illustrate with examples. 

Ans:  An execution of a program rely on the flow control that governs the order in which statements and instructions are executed. Conditional statements in          Python play a key role in determining the direction of program execution. There are mainly four types of conditional statements are there:

Python If Statement 
Python If Else Statement
Python Elif
Python Nested If Statement

------>>>>>>>Python If Statement: The if statement is the most simple decision-making statement. It is used to decide whether a certain statement or block of                                     statements will be executed or not. Here, execution of a block or statement depends on the condition checking. if given test                                    condition was true then it will execute if block otherwise it will execute the block below if block.
         Here is the syntax: if condition:
   statement1
statement2
# Here if the condition is true, if block 
# will consider only statement1 to be inside 
# its block.     Ex1 : marks = 4                      Ex2: marks = 45
                        if marks > 35:                                   if marks < 35:
                  print("you are passed the exam")                                      print("you are passed the exam")
                       print(" you are a looser") o/p is  'you are passed the exam '                               print(" you are a looser")     
                                                                                                     output will be 'you are a looser'                                        
-------->>>>>> Python If Else Statement: The if statement alone tells us that if a condition is true it will execute a block of statements and if the condition                                          is false it won’t. But if we want to do something else if the condition is false, we can use the else statement with                                            the if statement Python to execute a block of code when the Python if condition is false.  

 Syntax of If Else condition: if (condition):
                            # Executes this block if
                                 # condition is true
                              else:
                     # Executes this block if
                     # condition is false
 
  Ex: i = 20
if (i < 15):
    print("i is smaller than 15")
    print("i'm in if Block")
else:
    print("i is greater than 15")
    print("i'm in else Block")
print("i'm not in if and not in else Block")     O/P:  will be i is greater than 15
                                                        i'm in else Block
                                                       i'm not in if and not in else Block                
                                                     
------->>>>>>>>>Nested If Statement A nested if is an if statement that is the target of another if statement. Nested if statements mean an if statement inside             another statement. Yes, Python allows us to nest if statements within if statements. i.e., we can place an if statement inside another if statement.

Syntax:  if (condition1):
             # Executes when condition1 is true
              if (condition2): 
                # Executes when condition2 is true
          # if Block is end here
              # if Block is end here

Ex code  : i = 10                                       
if (i == 10):
    if (i < 15):
        print("i is smaller than 15")
        if (i < 12):
             print("i is smaller than 12 too")     O/P: i is smaller than 15
        else:                                           i is smaller than 12 too
            print("i is greater than 15")        


------------>>>>>>>>>>>> Elif statement: Here, a user can decide among multiple options. The if statements are executed from the top down.
                                         As soon as one of the conditions controlling the if is true, the statement associated with that if is executed, and                                           the rest of the ladder is bypassed. If none of the conditions is true, then the final “else” statement will be executed.

Syntax: if (condition):     
    statement
elif (condition):
    statement
.
.
else:
    statement

Ex code : i = 25
if (i == 10):
    print("i is 10")
elif (i == 15):
    print("i is 15")
elif (i == 20):
    print("i is 20")
else:
    print("i is not present")  O/P : i is not present
 
Q7) Describe the different types of loops in Python and their use cases with examples. 

Ans: loop statement>> loops allows us to execute a block of code repeatatively untill a given condition will false.There are two types of loops are there:
 i> While loop 
 ii> For loop

i > While loop : a while loop is used to execute a block of statements repeatedly until a given condition is satisfied. When the condition becomes false, the                     line immediately after the loop in the program is executed.
Syntax : while expression:  Ex: 
        statement(s)
         .
    Ex:  n = 15
     i = 2        O/P : 2 3 4 5 6 7 8 9 10 11 12 13 14
while (i<n):
    print(i)
    i = i+1     
  
Ex:  count = 0         O/P: pwskills
while (count < 3):          pwskills
    count = count + 1       pwskills
    print("pwskills") 

ii > For loop : are used for sequential traversal. For example: traversing a list or string or array etc. In Python, there is “for in” loop which is similar to                 foreach loop in other languages. Let us learn how to use for loops in Python for sequential traversals with examples.

Syntax: for iterator_var in sequence: ex: 
    statements(s)

Ex code:                            O/P: 
list = [1, 2,"Kumar", 2.5, 3+4j]
for i in list:
    print(i)     : 
    