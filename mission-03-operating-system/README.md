# Mission 3 — Understand the operating system

## 1. Task / objective
Explore the operating system, running processes, storage, paths and file permissions, and describe the OS responsibilities.

## 2. Work completed
- Explored system information using Terminal commands
- Observed running processes and identified PIDs
- Understood absolute vs relative paths
- Checked file permissions
- Documented OS responsibilities

## 3. Commands / tools used

| Command | Purpose |
|---------|---------|
| `uname -a` | Shows operating system name and version details |
| `sw_vers` | Shows macOS product name, version and build number |
| `whoami` | Shows the current user account name |
| `df -h` | Shows available and used disk storage in human-readable format |
| `top -l 1 \| head -15` | Shows a snapshot of system activity (CPU, memory usage) |
| `ps aux` | Lists all running processes with details |
| `pwd` | Shows the absolute path of current directory |
| `ls -l` | Shows file details including permissions |

## 4. My understanding

### Task 3.1 — Exploring the operating system

| Information explored | What it tells you | My observation (privacy-safe) |
|---------------------|-------------------|-------------------------------|
| Operating system details | The name, version and architecture of the OS | macOS, Darwin kernel, arm64 (Apple Silicon) |
| Current account identity | Which user is logged in | [redacted] |
| Available and used storage | How much space is free on the disk | 926 GB total, about 831 GB free |
| System activity snapshot | CPU usage, memory usage and running processes | Several background processes running, low CPU usage when idle |

### Task 3.2 — Understanding processes

A **process** is a program that is currently running on the computer. Every time I open an app or run a command, the OS creates a process for it.

The **PID (Process ID)** column is a unique number the OS gives to each running process. It helps the OS keep track of and manage each process separately.

**Two examples of processes on my computer:**
1. `Safari` — my web browser running in the background
2. `Terminal` — the terminal app I use to type commands

### Task 3.3 — Paths and permissions

**Absolute path** — the full path starting from the root `/`. It always points to the same location no matter where I am.
- Example: `/Users/[redacted]/Documents/digital-detective-8414/mission-03-operating-system`

**Relative path** — the path relative to where I currently am. It changes depending on my current directory.
- Example: `../mission-02-terminal` (goes up one folder then into mission-02)

**File permissions:**
When I ran `ls -l` on a file, I saw something like `-rw-r--r--`. This means:
- `r` (read) — the owner can read the file
- `w` (write) — the owner can edit the file
- The owner does not have `x` (execute) permission, so the file cannot be run as a script

### Task 3.4 — Operating system responsibilities

| OS responsibility | My explanation | Example |
|-------------------|---------------|---------|
| Process management | The OS starts, pauses, resumes and stops programs. It decides which process gets CPU time. | When I open Safari and VS Code together, the OS switches between them smoothly. |
| Memory management | The OS decides how much RAM each program gets and makes sure they do not interfere with each other. | If I open too many apps, the OS may slow things down or close background apps to free memory. |
| Device management | The OS communicates with hardware like keyboard, mouse and display through drivers. | When I plug in a USB drive, the OS detects it and makes it available. |
| File management | The OS organises files into folders, controls access and handles reading and writing to storage. | When I save a file in VS Code, the OS writes it to the correct location on the SSD. |
| User interface / shell | The OS provides a way for users to interact with the computer — either graphical (GUI) or text-based (Terminal). | I use Finder (GUI) to browse files and Terminal (CLI) to run commands. |
| Security and permissions | The OS controls who can access what files and what programs can do. | File permissions (`rwx`) prevent other users from editing my private files. |

## 5. Difficulties faced
I was confused about the difference between absolute and relative paths at first.

## 6. How I resolved them
I practised by using `pwd` to see my absolute path, then navigated using relative paths like `cd ..` and `cd mission-02-terminal` and checked `pwd` again each time. That made it click.

## 7. Evidence / files
- This README with all tables and explanations

## 8. Commit details
- Commit message: **"Document operating system and file management"**
- Pushed to GitHub and verified.
