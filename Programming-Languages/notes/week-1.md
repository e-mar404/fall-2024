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
{ |e| e * factor } -> this is a closure because factor had to be bounded or losed over to a variable outside the scope of the block

## Functional style basics

In order to get rid of the iterative process that we have we use the following to iterate through elements, return a list with "modified" values (a copy so not mutating the original), return sum of elements, etc we use the following concepts:

1. **map**
2. **filter**
3. **reduce**

*end of functional style part II*
