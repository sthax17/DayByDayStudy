# -*- coding: utf-8 -*-
"""study0714.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1YiY3PAuY-dclN0H9ltJQHh2wYUCq8WWT
"""

import math

print(dir(math))


print(dir(help))
print(type(math))
print(type(help))


dir(math.degrees)
help(math.degrees)

dir(math.remainder)
help(math.remainder)

def fibonacci(n):
  if n == 1: 
    return 1
  if n == 2:
    return 1
  else:
    return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(1))
print(fibonacci(2))
print(fibonacci(3))
print(fibonacci(4))
print(fibonacci(5))

def factorial(n):
  if n == 0:
    return 1
  else:
    return n* factorial(n-1)
print(factorial(1))
print(factorial(2))
print(factorial(3))
print(factorial(4))
print(factorial(5))

def factorial(n):
  output = 1
  for i in range(1, n+1):
    output *= i
  return output

print(factorial(1))
print(factorial(2))
print(factorial(3))
print(factorial(4))
print(factorial(5))



def run_cmd_with_stack(stack, cmd):
    cmd_type = cmd[0]

    if cmd_type == "push":
        _, num = cmd
        stack.append(int(num))
    elif cmd_type == "pop":
        if len(stack) > 0:
            print(stack.pop())
        else:
            print(-1)
    elif cmd_type == "size":
        print(len(stack))
    elif cmd_type == "empty":
        if len(stack) > 0:
            print(0)
        else:
            print(1)

    elif cmd_type == "top":
        if len(stack) > 0:
            print(stack[-1])
        else:
            print(-1)

    return stack

stack = []

n = int(input())

for _ in range(n):

    stack = run_cmd_with_stack(stack, command)

class Stack:
    def __init__(self, n):
        self.stack = [None for _ in range(n)]
        self.stack_size = 0


     def push(self, num):
         # self.stack.append(int(num))
         self.stack[self.stack_size] = int(num)
         self.stack_size += 1


      def pop(self):
         if self.size() > 0:
             last_val = self.top()
             self.stack[self.stack_size - 1] = None
             self.stack_size -= 1

             return last_val

          return -1
           # 2)
           # last_val = self.top()
           # if last_val > 0:
           #     self.stack_size -= 1

           # return last_val


      def size(self):
          return self.stack_size


      def empty(self):
          if self.size() > 0:
             return 0

          return 1


          # return int(self.stack_size <= 0)


      def top(self):
          if self.stack_size > 0:
              return self.stack[self.stack_size - 1]

          return -1


def run_cmd_with_stack(my_stack, cmd):
    cmd_type = cmd[0]


    if cmd_type == "push":
        _, num = cmd  # num = cmd[1]
     my_stack.push(num)
    elif cmd_type == "pop":
        print(my_stack.pop())
    elif cmd_type == "size":
     print(my_stack.size())
    elif cmd_type == "empty":
        print(my_stack.empty())
    elif cmd_type == "top":
        print(my_stack.top())

    return my_stack

n = int(input())
my_stack = Stack(n)

for _ in range(n):
    # "push 2".split() => ["push", "2"]
    # "size".split() => ["size"]
    command = input().split()
    my_stack = run_cmd_with_stack(my_stack, command)

print(my_stack.stack)
print(f"stack_size: {my_stack.stack_size}")