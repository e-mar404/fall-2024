# Week 3 - Procedures

# Procedures 

## Overview

- Made of expressions
- composition of expressions
- exist in a level of abstractions, they do something/represent for you
- in a functional language a procedure does not have any side effects

## REPL

- read-evaluate-print loop
- started with lips Interpretive environment, but several languages now support it
- REPLs give quick feedback
- easy to evaluate expressions
- helps learn a language quickly from the ease of just typing and running code quickly

## Expressions

- evaluated and produce a result
- a number is a primitive expression (2, 49)
- combinations: you can use operators to create other expressions (2 + 4)

## Variables

- identified by name
- has a value
- definition: defining a specific variable
- assignment: related to mutation

## Order of Evaluation

### Applicative Order
- operators and parameters evaluated before procedure is evaluated
``` scala
def square(x) = x * x
square(2+3) = square(5) = 5 * 5 = 25
```
- this is efficient 
- can remove duplicate computations

### Normal Order
- operations and parameters are evaluated only after the procedure is fully expanded
``` scala
def square(x) = x * x
square(2+3) = (2+3) * (2+3) = 5 * 5 = 25
```
- result is same as applicative order
- not as efficient
- lazy evaluation can come in handy

## Decomposing Procedures

- easier if we decompose procedures into smaller procedures
- easy to comprehend, explain, express and maintain
- if a language does not protect encapsulation and abstraction it makes decomposing procedures harder 

*end of Procedures - Part I*
