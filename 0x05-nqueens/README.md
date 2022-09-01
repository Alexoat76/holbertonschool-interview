<p align="center">
<img src="https://img.shields.io/badge/LINUX-darkgreen.svg"/>
<img src="https://img.shields.io/badge/Shell-ligthgreen.svg"/>
<img src="https://img.shields.io/badge/Vim-green.svg"/>
<img src="https://img.shields.io/badge/Python-blue.svg"/>
<img src="https://img.shields.io/badge/Markdown-black.svg"/><br>	
</p>

# 0x05. N Queens

This task consist in Create a *`Program`* that solves the N queens problems. Using Python language.

<p align="center">
  <img width="240"  
        src="https://upload.wikimedia.org/wikipedia/commons/1/1f/Eight-queens-animation.gif?20070625172331"
  >
</p>

# Getting Started :running:	
<div style="text-align: justify">

## Table of Contents
* [Resources](#resources-books)
* [Requirements](#requirements)
* [Files](#files-file_folder)
* [Tasks](#tasks)
* [Credits](#credits)

## Resources :books:
Read or watch:
	
[![M](https://upload.wikimedia.org/wikipedia/commons/thumb/2/2f/Google_2015_logo.svg/80px-Google_2015_logo.svg.png)](https://www.google.com/search?q=n+queens+problem+python&oq=N+Queens&aqs=chrome.5.0i512l10.3281j0j15&sourceid=chrome&ie=UTF-8)

[![M](https://upload.wikimedia.org/wikipedia/commons/thumb/e/e1/Logo_of_YouTube_%282015-2017%29.svg/70px-Logo_of_YouTube_%282015-2017%29.svg.png)](https://www.youtube.com/results?search_query=n+queens+problem+python)

- **[Queen](https://intranet.hbtn.io/rltoken/u80efQj5HUl9-FwkzWieCA)** 
- **[Backtracking](https://intranet.hbtn.io/rltoken/OjIVuPYh-rEjUHc7crQ5lw)**

## Requirements
### General
- Allowed editors:  *` vi `* ,  *` vim `* ,  *` emacs `* 
- All files will be interpreted/compiled on Ubuntu 14.04 LTS using  *` python3 `*  (version 3.4.3)
- All files should end with a new line
- The first line of all your files should be exactly  *` #!/usr/bin/python3 `* 
- A  *` README.md `*  file, at the root of the folder of the project, is mandatory
- The code should use the  *` PEP 8 `*  style (version 1.7.x)
- All files must be executable

### Installation :computer:
	
- Clone this repository: `https://github.com/Alexoat76/holbertonschool-interview.git`	
- Access to directory: `cd 0x05-nqueens`
- `Compile` accord to `instructions` of each task.

## Files :file_folder:

## Tasks

+ [x] 0\. **0. N queens**

+ **[0-nqueens.py](./0-nqueens.py)**

The *`N queens puzzle`* is the challenge of placing `N` non-attacking queens on an `N×N` chessboard.Write a program that solves the *`N queens`* problem.
* Usage:  *` nqueens N `* 
	* If the user called the program with the wrong number of arguments, print  *` Usage: nqueens N `* , followed by a new line, and exit with the status  *` 1 `* 

* where N must be an integer greater or equal to  *` 4 `* 
	* If N is not an integer, print  *` N must be a number `* , followed by a new line, and exit with the status  *` 1 `* 
	* If N is smaller than  *` 4 `* , print  *` N must be at least 4 `* , followed by a new line, and exit with the status  *` 1 `* 

* The program should print every possible solution to the problem
	* One solution per line
	* Format: see example
	* You don’t have to print the solutions in a specific order

* You are only allowed to import the  *` sys `*  module

**`Don't forget to read:`**  
- **[Queen](https://intranet.hbtn.io/rltoken/u80efQj5HUl9-FwkzWieCA)** 
- **[Backtracking](https://intranet.hbtn.io/rltoken/OjIVuPYh-rEjUHc7crQ5lw)**

```bash
$ ./0-nqueens.py 4
[[0, 1], [1, 3], [2, 0], [3, 2]]
[[0, 2], [1, 0], [2, 3], [3, 1]]
$ ./0-nqueens.py 6
[[0, 1], [1, 3], [2, 5], [3, 0], [4, 2], [5, 4]]
[[0, 2], [1, 5], [2, 1], [3, 4], [4, 0], [5, 3]]
[[0, 3], [1, 0], [2, 4], [3, 1], [4, 5], [5, 2]]
[[0, 4], [1, 2], [2, 0], [3, 5], [4, 3], [5, 1]]
$ 
```

---

## Credits

## Author(s):blue_book:

Work is owned and maintained by 
	**`Alex Orland Arévalo Tribaldos`**  and credits for `group projects` are displayed in the respective `README.md` files.

<3915@holbertonstudents.com>
	
[![M](https://upload.wikimedia.org/wikipedia/commons/thumb/9/91/Octicons-mark-github.svg/25px-Octicons-mark-github.svg.png)](https://github.com/Alexoat76)
[![M](https://upload.wikimedia.org/wikipedia/fr/thumb/c/c8/Twitter_Bird.svg/25px-Twitter_Bird.svg.png)](https://twitter.com/aoarevalot)
[![M](https://upload.wikimedia.org/wikipedia/commons/thumb/c/ca/LinkedIn_logo_initials.png/25px-LinkedIn_logo_initials.png)](https://www.linkedin.com/in/Alexoat76/)

## Acknowledgments :mega: 

### **`Holberton School`** (*providing guidance*)
	
This program was written as part of the curriculum for Holberton School.
Holberton School is a campus-based full-stack software engineering program
that prepares students for careers in the tech industry using project-based
peer learning. For more information,  please visit [this link](https://www.holbertonschool.com/).
![Brand](https://assets.website-files.com/6105315644a26f77912a1ada/610540e8b4cd6969794fe673_Holberton_School_logo-04-04.svg)
