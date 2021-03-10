# Object Oriented Programming II

Tuesday 3/9/21

Project: Adventure Game II (Github link goes here)

## Inheritance

- One class can be an instance of another class
- parent/child classes, child can add function to the parent
- child classes contain more detail

## Composition

- If one class is composed of another class, can't exist on its own
- less closely related: a restaurant has an employee. The employee still exists if there's no restaurant.

## Python for Dummies

(my notes on learning the language coming from Javascript)

Using vscode:

- to run a program, ctrl + shift + p: run python file in terminal
- It opens another terminal you can access from dropdown, bash stays separate
- cd into folder where the program is
- python filename.py runs the file
- up arrow recalls last command

## Adventure Game Notes

How do I handle exit logic?

I want a list of available exits to print

I can mess with the code linking the rooms together

valid inputs are n, e, s, w

if n, check if this.room has a n_to that is longer than 1

if not, "You can't go north from here"

repeat for e, s, w

logic is in the cases, doesn't need to be in room class

```python
#     fancyline = "»»————-------　★　-------————-««"
#     boringline = "———————————————————————————————"

#     # request input from the user
#     # needs to go after things that are printed otherwise it sits and waits for input
#     userInput = input(userPrompt)

# if _name_ == '_main_':
# https://www.geeksforgeeks.org/what-does-the-if-__name__-__main__-do/
```

## Stuff I Googled

- check if something is in an array: if x in arr (well that's straightforward).
- lowercase syntax: StringContent.lower()
- python dictionary syntax: w3schools, looks a lot like a js object. Can separate with returns for readability.
- triplequotes in python: used for a multi-line string
- how to add a new key to a dictionary: easier way was to initialize all keys with an empty array for the value, then filter for the non-empty values
- get list of items in a dictionary conditionally: list comprehension with a filtering condition. ex: `>>> [item["Id"] for item in categories if item["hasCategory"]
[1350, 113563]`
- python list comprehension filter syntax

