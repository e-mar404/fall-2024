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

### Finding the square root

**Successive Refinement**
//      Sqrt
//       |
// Sqrt Successive
//     /      \
// Good Enough  Improve Guess
//  /     \           \
// Square  Abs       avg

## Abstractions and Encapsulation

- procedures should abstract and encapsulate the details
- they should tell you what they provide and hide the details of how they do it, we should not care how a procedure does things
- user should not be forced to know the details of the implementation

*sqrt function above breaks the encapsulation requirements*

## Formal Parameters & Binding

- names chosen for formal parameters should not affect the choice of names by user of a procedure
- formal parameters are bounded variables
- local variables are only visible within procedures
- these are not affect by outside procedures or affect them

## Dependency

- procedures tend to depend on other procedures
- increases coupling
- if you modify the name of a procedure your procedure depends on, you will affect your procedures implementation

## Lexical Scoping

- you don't have to pass parameters repeatedly to nested procedures
- they can use parameters both formal and local in further computations defined in the nesting block 

## Procedures in different languages

### Ruby

``` Ruby
def max(*numbers)
  max_value = numbers[0]
  
  numbers.each do |e|
    max_value = e if e > max_value
  end

  max_value
end

puts max(1, 2, 4, 5 , 0)
```

### Scala 

``` Scala
def max(numbers: Int*) = {
    var maxValue = numbers(0)

    for (e <- numbers) {
      if (e > maxValue)
        maxValue = e
    }

    maxValue
}

println(max(1, 2, 3, 5, 0))
```

### Erlang 

``` Erlang
#!/usr/bin/env escript

main(_) ->
  io:format("~p~n", [max([1, 2, 3, 4, 5, 0])]).

max2(A, B) when A > B -> A;
max2(_, B) -> B.

max([H | []]) -> H;
max([H | T]) ->
max2(H, max(T)).
```

*end of Procedures - Part IV*
