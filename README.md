# Knifey 

A python module to make the writing of day-to-day scripts easier.

## Installation
```sh
pip install Knifey
```

## Keep it simple, stupid!

Knifey is designed to be very simple to use. At the moment, it has only one class, the `Command`, that is useful for executing system commands and modifying them on-the-fly!
Want to see an example? Here it is:

```py
from knifey import Command
Command("ls").pipe("grep i").execute().printResult()
```


Here, you create a command, which is "ls". Then, you pipe that result to "grep i". Now, the command is "ls | grep i". The last thing to do is to execute the command, and then print its result.

And, if you want to save the command result in a variable or pass it to a function, just use getResult instead of printResult.

```py
from knifey import Command
import os
for i in Command("cat /etc/passwd").execute().find(os.environ["USER"]):
	print(i)
```

Wow! That's a new method, find! This one returns a list of the found strings on a command result. First, you create the command, which shows the contents of /etc/passwd (cat /etc/passwd). You execute it, and search for your username on the file (the username is being received from the enviroment variable USER on an unix system). Finally, you iterate over the list of found strings, and print them!

That's it! You learned how to use knifey! Very easy, don't you think so?

