#!/usr/bin/env phyton3
#-*- coding:utf-8 -*-

class Class_example:
    def __init__(self) -> None:
        self.data = 0

    def func(self):
        pass
    
def main():
    try:
        class_name = Class_example()
        class_name.func() 
    except :
        pass

if __name__=="__main__":
    main()
    