# Functional Style  Programming

## Imperative vs Functional Style

Imperative -> step by step instructions

- this is the same style of code that we have been writing for a while (think C code)

### External Iterator 
Iterate through every element and keep an external variable to enumerate and go through elements of a collection 

Fucntional -> immutable state only output

- functions are first class citizens

- functions are higher order
    - pass functions to functions and return functions

- functions dont have any side-effects 
    - promote immutabilitym, if wanting to use something then make a copy and change it on the process
    - correctness can be proven mathematically
    - input -> blackbox -> output
    - easier to perform multithreated processes since there are no mutable changes forcing a specific order of operations

### Internal Iterator
Specify a body of code that gets executed within the contexts of the elements of a collection without a need to control the iteration ourselves

### Scope of function blocks

{ |e| e * 2 } -> this is a block/function value
{ |e| e * factor } -> this is a closure because factor had to be bounded or closed over to a variable outside the scope of the block

## Functional style basics

In order to get rid of the iterative process that we have we use the following to iterate through elements, return a list with "modified" values (a copy so not mutating the original), return sum of elements, etc we use the following concepts:

1. **map**
2. **filter**
3. **reduce**

## Mutability vs Immutability

- In a pure functional language we work with the constraint of immutability. I is still possible to build a proper app with a functional language but just in a different way.

- A programming language that follow this pure functional way is Erlang. Scala on the other hand has functional programming capabilities and style of writing but still has mutability.

- Even with functional style languages we can use different languages depending on the end goal.

*end of functional style IV*

# Expressions and Symbols

## Expressions vs Statements
- a *statement* is a command that we execute and perform a certain action. 
- an *expression* returns a value/result.

There are some languages that only have expressions and do not use statements. One of the benefits is that you can ignore the result if you don't want to use it but with a statement there is no result to look at. An example of this programming language is Ruby.

If everything is an expression then the number of temp variables and ceremony is reduced since everything returns something and the return value can be used further.

## Interning

Interning is the re=use of objects of equal value on-demand instead of creating new objects. This way if there are multiple vars with the assigned value of "hello" they all point to the same instace of "hello" in memory instead of creating multiple instances. This can be a pretty powerful concept if used correctly.

## Symbols

A symbol is like a reference to a variable. This helps to only have something that represents an item and not necessarily the value itself. This can be seen on the `method_missing` on ruby when creating a class that gets a method called that does not exits.

```
class Person
    def method_missing(name, *args)
        puts "called method ${name}"
        puts name.class // Symbol, this is a reference to the method called
    end
end

sam = Person.new
sam.sing // prints "called method sing"
```

*end of week 1 lectures*

# Questions to think about:
**How to get around a mutable application state?**
**Pattern matching with Erlang**
