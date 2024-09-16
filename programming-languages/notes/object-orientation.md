# Object Orientation:

**Keep in mind this is a very broad overview, i did not go in depth**

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

## Static

From the testing point of view static methods are pretty difficult. It also becomes a problem with not very straightforward behavior when in web. 

## Interfaces

A grouping of methods with no implementation. Traditionally used with design by contract. If you use an interface you sign a contract in supporting the methods of the interface.

### Interface collision

What happens if multiple interfaces have a method with the same name and a class tries to defining that method while adhering to the multiple interfaces. 

Well in Java one implementation of the method will work for both. This happens because there is no context as to which method's interface you are implementing.

In C# you can use explicit method implementations so you can define each method differently.

## Overloading

- Usually confused with with Polymorphism  
- in terms of binding it is static binding, what method to call is decided at compile time
- for multiple methods to be over loading each other they need to be in the same scope
- methods need to have a different signature

## Polymorphism

- methods have the same name but are defined in two different but related scopes
- gives you the extensibility needed in OOP 
- inheritance is not needed to achieve Polymorphism
- dynamic/runtime binding
- in order for Polymorphism to work correctly both the base and derived classes should work interchangeably (what works on A should work on B)

## Traits and Mixins

These are used to handle multiple levels of inheritance in an ok way. Traits are used during compile time while Mixins during runtime.

Traits are very similar to interfaces but unlike interfaces, you can make a singular object instance that implements that interface. This trait is specified during compile time.

Mixins can be added to classes during runtime. This gives a greater amount of flexibility.

## Using base objects and their derived objects

### Covariance

- you can treat an object as either an object of that type or an object of its base type

### Contravariance

- take an object of a base type and you can treat it as object of a derived type
- usually doesn't make too much sense so languages do not support it much

### Abstract Types

- a particular type is not decided until a later time
- will let the derived class decide

*end of object orientation VII*
