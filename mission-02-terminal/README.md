# Mission 2 — Become comfortable with the Terminal

## 1. Task / objective
Use the Terminal to inspect folders, create and manage files, understand flags and pipes, and explain package managers.

## 2. Work completed
- Practised basic Terminal operations inside the assignment repo
- Created the `terminal-practice/` folder with practice files
- Learned about flags, pipes and package managers
- Documented all commands and observations

## 3. Commands / tools used

| Command | Purpose |
|---------|---------|
| `pwd` | Prints the full path of the current working directory |
| `ls` | Lists files and folders in the current directory |
| `ls -la` | Lists all files (including hidden) in detailed format |
| `ls -lah` | Same as above but with human-readable file sizes |
| `cd ..` | Moves to the parent directory |
| `cd terminal-practice` | Moves into the terminal-practice folder |
| `mkdir` | Creates a new directory |
| `touch` | Creates a new empty file |
| `cp` | Copies a file |
| `mv` | Moves or renames a file |
| `cat` | Displays the contents of a file |
| `echo "text" > file.txt` | Writes text to a file (replaces contents) |
| `echo "text" >> file.txt` | Appends text to a file (adds to the end) |
| `ls -la \| head -5` | Pipes the directory listing and shows only the first 5 lines |
| `brew --version` | Checks the version of Homebrew package manager |
| `brew list` | Shows packages installed through Homebrew |

## 4. My understanding

### Task 2.1 — Basic Terminal operations

| Operation | Command | What I observed |
|-----------|---------|----------------|
| Current-directory display | `pwd` | It showed the full path like `/Users/[redacted]/Documents/.../digital-detective-8414` |
| Directory listing | `ls` | It listed all folders and files in the current location |
| Detailed listing | `ls -la` | It showed permissions, owner, file size, date and hidden files |
| Change directory | `cd ..` | My location moved one folder up. `pwd` confirmed the change |
| Create directory | `mkdir terminal-practice` | A new empty folder was created |
| Create empty file | `touch notes.txt` | An empty file appeared in the folder |
| Copy file | `cp notes.txt notes-backup.txt` | A second file appeared with the same content |
| Move / rename file | `mv notes-backup.txt notes-copy.txt` | The file was renamed. The old name disappeared |
| Display file contents | `cat notes.txt` | It printed the text inside the file to the screen |

### Task 2.2 — File changes practice

I worked inside the `terminal-practice/` folder:
1. Created `practice.txt` using `touch practice.txt`
2. Added first line: `echo "This is line one" > practice.txt`
3. Added second line: `echo "This is line two" >> practice.txt`
4. Checked contents: `cat practice.txt` — both lines were there
5. Made backup: `cp practice.txt practice-backup.txt`
6. Renamed backup: `mv practice-backup.txt practice-renamed.txt`

**Answers:**
- **Replacing vs appending:** Using `>` replaces everything in the file. Using `>>` adds text at the end without removing what was already there.
- **Copying vs moving:** Copying (`cp`) makes a duplicate — both files exist. Moving (`mv`) changes the location or name — the original is gone.
- **Current-directory display:** `pwd` tells me exactly where I am in the file system so I do not get lost.
- **Directory listing:** `ls` is useful to see what files and folders exist before I work with them.

### Task 2.3 — Flags and pipes

- `ls` shows just file names
- `ls -l` adds permissions, size and date
- `ls -la` also shows hidden files (starting with `.`)
- `ls -lah` makes file sizes human-readable (K, M, G instead of raw bytes)

**Pipe example:** `ls -la | head -5`
- The pipe `|` takes the output of the command on the left (`ls -la`) and sends it as input to the command on the right (`head -5`). So instead of showing all files, it only shows the first 5 lines.

### Task 2.4 — Package managers

Homebrew is installed on my Mac. I checked its version using `brew --version` and listed installed packages using `brew list`.

**Why package managers are useful:** A package manager makes it easy to install, update and remove software from the Terminal with just one command. Without it, I would have to manually download files from websites, figure out where to put them, and handle updates myself. It also manages dependencies — if a program needs another library, the package manager installs that too.

## 5. Difficulties faced
At first I confused `>` and `>>`. I accidentally replaced my file contents when I meant to add text.

## 6. How I resolved them
I re-read the difference — `>` overwrites and `>>` appends. After that I was careful to use `>>` when I wanted to add a second line.

## 7. Evidence / files
- `terminal-practice/practice.txt` — file with two lines of text
- `terminal-practice/notes.txt` — empty practice file
- `terminal-practice/notes-copy.txt` — renamed backup copy
- This README with all tables and explanations

## 8. Commit details
- Commit message: **"Complete Terminal and file management mission"**
- Pushed to GitHub and verified.
