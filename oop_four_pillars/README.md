# What is object oriented programming?

Object-oriented programming (OOP) is a computer programming model that organizes software design around data.

# What are the four pillars of object oriented programming are:

- Abstraction
- Encapsulation
- Inheritance
- Polymorphism

# OOP Diagram
![](oop%20image.jpg)


# Explain each pillar?

Abstraction - Abstraction in python is defined as a process of handling complexity by hiding unnecessary information from the user.

Encapsulation - Encapsulation in coding where data and methods are bundled together into a single package.

Inheritance allows us to define a class that inherits all the methods and properties from another class.

```
class Animal:
    
    def eat(self):
        print( "I can eat!")
    
    def sleep(self):
        print("I can sleep!")

class Dog(Animal):
    
    def bark(self):
        print("I can bark! Woof woof!!")

# Created an object for the Dog class
dog1 = Dog()

dog1.eat()
dog1.sleep()
dog1.bark();

```
The output for this class should be

```I can eat!
I can sleep!
I can bark! Woof woof!!
```

Polymorphism is a programming term that refers to the use of the same function name, but with different signatures, for multiple types.



# What are the benefits of using Object oriented programming?

- Productivity - Construct new programs quicker through the use of multiple libraries and reusable code
- Security - Complex code is hidden and internet protocols are protected
- Flexibility - Polymorphism enables a single function to adapt to the class it is placed in. Different objects can also pass through the same interface.


# What are Lambda functions in python?

lambda is a keyword in Python for defining the anonymous function. A lambda function can have multiple variables depending on what you want to achieve.

# where can the lambda function be useful?

Lambda functions can be useful to write concise code without wasting multiple lines defining a function. They are also known as anonymous functions.