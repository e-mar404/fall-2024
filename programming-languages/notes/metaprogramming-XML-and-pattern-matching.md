# Metaprogramming, XML & Pattern Matching

Metaprogramming is a program that writes a program. Code that writes code. There is also code generation, which is an output of code based on code that comes in.

## Method missing

Meta programming can be used to call a specific function when a method is missing and then from there you can do wtv you need to do. For example if the method starts with find you can parse the left over of that method and see if it makes sense and dynamically do something based on the name.

On the code bellow there will just be a print statement with the name of the missing method

```ruby
class Person
  def work
    puts "working..."
  end

  def method_missing(name, *args)
    puts "called MethodMissing with #{name}"
  end
end

joe = Person.new
joe.work
joe.sing
```

## DSL in Groovy

- Domain Specific Language is a language that is very narrow for a specific situation.  
- They are heavily context driven
- very effective way of communicating between people that are fluent in the DSL 

### External DSLs

- you create the language, parser and grammar
- infer the parsed code to something meaningful
- creating the parser can be a lot of work, this cannot be an after thought

### Internal DSLs

- you do not create a parser for the language because the language that will host the DSL does all the hard work
- the DSL is a subset of the hosted language
- the host language should have fairly low ceremony (no ;, no significant spaces, no () or .?)
- the host language should have metaprogramming to give flexibility

## DSL Example in Ruby

```ruby
# processor.rb
$players_and_scores = {}

def self.method_missing(name, *args)
  $players_and_scores[name] = args[0]
end

def winner ()
  maxScore = 0
  theWinner = ""

  $players_and_scores.each { |person| 
    if (maxScore < person[1])
        maxScore = person[1]
        theWinner = person[0]
    end 
  }

  puts "#{theWinner} won with #{maxScore}"
end
```
```ruby
# commands.rb
joe 12
bob 14
jim 8
winner
```
```ruby
# sample.rb
dsl = File.open("ruby/commands.dsl").read
code = File.open("ruby/processor.rb").read

eval(code + dsl)
```

## Literally why i want to learn vim proficiently

"GUIs make a bellow average user productive but makes an expert user and dumbs them down" -Venkat
To become an expert you have to go past the GUI?

*end of lecture IV*
