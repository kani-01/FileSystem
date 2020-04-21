# -*- coding: utf-8 -*-
"""
Created on Mon Apr 20 15:33:03 2020

@author: Srini Kani
"""

'''
The file system consists of Nodes -> of File Structure.
The File Node Structure may be a file or a directory
The Nodes contain two data: 
    datatype whether it is a file or directory 
    contents -> File -> String type, Directory -> DefaultDictionary datatype
    
Do :
    List Files/Directories
    Make Directories
    Add data/content to existing File
    Retrieve and display data from a File

'''

from collections import defaultdict

class FileNode():
    def __init__(self,filetype):
        self.filetype = filetype
        if self.filetype == "f":
            self.content = ""
        else: #elif self.filetype == "d":
            self.content = defaultdict()
            
            
class FileSystem():
    def __init__(self):
        self.root = FileNode("d")
        self.root.content["/"] = FileNode("d")
            
    def mkdir(self,path):        
        current = self.root.content["/"]
        print(current)
        
        path = path.strip("/").split("/")
        for x in path:
            #print(x)
            if x not in current.content:
                current.content[x] = FileNode("d")
            current = current.content[x]
         
    def ls(self,path):

        current = self.root.content["/"]
        if path == "/":
            result = list(current.content.keys())
            return sorted(result)
        path = path.strip("/").split("/")
        for x in path:
            if x in current.content:
                current = current.content[x]
            else:
                return "Path not found" #-1    
        if current.filetype == "f":
            return [path[-1]]
        else:
            res = list(current.content.keys())
            res.sort()
            return res
            #return sorted(current.content.keys())
         
    def readContentFromFile(self,path):
        current = self.root.content["/"]
        path = path.strip("/").split("/")
        for p in path[:-1]:
            current = current.content[p]
        return current.content[path[-1]].content

    
    def addContentToFile(self, filePath, contents):
        current = self.root.content["/"]
        path = filePath.strip("/").split("/")
        for p in path[:-1]:
            current = current.content[p]
        if path[-1] not in current.content:
            current.content[path[-1]] = FileNode("f")
        curr = current.content[path[-1]]
        curr.content += contents
        
            
            
F = FileSystem()
print(F.ls("/"))
print(F.mkdir("/a"))
print(F.mkdir("/a/p"))
print(F.mkdir("/a/w"))
print(F.mkdir("/a/b/c"))
print(F.ls("/"))
print(F.ls("/a"))
print(F.ls("/a/b"))
print(F.addContentToFile("/a/b/c/d","hello"))
print(F.ls("/a/b/c/d"))
print(F.readContentFromFile("/a/b/c/d"))         

'''    
F = FileSystem()
print(F.ls("/"))
print(F.mkdir("/a"))
print(F.mkdir("/a/p"))
print(F.mkdir("/a/w"))
print(F.mkdir("/a/b/c/d"))
print(F.ls("/a"))
print(F.ls("/a/b/h"))
#print(F.ls("/a"))
'''
