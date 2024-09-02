# Typing

## Data and Values

*Values*: literals that we use in applications ('hello', 7) 
Data: sets of values which represent a lot of different things

## Types

- We process data in different types, string, int, float, etc.
- We can classify values in terms of types, (v is a of type T) 
- expressions can return something with type T so we know that every result from an expression is of type T

## Data Types

**Primitives**: Types like int, longs, char. C is a language that deals with these.

**Composites**: type that is a collection of other types, an example is a string being a collection of chars. Composite types are usually referred with objects.

**Recursive**: an object that has another object that has even more types. Similar to a hierarchical structure.

## Functional languages and lists

Functional languages tend to be work on the head of the list a lot more compared to the rest of the list. This came about because on the constraint of immutability.

It is very common to divide a list by the head and the tail. The head being the first item of the list and the tail the remaining body.

## Static vs Dynamic Typing

There is not a clear better way, they each have advantages and disadvantages.

**Static**: types are verified at compile time (usage represents the intent)
**Dynamic**: types are verified at runtime, sometimes the language might not even have a compiler

### Static Typing

Sometimes even statically typed languages might have a certain amount of flexibility. An example is double and int in java. EX:

``` java
// this is allowed

double value = 4.0;
value = 3;
```

*It is not true that you specify type on static and that you don't on dynamic*. Dynamic languages might still be able to declare values with type definitions and static languages might not always require type declarations (this is called type inference).

"The more statically typed a language is the less manual typing you'll have to do" -Venkat

Type might not be inferred correctly at compile time. An example of this is type casting. Ex

``` java
List scores = new ArrayList();

scores.add(1);
scores.add(1.0);

int total = 0;
for (int e : scores) {
    total += (Integer) e;
}

// this will compile successfuly but fail at runtime by the missmatched types
```

*end of typing - part II*
