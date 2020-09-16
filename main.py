from knifey import Command
Command("ls").pipe("grep i").execute().printResult()

