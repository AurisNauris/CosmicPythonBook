# Introduction

## Why do our designs go wrong?

- I would argue that the authors wrongly establish definitions of chaos (randomness) and order. Neither is complex, the state in between is a complex one because randomness can be understood easily by statistics, while order can be understood easily by a unit cell and translation vector.
- Software system is akin to a garden in that it needs to be looked after, pruned, trimmed around otherwise you will end up with a highly complex system, difficult to deal with.
- **morass** - a complicated or confusing situation
- In a chaotic system every part of code does a little bit of everything, so they start to look the same
- Without a proper separation of concerns, changing how, e.g., the software interacts with emails will be messy, because then one will have to go through all the code and this will very likely cause massive breaks
- "A big ball of mud is the natural state of software in the same way that wilderness is the natural state of your garden. It takes energy and direction to prevent the collapse."

## Encapsulation and Abstractions

- encapsulation: simplifying behaviour and hiding data. To simplify behaviour, we give a taks to a well-defined object or function.
- abstraction: an object/function that does one thing, that has input and output and is used by another part of the code so it would not need to deal with the logic.
- Encapsulating behaviour by using abstraction makes code easier to read, test, and maintain
    - [Responsibility-Driven Design](https://www.wirfs-brock.com/Design.html)
        - "Objects are more than simple bundles of logic and data... they are service-providers, information-holdsers, structures, coordinators, controllers, and interfacers to the outside world.
    - Think about code in terms of behaviour rather than data and algorithms

## Layering

- When one object uses another, we say that the one **depends** on the other.
- Dependencies form a network/graph
- In a big ball of mud, dependencies are out of control
    - Changin one node of the graph affects a lot of other parts of the system
    - Layered architectures suggest a way to solve this
- Layered architecutre: our code is divided into discrete categories/roles and we introduce rules how they can interact
    - e.g. Presentation Layer -> Business Logic -> Database Layer

# Dependency Inversion Principle

- Reference to: [SOLID](https://www.digitalocean.com/community/conceptual-articles/s-o-l-i-d-the-first-five-principles-of-object-oriented-design)
    - SOLID is the acronym for five object-oriented design (OOD) principles by Robert C. Martin
        - S - single-responsibility principle
            - "A class should have one and only one reason to change, meaning that a class should have only one job."
            - A good example is where you want to have a class that calculated the area of all the given shapes. In this system, each shape is an object on itsown right and has a function or an attribute that return area that is specific to the shape, whereas a class AreaCalculator() would just aggregate the area output for each shape. So if you create a new shape, there is no need to change the AreaCalculator().
            - Also the AreaCalculator() should not include the output formating functions because say if we need to now update how we want our output is presented/printed, now we have to update AreaCalculator(). And if we have a few objects and want to make them consistent, then we will have to update them all... not great. AreaCalculator() should be primarily concerned with the sum of the areas and should not care whether the users wants JSON or HTML.
        - O - open-closed principle
        - L - Liskov Subsitution Principle
        - I - Interface Segregation Principle
        - D - Dependency Inversion Principle

