# Mission 6 — Git and GitHub

## 1. Task / objective
Understand version control, stage and commit changes, create a branch, open a Pull Request and explain the collaboration workflow.

## 2. Work completed
- Practised Git workflow (status, add, commit, log)
- Created the `update-about` branch
- Added a "My Learning" section to the root README
- Pushed the branch to GitHub
- Created a Pull Request from `update-about` into `main`
- Built a Git command glossary

## 3. Commands / tools used

| Command | Purpose |
|---------|---------|
| `git status` | Shows which files are modified, staged or untracked |
| `git add <file>` | Stages a specific file for the next commit |
| `git commit -m "message"` | Creates a commit with a message describing the changes |
| `git log --oneline` | Shows a short summary of recent commits |
| `git branch update-about` | Creates a new branch called update-about |
| `git checkout update-about` | Switches to the update-about branch |
| `git push -u origin update-about` | Pushes the new branch to GitHub |
| `git checkout main` | Switches back to the main branch |
| `git pull origin main` | Downloads the latest changes from GitHub to local |

## 4. My understanding

### Task 6.1 — Basic Git workflow

| Git operation | What it does in my own words |
|--------------|------------------------------|
| Check repository status | `git status` shows me what files I have changed, what is ready to be committed, and what is not tracked yet |
| Stage selected changes | `git add` moves specific files to a "staging area" — like putting items in a box before shipping |
| Create a commit | `git commit` takes everything in the staging area and saves it as a permanent snapshot with a message |
| View commit history | `git log` shows all past commits with their messages, dates and IDs so I can see what was done |

**Difference between staging and committing:** Staging (`git add`) is like selecting which files to include. Committing (`git commit`) is like taking a photo of those selected files and saving it permanently. I can stage some files and leave others out of the commit.

### Task 6.2 — Creating and using a branch

I created a branch called `update-about`, added a "My Learning" section to the root README, committed it and pushed the branch to GitHub.

### Task 6.3 — Pull Request

I opened a Pull Request on GitHub to merge `update-about` into `main`. The PR showed the exact lines I added to the README. This lets others review my changes before they go into the main version.

**What is a branch?** A branch is like a copy of the project where I can make changes without affecting the main version. If the changes are good, I can merge them back.

**What is a Pull Request?** A Pull Request is a way to ask others to review my branch changes before merging them into main. It shows exactly what was added, removed or changed. This is useful when multiple people work on the same project because it prevents breaking the main code.

### Task 6.4 — Git command glossary

| Git operation | One-line explanation |
|--------------|---------------------|
| `git init` | Creates a new Git repository in the current folder |
| `git status` | Shows which files have been changed or staged |
| `git add` | Stages files so they are included in the next commit |
| `git commit` | Saves a snapshot of staged changes with a message |
| `git log` | Shows the history of all past commits |
| `git branch` | Creates a new branch or lists existing branches |
| `git checkout` | Switches to a different branch |
| `git push` | Uploads local commits to the remote GitHub repository |
| `git pull` | Downloads and applies remote changes to the local repository |

## 5. Difficulties faced
I was unsure about the difference between `git add` and `git commit` at first — they felt like the same thing.

## 6. How I resolved them
After practising, I understood that `add` is selecting files and `commit` is saving them. It is a two-step process so I have control over what goes into each commit.

## 7. Evidence / files
- `update-about` branch visible on GitHub
- Pull Request created on GitHub
- This README with all explanations and glossary

## 8. Commit details
- Commit message: **"Complete Git and GitHub collaboration mission"**
- Pushed to GitHub and verified.
- The Pull Request and branch activity are visible on the GitHub repository.
