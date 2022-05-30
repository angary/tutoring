# Tutoring Resources

Welcome to the repository for my UNSW tutoring notes.

You can find the code it's week's folder, and the slides from the links below.

| Week       | Content         | Slides                                                                                                       |
| ---------- | --------------- | ------------------------------------------------------------------------------------------------------------ |
| [01](wk01) | JavaScript, Git | [link](https://docs.google.com/presentation/d/1v8AWey1W6xopu4vZoj_QYqUxwHd0YHL2bpJPt4xqsS4/edit?usp=sharing) |

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

From there, (in the WSL / unix terminal) you can run the following commands in the terminal to install git and node

```sh
sudo apt-get update # Update package information so you get the latest versions
sudo apt-get git
sudo apt-get node
```

If you are on MacOS, install [homebrew](https://brew.sh/), and use that to install git and node by running the following commands.

```sh
brew install git
brew install node
```

### Setup FAQ

**What text editor are you using?**

- I use Visual Studio Code ([VSCode](https://code.visualstudio.com/)) with a theme and the [VIM extension](https://marketplace.visualstudio.com/items?itemName=vscodevim.vim)

**How do you get those colours / autocomplete / git details etc in your terminal?**

- My shell (program that the terminal runs) is ZSH and I use plugins such as
  - git
  - zsh-autosuggestions
  - zsh-syntax-highlighting
  - exa (for coloured `ls` and file icons)
