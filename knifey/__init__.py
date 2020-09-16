import collections
import re
import subprocess

class PreCommand():
    def __init__(self, command):
        self.command = command
        self.mustSearch = False
        self.searchTerm = ""
    
    def pipe(self, toPipe):
        self.command.append(" | ")
        self.command.append(toPipe)

    def find(self, string):
        self.mustSearch = True
        self.searchTerm = string
