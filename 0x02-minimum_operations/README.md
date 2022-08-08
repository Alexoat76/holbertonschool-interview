<p align="center">
<img src="https://img.shields.io/badge/LINUX-darkgreen.svg"/>
<img src="https://img.shields.io/badge/Shell-ligthgreen.svg"/>
<img src="https://img.shields.io/badge/Vim-green.svg"/>
<img src="https://img.shields.io/badge/Python-blue.svg"/>
<img src="https://img.shields.io/badge/Markdown-black.svg"/><br>	
</p>

# 0x02. Minimum Operations

This task consist in Create a function that calculates the fewest number of operations needed to result in exactly *` n H `* characters in a file. Using Python language.

<p align="center">
  <img width="350"  
        src="https://cdn.sanity.io/images/oaglaatp/production/a697fedfc98c7c8f5a8063a3461e53e1350a6acb-1200x800.png?w=1200"
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
	
[![M](https://upload.wikimedia.org/wikipedia/commons/thumb/2/2f/Google_2015_logo.svg/80px-Google_2015_logo.svg.png)](https://www.google.com/search?q=method+that+calculates+the+fewest+number+of+operations+needed+to+result+in+exactly+n+h+characters&oq=&aqs=chrome.0.69i59i450l8.536578941j0j15&sourceid=chrome&ie=UTF-8)

[![M](https://upload.wikimedia.org/wikipedia/commons/thumb/e/e1/Logo_of_YouTube_%282015-2017%29.svg/70px-Logo_of_YouTube_%282015-2017%29.svg.png)](https://www.youtube.com/watch?v=03ZepmoVJGI)

## Requirements
### General
- Allowed editors:  *` vi `* ,  *` vim `* ,  *` emacs `*
- All files will be interpreted/compiled on Ubuntu 14.04 LTS using  *` python3 `*  (version 3.4.3)
- All files should end with a new line
- The first line of all your files should be exactly  *` #!/usr/bin/python3 `* 
- A  *` README.md `*  file, at the root of the folder of the project, is mandatory
- The code should be documented
- The code should use the  *` PEP 8 `*  style (version 1.7.x)
- All files must be executable

### Installation :computer:
	
- Clone this repository: `https://github.com/Alexoat76/holbertonschool-interview.git`	
- Access to directory: `cd 0x02-minimum_operations`
- `Compile` accord to `instructions` of each task.

## Files :file_folder:

## Test :heavy_check_mark:

+ **[main_0.py](./main_0.py)**  *`Provided by Holberton School`*.

---

## Tasks

+ [x] 0\. **minoperations.py**

+ **[0-minoperations.py](./0-minoperations.py)**

In a text file, there is a single character   *` H `*  . Your text editor can execute only two operations in this file:  *` Copy All `*   and   *` Paste `*  . Given a number   *` n `*, 
write a method that calculates the fewest number of operations needed to result in exactly   *` n `*   *` H `*   characters in the file.
* Prototype:  *` def minOperations(n) `* 
* Returns an integer
* If  *` n `*  is impossible to achieve, return  *` 0 `* 

Example:

 *` n = 9 `* 
 *` H `*  =>  *` Copy All `*  => *` Paste `*   =>  *` HH `*  =>  *` Paste `*  =>  *` HHH `*  =>  *` Copy All `*  => *` Paste `*  =>  *` HHHHHH `*   =>  *` Paste `*  => *` HHHHHHHHH `* 

Number of operations:   *` 6 `*
 
```bash
$ cat 0-main.py
#!/usr/bin/python3
"""
Main file for testing
"""

minOperations = __import__('0-minoperations').minOperations

n = 4
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))

n = 12
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))

carrie@ubuntu:~/0x02-minoperations$

```

```bash
$ ./0-main.py
Min number of operations to reach 4 characters: 4
Min number of operations to reach 12 characters: 7
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
