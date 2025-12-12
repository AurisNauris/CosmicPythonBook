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
            - Objecs should be open for extension but closed for modification. You should be able to extend teh class without modifying the class itself.
            - Coding should be done to an interface as opposed to implementation. This means that you state that you need an object that acts in a certain way. You don't care though about the version/brand of the objects, as long as it follow the rules of the interface. Essentially think of that your interface is an electrical socket, and your coding to an interface means that you write a code that expects to have any socket that is with two pins and 240 Volts but it does not specify which exact sockets it is. Now your code will work regardless of which socket you chose to use in the end. Now if your device (i.e. code) say does not work with one socket, you can test it at another socket to check where is a problem, or other way round as well.
            - Say you are building a `AreaCalculator()` class that accepts a list of shapes and returns their area. But how do you ensure that a list has only shapes and not accidentally one that is not a shape or if all shapes have `area()` method? One way to do that is to make all different types of shapes a subclass of `GeneralShape` class and then calculate the area only if the shape belongs to this class. And this `GeneralShape` class can itself define general methods.
        - L - Liskov Substitution Principle
            - "Let q(x) be a property provable about objects of X of type T. Then q(y) should be provable for objects y of type S, where S is a subtype of T." This means that every subclass or derived class should be substitutable for their base or parent class, like if you have a class `Animal` and a subclass `Zebra`, you should be able to swap `Animal` and `Zebra` anywher in your code, and the code should still work exactly as expected.
            - This ensures that every class must follow the interface rules, like the socket analogy in a few bullet points above. It must adhere to the interface in syntax and in behaviour.
            - In maths, a square is a rectangle, but in code it is often not the case. Like you can change width and height independently in rectangle but in a square they are coupled. If you swap `Rectangle` and `Square` in a function that expects to stretch a shape, the square will behave unexpectedly.
            - LSP violations when:
                - Throws a "not implemented" exception
                - Ignores the method - the method does nothing when the parent implies it should do something.
                - Strengthens preconditions - e.g. the parent accepts any number, but the subclass only accepts positive numbers
                - Weakens postconditions - the parent guarantees the database is saved, but the subclass "maybe" saves it.
            - The test: "if it looks like a duck, quacks like a duck, but needs batteries - you have the wrong abstraction."
            - **Inheritance is often the wrong tool**. Just because two things share a name or look alike in the real world, doesn't mean they share the same behavior in code.
                - `Bird` class would implement what all birds do for sure, then you would implement `Flyable` that is a subclass of `Bird` for birds like `Sparrow`, but `Ostrich` would be a direct subclass of `Bird`.
                - `Square` and `Rectangle` are siblings, not parent/child in code. Thus, you make them both distinct class that implement common interface, like `Shape` or `Quadrilateral`. This is because their rules for mutation are different:
                    - `Rectangle.setWidth(5)` does not change the height.
                    - `Square.setWidth(5)` also changes the height to 5.
                - Say you have three different ducks, one that is a real duck, one that is a rubber duck and a robbot duck. Now you can create a class `Duck` and this duck on instantiation would expect to receive another callable that is a `FlyBehavior`. So you still have a single class for all ducks, but the methods etc are modified outside.
        - I - Interface Segregation Principle
        - D - Dependency Inversion Principle

- [ ] Coding to an interface is an integral part of SOLID.
