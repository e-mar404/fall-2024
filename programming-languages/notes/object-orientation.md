# Object Orientation:

// this is very broad overview

## What it is and pillars of the Paradigm?

OOP is about decomposing an application into objects. These objects are an abstractions that have methods and do things for you.

The 4 pillars are:

- Abstraction
- Encapsulation
- Inheritance
- Polymorphism

## Singleton

In order to make a singleton the one true instance as a field within the class and not being able to create a new instance of a that class. There will be a `getInstance` method that will check if the instance exists, if it does then it returns it if it doesn't exists a new instance is created.

In Java implementing a singleton is expensive but you can get around it with using an `enum`

Scala on the other hand handled it better. Since there is already a built in singleton object implemented by the language.

*end of object orientation I*
