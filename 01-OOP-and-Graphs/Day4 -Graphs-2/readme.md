# Graphs 2

## Social.py

using debugger to visualize

- breakpoint: visited dictionary created, right before "implement me" comment
- watch: (once it appears, right click under locals, "watch", then step forward to see changes)
    - visited
    - q.storage
    - path
    - newuser_id
    - self.friendships

> [lecture video](https://youtu.be/hpy8ztTbC1A) has a good step-by-step explanation of what happens to each variable through the steps

- there is some redundancy when appending to queue, ie `[1,9,4,9]` 

- this method works with any bft that tracks a path
- could model a bot traversing every single room in the adventure game

dense vs sparse graphs

- dense: lots of connections, ie 1 user has 50 connections, like aiport outgoing flights
- sparse: like a line, each user has 1 connection, like a route
- dense = more collisions
- linear collisions is bad on a dense graph
- sparse graph: linear is better?

using time module in python to test how long program is taking

### Stack

```python
class Stack():
    def __init__(self):
        self.storage = []

    def push(self, value):
        self.storage.append(value)
    
    def pop(self):
        if self.size() > 0:
            return self.storage.pop()
        else:
            return None

    def size(self): 
        return len(self.storage)

```

### Queue

```python
class Queue():
    def __init(self):
        self.storage = []

    def enqueue(self, value):
        self.storage.append(value)

    def dequeue(self):
        if self.size() > 0:
            return self.storage.pop(0)
        else:
            return None

    def size(self):
        return len(self.storage)
```
Exact same thing, using lists, except queue removes at index 0

