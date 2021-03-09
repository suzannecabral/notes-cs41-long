# Object Oriented Programming

helfpful link: [FreeCodeCamp on 4 Pillars of OOP](https://www.freecodecamp.org/news/four-pillars-of-object-oriented-programming/)

## 4 pillars:

1. Encapsulation
2. Abstraction
3. Inheritance
4. Polymorphism

### Encapsulation

Keeping the inner workings separate from the public interface. Data hiding. Make things inaccessible if they aren't needed.

Example: TV and Remote

The user doesn't care what happens when you push the button, just that the volume turns up or the channel changes. You can make internal changes to the program as long as it doesn't affect the inputs and outputs.

### Abstraction

Hiding the details of the object and making the interface easy to understand, not getting swamped by details that aren't used by this implementation.

Example 1: Which coffee maker is better? One where you have to remember a sequence of how to make the coffee, or one that has a simple "Make Coffee" button?

Example 2: Car object with Driver and Mechanic

Each of them need access to different methods and information about the same car

### Inheritance

Instantiating objects

A dog is a type of animal, it inherits properties from the animal class.

### Polymorphism

Treat a class differently depending on what subclass is implemented


ChessBoard > Piece > Rook

Rook has different movement rules than Pawn. They each have a .move() method that overrides the default behavior.

## Translating from idea to program

1. Describe the project in detailed sentences
2. Nouns > Classes
3. Adjectives > Attributes of Nouns (Classes)
4. Verbs > Methods on Classes

- If there is only behavior and no stored data, it should probably be a function instead.
- If there is only stored data and no behavior, it should probably be a list/array/set/dictionary instead.

## Warmup Exercise - Parking Lot

```
    Lot
        spaces

    Space
        price
        am_price
        pm_price

    Vehicle
        spaces_taken

    Customer
        vehicle

    Purchase
        customer
        space
        total_price
        expiration
```

### Class methods

```__init__```

- defines how a new instance of the class is initialized
- tells it what variables to set when you initialize

```__str__```

- used to return a string representation of an object
- you can set it to return useful info for debugging
- by default it returns the object's location in memory.
- str is informal, meant to be readable for end users

```__repr__```

- also returns a printable representation of the object
- convention: set it to show how you create a new instance of that object, required parameters
- repr is meant to be "official", gives all info about an object
- meant to be unambiguous for developers
