# Mission 4 — How programs run

## 1. Task / objective
Create and run a simple Python program. Compare how compilers and interpreters translate and execute programs.

## 2. Work completed
- Created `hello.py` and ran it using Python 3
- Compared compilers and interpreters in a table
- Wrote an explanation in my own words

## 3. Commands / tools used

| Command | Purpose |
|---------|---------|
| `python3 hello.py` | Runs the Python script using the Python 3 interpreter |
| Text editor | Used to write the hello.py file |

## 4. My understanding

### Task 4.1 — Create and run a Python program

I created a file called `hello.py` with this code:

```python
print("Hello from Python")
```

I ran it using:
```bash
python3 hello.py
```

Output:
```
Hello from Python
```

The message appeared correctly on screen.

### Task 4.2 — Compiler vs interpreter comparison

| Point | Compiler | Interpreter |
|-------|----------|-------------|
| When translation / execution happens | Translates the entire source code into machine code before the program runs | Reads and executes the code line by line at runtime |
| Typical output | Produces a separate executable file (like `.exe`) | No separate file — runs the code directly |
| One example | C language uses `gcc` compiler | Python uses the Python interpreter |
| One advantage | Compiled programs run faster because translation is already done | Easier to test and debug because you can run code immediately |

**My explanation:**

A compiler takes the whole source code and translates it into machine code all at once before the program runs. The result is a separate file that the computer can execute directly, which makes it fast. An interpreter, on the other hand, reads the code line by line and executes each line immediately without creating a separate file. This makes it easier to test small changes quickly. Python uses an interpreter, which is why I can just type `python3 hello.py` and see the result right away. Some languages like Java actually use both — they compile to an intermediate form and then interpret it.

## 5. Difficulties faced
No major difficulties.

## 6. How I resolved them
Not applicable.

## 7. Evidence / files
- `hello.py` — working Python program
- This README with comparison table and explanation

## 8. Commit details
- Commit message: **"Compare compilers and interpreters"**
- Pushed to GitHub and verified.
