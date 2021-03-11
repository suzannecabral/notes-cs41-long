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

> lecture video (LINK ME) has a good step-by-step explanation of what happens to each variable through the steps

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


