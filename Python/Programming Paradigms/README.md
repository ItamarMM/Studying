# Programming Paradigms... Introduction
I wanted to understand why Object Oriented Programming (OOP) was so popular, and yet, unknown for a DevOp with 2 years of experience. What were the main usages of OOP and so on. So, I started comparing it to other programming paradigms mainly in Python, because as for now is the language that I dominate the most, so, these are my study notes on the most common programming paradigms.

A programming paradigm is a "method" of programming. 

There are multi-paradigm languages, like Python, Java, Ruby, C++, C#, Visual Basic, Go!... that *support* multiple paradigms, but do not necessarily *enforce* all of them.

# The main programming paradigms
## Machine code
The first programming paradigm is machine code, in which, instructions are given in a sequence directly written in machine language. 

## Imperative
Any programming language that works directly with a list of instructions, for example, assembly code.

## Structural
Would refer to this paradigm as modular programming.
Reusing the code would be the main characteristic.

- Procedural:

    Relies on modules(procedures/functions) to be organized. It is supposed to "be better for small programs".
    - Functional:

        Modules are written from functions, whose returns would change only based on the input.
    - Architectural patterns:
        Not really "programming paradigms", but was interesting:
        - Service-oriented programming (SOA):
        
            Reusable modules would be services with known interfaces from the company. Gives the governance control to the company.
        - Microservice programming:
        
            Modules that do not store data internally, scalable and resilient in cloud deployments.

- Object-Oriented Programming (OOP)

    Its organization relies on data and objects, rather than functions/logic. It is supposed to "be better for bigger programs".

    The main concepts of OOP are:
    - Classes: Definitions of characteristics of the objects.
    - Objects: Individuals based on classes definitions.
    - Polymorphism: The characteristic that something can be in multiple forms. For example, in Python two different classes could have the same method names.
    - Abstraction: The user would have the internal details hidden and would only see the basic functionalities.
    - Encapsulation: It "does not really exists in Python", but, is a way to privatize methods and not letting other objects access such methods.
    - Inheritance: When a class is based on a base class, maintaining the code of the base class.
    
    As I have seen in Brian's video, OOP gives the devs too many tools and options while not imposing the appropriate constraints.

# Opinion
After watching the video and reading some people's opinion regarding programming paradigms (mainly OOP vs functional programming)
- Modularity is key for organization, does not matter the programming paradigm used. 
- Having 20 layers of subclasses and creating a 30 functions that could be one(being a "x" paradigm defensor) are not actually that good for organization, but actually could slow developing actual functionalities.
- Whether you take one paradigm or another, separating your code in clear ways, and supporting code is clearly hard, and no paradigm will make the code magically organized and understandable. As bigger the project, harder the maintenance/organization.

I really liked the summarization of Brian Stewart in Brian's video: **""Bolting on" without understanding the design of a program is a fast way to create spaghetti, not matter functional or OO."**

# Bibliography
These study notes were obtained based on the information obtained from:
- [Wikipedia: Programming paradigm](https://en.wikipedia.org/wiki/Programming_paradigm)
- [Brian's Will video "Object-Oriented Programming is Bad"](https://www.youtube.com/watch?v=QM1iUe6IofM)