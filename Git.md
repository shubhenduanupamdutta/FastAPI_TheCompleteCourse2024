# Git and GitHub

---

## What is Git?

---

- ### Git is a free and open source distributed version control system.
- ### It is designed to handle everything from small to very large projects with speed and efficiency.
- ### Allows team members to use same files by distributed branches/environments.

### Git Example:

- **Version 1**

```python
class MathFunctions:

    def addition(a + b):
        return a + b
```

- **Version 2**

```python
class MathFunctions:

    def addition(a, b):
        return a + b

    def subtraction(a, b):
        return a - b
```

- **Version 3**

```python
class MathFunctions:

    def addition(a, b):
        return a + b

    def subtraction(a, b):
        return a - b

    def multiplication(a, b):
        return a * b
```

**We started with our starting version (_Version 1_), one of our code that had just our class and the addition functionality created. We then committed our first version. Then we created a newer version of the `MathFunctions` class, which included the subtraction functionality. We then committed our second version. Finally, we created a newer version of the `MathFunctions` class, which included the multiplication functionality. We then committed our third version.**

**Using git we can easily switch between these versions, and also we can easily collaborate with other team members.**

**Git is distributed, which means that every developer has a copy of the repository on their local machine, and changes are synchronized between them.**

### Distributed Version Control System Example:

_Let's say we have our class `MathFunctions`, which now include `addition`, `subtraction` and `multiplication` functions. Suppose one of our team member **Bill** is working on a new enhancement to our class, which is to add `division` functionality. His team mate **Sarah** is working on her own feature to add the `power` functionality._

_Without Git, the only way Bill and Sarah can exchange code with one another is for them to send each other their code files. They would have to manually copy each other code and paste it into their own files. This is a very inefficient way to work, and it is very error-prone._

_With Git, Bill and Sarah can work on their own features in their own branches. When they are ready to share their code, they can merge their branches together. This is a much more efficient way to work, and it is much less error-prone._

---

### Recap:

- **Git allows us to track changes in our code.**
- **Git allows us to have a strong version control system.**
- **Git allows team members to use same files without needing to sync every time.**

---

## Git Basics

---

| Git Command                | Description                                                  |
| -------------------------- | ------------------------------------------------------------ |
| `git init`                 | Initializes a new Git repository.                            |
| `git add .`                | Adds all files in the current directory to the staging area. |
| `git commit -m "message"`  | Commits the files in the staging area with a message.        |
| `git checkout <commit #>`  | Checks out a specific commit.                                |
| `git log`                  | Shows a list of all previous commits.                        |
| `git checkout -b <branch>` | Creates a new branch and switches to it.                     |
| `git branch`               | Shows a list of all branches.                                |
| `git merge <branch>`       | Merges a branch into the current branch.                     |
| `git push`                 | Pushes changes to a remote repository.                       |
| `git pull`                 | Pulls changes from a remote repository.                      |

---

## What is GitHub?

- ### GitHub is a web-based platform that provides Git Repository Hosting services.
- ### It offers all of the distributed version control and source code management (SCM) functionality of Git as well as adding its own features.
- ### User friendly interface.
- ### Large development platform.

---

## Git vs GitHub

| Git                                  | GitHub                                                                            |
| ------------------------------------ | --------------------------------------------------------------------------------- |
| **Git is a version control system.** | **GitHub is a web-based platform that provides Git Repository Hosting services.** |
| **Git is a software.**               | **GitHub is a service.**                                                          |
| **Git is installed on your system.** | **GitHub is hosted on the web.**                                                  |

### Git Remote Commands:

| Git Command                   | Description                                      |
| ----------------------------- | ------------------------------------------------ |
| `git remote add origin <url>` | Adds a remote repository to your Git repository. |
| `git remote -v`               | Shows a list of all remote repositories.         |
| `git push origin <branch>`    | Pushes changes to a remote repository.           |
| `git pull origin <branch>`    | Pulls changes from a remote repository.          |
