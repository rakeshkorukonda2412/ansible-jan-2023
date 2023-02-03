#!/usr/bin/python3

class Hello:

  def __init__(self):
      print("Inside constructor ...")

  def sayHelloPublicFunction(self,msg):
      print(msg)

  def _protectedFunction(self):
      print("Protected function")

  def __privateFunction(self):
      print("Private function")

if __name__ == "__main__":
   hello = Hello()
   hello.sayHelloPublicFunction("Hello World!")
   hello._protectedFunction()
   hello._privateFunction()
