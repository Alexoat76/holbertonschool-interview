<p align="center">
<img src="https://img.shields.io/badge/LINUX-darkgreen.svg"/>
<img src="https://img.shields.io/badge/Shell-ligthgreen.svg"/>
<img src="https://img.shields.io/badge/Vim-green.svg"/>
<img src="https://img.shields.io/badge/Python-blue.svg"/>
<img src="https://img.shields.io/badge/Markdown-black.svg"/><br>	
</p>

# 0x08. Making Change

Given a pile of *` coins `* of different values, determine the *` fewest `* number of coins needed to meet a given amount **` total`**. Using Python language.

<p align="center">
  <img width="260"
        src="https://thumbs.gfycat.com/FailingMeekArmyant-size_restricted.gif"
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
	
[![M](https://upload.wikimedia.org/wikipedia/commons/thumb/2/2f/Google_2015_logo.svg/80px-Google_2015_logo.svg.png)](https://www.google.com/search?q=making+change+problem+in+python&oq=Making+Change+problem+&aqs=chrome.3.69i57j0i512l9.7313j0j15&sourceid=chrome&ie=UTF-8)

[![M](https://upload.wikimedia.org/wikipedia/commons/thumb/e/e1/Logo_of_YouTube_%282015-2017%29.svg/70px-Logo_of_YouTube_%282015-2017%29.svg.png)](https://www.youtube.com/results?search_query=making+change+problem+in+python)

## Requirements
### General
- Allowed editors:  *` vi `* ,  *` vim `* ,  *` emacs `* 
- All files will be interpreted/compiled on **` Ubuntu 14.04 LTS `** using  *` python3 `*  (version 3.4.3)
- All files should end with a new line
- The first line of all your files should be exactly  *` #!/usr/bin/python3 `* 
- A  *` README.md `*  file, at the root of the folder of the project, is mandatory
- The code should use the  *` PEP 8 `*  style (version 1.7.x)
- All files must be executable

### Installation :computer:
	
- Clone this repository: `https://github.com/Alexoat76/holbertonschool-interview.git`	
- Access to directory: `cd 0x08-making_change`
- `Compile` accord to `instructions` of each task.

## Files :file_folder:

## Test :heavy_check_mark:

+ **[0-main.py](./0-main.py)**  *`Provided by Holberton School`*.

---

## Tasks

+ [x] 0\. **Change comes from within**

+ **[0-making_change.py](./0-making_change.py)**

Given a pile of coins of different values, determine the fewest number of coins needed to meet a given amount *` total `*.
* Prototype:  *` def makeChange(coins, total) `*
* Return: fewest number of coins needed to meet  *` total `* 
	* If  *` total `*  is  *` 0 `*  or less, return  *` 0 `* 
	* If  *` total `*  cannot be met by any number of coins you have, return  *` -1 `* 
*  *` coins `*  is a list of the values of the coins in your possession
* The value of a coin will always be an integer greater than  *` 0 `* 
* You can assume you have an infinite number of each denomination of coin in the list
* Your solution’s runtime will be evaluated in this task

```python3
#!/usr/bin/python3
"""
Main file for testing
"""

makeChange = __import__('0-making_change').makeChange

print(makeChange([1, 2, 25], 37))

print(makeChange([1256, 54, 48, 16, 102], 1453))

carrie@ubuntu:~/0x08-making_change$

```
```bash
$ ./0-main.py
7
-1
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
