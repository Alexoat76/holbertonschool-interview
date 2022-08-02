<p align="center">
<img src="https://img.shields.io/badge/LINUX-darkgreen.svg"/>
<img src="https://img.shields.io/badge/Shell-ligthgreen.svg"/>
<img src="https://img.shields.io/badge/Vim-green.svg"/>
<img src="https://img.shields.io/badge/Python-blue.svg"/>
<img src="https://img.shields.io/badge/Markdown-black.svg"/><br>	
</p>

---
# 0x00. Pascal's Triangle

This task consist in Create a function that determines if all the boxes can be opened. Using Python language implementation.

<p align="center">
  <img width="220"  
        src="https://media4.giphy.com/media/3orif74MzRbKQeJiQE/giphy.gif?cid=ecf05e4744ao5uo4tj521e1lc1ljfi9oltj8oj72jayma0we&rid=giphy.gif&ct=g"
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
	
[![M](https://upload.wikimedia.org/wikipedia/commons/thumb/2/2f/Google_2015_logo.svg/80px-Google_2015_logo.svg.png)](https://www.google.com/search?q=pascal+triangle+in+python&oq=Pascal+trian&aqs=chrome.6.69i57j0i512l9.7223j0j15&sourceid=chrome&ie=UTF-8)

[![M](https://upload.wikimedia.org/wikipedia/commons/thumb/e/e1/Logo_of_YouTube_%282015-2017%29.svg/70px-Logo_of_YouTube_%282015-2017%29.svg.png)](https://www.youtube.com/results?search_query=pascal%27s+triangle+in+python)

## Requirements
### General
- Allowed editors: `vi`, `vim`, `emacs` 
- All -files will be interpreted/compiled on Ubuntu 20.04 LTS using `python3`.
- All -files should end with a new line
- The first line of all -files should be exactly `#!/usr/bin/python3` 
- Libraries imported in the Python files must be organized in alphabetical order
- A `README.md` file, at the root of the folder of the project, is mandatory
- Your code should use the `PEP 8` style
- All your files must be executable
- The length of your files will be tested using `wc`

### Installation :computer:
	
- Clone this repository: `https://github.com/Alexoat76/holbertonschool-interview.git`	
- Access to directory: `cd 0x00-pascal_triangle`
- `Compile` accord to `instructions` of each task.

## Files :file_folder:

## Test :heavy_check_mark:

+ **[0-main.py](./0-main.py)**  *`Provided by Holberton School`*.

---

## Tasks

+ [x] 0\. **Pascal's Triangle**

+ **[0-pascal_triangle.py](./0-pascal_triangle.py)**

Create a function  *`def pascal_triangle(n):`*   that returns a list of lists of integers representing the Pascal’s triangle of   *` n `*  :

* Returns an empty list if  *` n <= 0 `* 
* You can assume  *` n `*  will be always an integer

```bash
$ cat 0-main.py
#!/usr/bin/python3
"""
0-main
"""
pascal_triangle = __import__('0-pascal_triangle').pascal_triangle

def print_triangle(triangle):
    """
    Print the triangle
    """
    for row in triangle:
        print("[{}]".format(",".join([str(x) for x in row])))


if __name__ == "__main__":
    print_triangle(pascal_triangle(5))

$
$ 
$ ./0-main.py
[1]
[1,1]
[1,2,1]
[1,3,3,1]
[1,4,6,4,1]
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
