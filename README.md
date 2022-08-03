# Tutoring Resources

Welcome to the repository for my UNSW tutoring notes.

You can find the code it's week's folder, and the slides from the links below.

| Week       | Content                               | Slides                                                                                                       |
| ---------- | ------------------------------------- | ------------------------------------------------------------------------------------------------------------ |
| [01](wk01) | JavaScript, Git                       | [link](https://docs.google.com/presentation/d/1v8AWey1W6xopu4vZoj_QYqUxwHd0YHL2bpJPt4xqsS4/edit?usp=sharing) |
| [02](wk02) | JavaScript, Code Style, Git           | [link](https://docs.google.com/presentation/d/1eRcaFwmqmUrdFqDYqexR8ihrizH1AhgKg2qb7naG-18/edit?usp=sharing) |
| [03](wk03) | Code Review, NPM, Testing             | [link](https://docs.google.com/presentation/d/1BU2BcO-AsAgYxjBks7Jqpb1nydWx4ukX6W-XDnx6XEM/edit?usp=sharing) |
| [04](wk04) | Teamwork, Typing, Linting             | [link](https://docs.google.com/presentation/d/1LrLAUkTdd_R3cq9Nzy7A-rSASAVydzgJl7kw3nKh0EI/edit?usp=sharing) |
| [05](wk05) | Express, HTTP, Functions              | [link](https://docs.google.com/presentation/d/1xc9vkwlYgjiGYHnS4OpNlVuuLaNiWadPOpM8o5RaPB0/edit?usp=sharing) |
| [07](wk07) | DRY, Exceptions, Interfaces           | [link](https://docs.google.com/presentation/d/1oUwYaCM8BlRfmtGpNAACIfwV78YJrQ2OMcTWabrZ8rI/edit?usp=sharing) |
| [08](wk08) | Coverage, State Diagrams              | [link](https://docs.google.com/presentation/d/1ltbTiOvcnnEAUbF-hC9IyR1jTOgGDxrDncItjV7L7No/edit?usp=sharing) |
| [09](wk09) | Requirements, User Stories, Use Cases | [link](https://docs.google.com/presentation/d/1eWw273x_9Ou0lGfpJlYkH9UMqeAtYaB-zIpnQ2naHO0/edit?usp=sharing) |
| [10](wk10) | Git, Complexity Analysis, Revision    | [link](https://docs.google.com/presentation/d/1SQmV2ViZQD8BQPNkzArYTW1n1HaOQggGYkmrK8_2-8w/edit?usp=sharing) |

Good luck for your studies!

## Miscellaneous

### Local Setup

I would highly recommend all students in this course setup a local development environment.
This course no longer has autotests / give (submissions are done through GitLab), hence there is no need to code on CSE machines.
If you are on Windows install and use [WSL](https://docs.microsoft.com/en-us/windows/wsl/install) (feel free to ask me / course forums / the CSESoc Discord on how to set this up).
This will allow you have a unix like environment within your operating system which is nice because

- it simulates the environment of CSE machines
- a lot of tooling / libraries may only be available for unix systems

and overall, it'll reduce the number of annoying dev related issues you may run into.

To get setup you'll need to install git and node by running the commands in the terminal:

**For WSL / UNIX**

```sh
sudo apt-get update # Update package information so you get the latest versions
sudo apt-get git
sudo apt-get node
```

**For MacOS**

Install [homebrew](https://brew.sh/) first (this is a package manager / MacOS's version of `apt` and you'll use this to install / update applications and utilities).

```sh
brew install git
brew install node
```

### Setup FAQ

**What text editor are you using?**

- I use Visual Studio Code ([VSCode](https://code.visualstudio.com/)) with atom one dark theme and the [VIM extension](https://marketplace.visualstudio.com/items?itemName=vscodevim.vim)

**How do you get those colours / autocomplete / git details etc in your terminal?**

- My shell (program that the terminal runs) is ZSH and I use plugins such as
  - git
  - zsh-autosuggestions
  - zsh-syntax-highlighting
  - exa (for coloured `ls` and file icons)
