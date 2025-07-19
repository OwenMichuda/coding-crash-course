# Python Basics

I already know you're going to know most of this, but we have to start somewhere so why not from the beginning? 

## Concepts to Cover
1. What even is coding?
2. Print
3. Variables
4. Data types
5. User Input
6. Math
7. Comparison Operators

## Coding

You know that Python is a programming language, but what does that even mean? What does a programming language do?

A programming language is a set of rules for writing instructions that a computer can follow. It's how we "talk" to the computer to make it do things like math, move files, or show us things on screen. We write down instructions in a way that's digestable to us (Python), and somehow the computer is able to understand these instructions and perform the described actions.

But computers aren't reading Python files, the language on its own makes no sense to a computer. A computer needs its instructions in *Machine Code*. Machine Code is literally just a bunch of 1's and 0's that represent binary instructions for our computer's processing unit... not very readable to humans.

So we have two extremes. We have a *high-level language* like Python, that's "easily" readable to human's, and the ultimate *low-level language* of machine code. You'll often hear about how high-level or low-level a language is, and this is what it refers to: how far displaced you are from the most granular way (1's and 0's) of delivering instructions to a computer. So with a low-level language, you have much finer control over what you want your computer, but comes at the cost of more complexity. How you want to manage memory is an example of something you'll have to think about with a low-level language. We're sticking to Python, a high-level language, which handles memory management for us. Super convenient! But some coding purists will scoff.

Ok but how are we getting from Python code to 1's and 0's our computer can read?

The Python Interpreter! We don't need to know the details of how the interpreter works, but know that it's an application that will read our Python code line-by-line and translate it into machine code for our computer (with a few steps in between).

(Other languages might use a compiler instead of an interpreter. They serve similar purposes, but compiler's convert all of the high-level code into machine code at once, compared to line-by-line with interpreters.)

So when we write Python code, we’re writing instructions that are friendly to us, and we rely on the interpreter to bridge the gap between our human-readable logic and the computer’s low-level execution. A lot of details were left out, but this is the general gist :)

One last quick note on terminals (aka command line, consoles, etc). This is how we actually pass the instruction to our computer. You're probably reading this text on an IDE (integrated development environment), which is really just a fancy way to edit files. But once we want actually execute code, we need to use the terminal to pass the instruction. Luckily for us, our IDE often has ways to use the terminal directly in a more user-friendly manner. For example, in the project tree, right-click on 001-introduction/birdbrain.py and hit Run **Python File in Terminal**. You'll see two arguments were passed to the terminal: the file path for what interpreter to use (should end in python), and the file to execute. And on the next line, the output from our program. This will be our main way of executing code.
