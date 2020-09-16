import re
import subprocess

class Command:
    def __init__(self, command):
        self.command = command
        self.mustSearch = False
        self.searchTerm = ""
        self.result = ""
    def execute(self):
        self.result = subprocess.run(self.command, shell=True, capture_output=True).stdout.decode("utf-8")
        return self

    def pipe(self, toPipe):
        newCommand = self.command
        newCommand += " | "
        newCommand += toPipe
        return Command(newCommand)

    def find(self, pattern):
        result = []
        for line in self.result.split("\n"):
            if re.search(pattern, line):
                result.append(line)
        return result

    def printResult(self):
        print(self.result)

    def getResult(self):
        return self.result

    
                

