import re
import subprocess
from typing import List
class Command:
    def __init__(self, command: str) -> None: 
        self.command: str = command
        self.result: str = ""
    def execute(self) -> 'Command':
        self.result = subprocess.run(self.command, shell=True, capture_output=True).stdout.decode("utf-8")
        return self

    def pipe(self, toPipe: str) -> 'Command':
        newCommand: str = self.command
        newCommand += " | "
        newCommand += toPipe
        return Command(newCommand)

    def find(self, pattern: str) -> List[str]:
        result: List[str] = []
        for line in self.result.split("\n"):
            if re.search(pattern, line):
                result.append(line)
        return result

    def printResult(self) -> None:
        print(self.result)

    def getResult(self) -> str:
        return self.result

    
                

