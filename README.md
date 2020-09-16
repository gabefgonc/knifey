# Knifey

A python module to make the writing of day-to-day scripts easier.



```py
from knifey import Command
Command("ls").pipe("grep i").execute().printResult()
```

