import collections

class PreCommand():
    def __init__(self, command):
        self.command = command
    
    def pipe(self, toPipe):
        self.command.append(" | ")
        self.command.append(toPipe)
