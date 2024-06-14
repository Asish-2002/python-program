what is python ?

-python is simple ,easy & portable.
-python is free and open sources.
-python is high level,interpreted language.
-python was devloped by Guido van Rosum.

- Python is interpreted language means when we write python code its executed the code line by line thats when we called python is 
 interpreted language.
 - print is function to give output statement in python. simply we can tell "print" is output function.

 character set of python language :-
 1.letter-> A-Z , a-z
 2.Digits-> 0-9
 3.Special character-> -,+,/,* etc...
 4.Whitespaces-> Blankspaces, Tab ,newline

 what is variable ?

 - A variable is a name given to a memory location in a program or else we can simply say variable is a container to store some data.

 example -
 name = "shradha"
 age = 23
 salarry = 23000

 variable names = name,age,salary
 variables values = "shradha" ,23 ,23000

 Rules for identifires :-
 1.identifires - names of the variable
 2. identifires can be combination of uppercase and lowercase letters, diogits or an undescore(_). ex-myVariable,variable_1
 3.an identifires can not start with digits. so while variable1 is valid but 1variable is not  valid.
 4.we can not use special character or symbol like !,#,@,% etc...
 5.identifires can be of any length.
 6.variable name should be small and meaningful like when we give our age in that case take the vareiable as "myAge". [myAge ->camel case letter]


 - 'type' is a operator to show the datatypes name in our variables like which datatypes we use in our variables.

 Data types:-

 -mainly data types of 5 types in python.
 -these data types are unmutable or build in data types.
 1.Integer - +ve value , 0, -ve value
 2.string - "hello" , "asish" ,etc.....
 3.float - 3.43 , 5.89 etc....
 4.boolean - true,false
 5.none- not assign 

 Comments in python :-

 -when we write some code but we dont want to execute it then we give the comment line to that place so that line of code will not executed.
 - comments are of 2 type.
 1. Single line comment-
 when we give the single line comments in python we did it on "#'.
 ex.
 # single line comment
 # this is a comment
 2. Multi line comment
 when we give the multi line comment in python we did it through """_""".
 ex.
 """
 multi line 
 comments 
 """

  Types of operator :-
  -simply we can say operator is a symbol that performs a certain operation between operands.
  ex. a+b
  a,b -> operands
  + ->operator
  -There are 4 types of operator are present in python 
  1. arithmatic operator. (+,-,*,/,%)
  2. relational operator. (==,!=,<,>,<=,>=)
  3. assignment operator. (=,+=,-=,*=, /=)
  4.  logical operator. (and , or , not)

Input in python:-
-Input() statement is used to accept values(use keyboard) from users.

String:-

-string is a data type that storev a sequence of characters.

str1="This is a good day"
str2="This is a beautiful day"
str3="""This is a bad day"""


-all these strings are real string because in python , it supports all of the syntax like-"",'',""" """

-\n (new line) - when we want to break our line into a new line then we can give the new linw symbol in that place so that line get breaked automatically.

Basic Operation of string:-

1. concatenation->
     "hello" + "world"=
2. Length of the string->
      len(str)

Indexing of string->
-webbocket-> 012345678(indexing)
-Always indexing start from '0'.

Slicing of string->
-Accessing parts of a string.
-ending index is not counting.
-syntax - str[strating index: ending_index]

str= "webbocket"
str[0:3]-web
str[:3]- web
str[3:]-bocket

Function of string ->

ex-
str= "i am a  coder"
1. str.end switch("er.")- returns true if string ends with substring
2. str.capitalize()- returns 1st char is capital
3. str.replace(old,new)- replace all occurance of old with a new
4. str.find(word)- returns 1st index of 1st occurance
5. str.count("am")- counts the occurance of substring in string


conditional statement:-

-used to handle the condition in your program.
-syntax(if-else-if)
-elif means else-if

if(condition):
    statement1
elif(condition):
    statement2
else:
    statement(default)

Lists in python :-

-Lists is a built-in bdata type  that store set of values.
-it can store elements of different types like integer, float and string etc...
-in lists we can make indexing.
-in lists we can find length of the list also.
-in lists we can also do the slicing activity.

ex-
marks= [87,56,45,90]- array and list
students=["Hitesh",78 ,"Bhanjanagar"]-list

List slicing:-

-it similar to list slicing.
-syntax:- list_name[starting_idx: ending_idx]
-ending index is not included.

marks=[24,45,67,89,98]
marks[1:4]->[45,67,89]
marks[:3]->[24,45,67]


Lists methods:-

list=[9,4,7,8,1]
list.append(6)-adds one element at the end of the list-[9,4,7,8,1,6]
list.sort() - sort the element in ascending order- [1,4,7,8,9]
list.sort(reverse=true) -sorts the element in descending order-[9,8,7,4,1]
list.insert(idx,el)- insert the element at index
list.remove(1) -remove the first occurance of element- [9,7,8,1]