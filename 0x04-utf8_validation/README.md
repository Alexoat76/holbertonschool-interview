<p align="center">
<img src="https://img.shields.io/badge/LINUX-darkgreen.svg"/>
<img src="https://img.shields.io/badge/Shell-ligthgreen.svg"/>
<img src="https://img.shields.io/badge/Vim-green.svg"/>
<img src="https://img.shields.io/badge/Python-blue.svg"/>
<img src="https://img.shields.io/badge/Markdown-black.svg"/><br>	
</p>

# 0x04. UTF-8 Validation

This task consist in Create a *`Script`* that determines if a given data set represents a valid **`UTF-8`** encoding. Using Python language.

<p align="center">
  <img width="360"  
        src="https://www.ionos.es/digitalguide/fileadmin/DigitalGuide/Teaser/UTF8-t.jpg"
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
	
[![M](https://upload.wikimedia.org/wikipedia/commons/thumb/2/2f/Google_2015_logo.svg/80px-Google_2015_logo.svg.png)](https://www.google.com/search?q=utf-8+validation+python&ei=NacDY9P6KKGdwbkPy8qk2As&ved=0ahUKEwiT6arx59r5AhWhTjABHUslCbsQ4dUDCA8&uact=5&oq=utf-8+validation+python&gs_lcp=Cgdnd3Mtd2l6EAMyBwgAEEcQsAMyBwgAEEcQsAMyBwgAEEcQsAMyBwgAEEcQsAMyBwgAEEcQsAMyBwgAEEcQsAMyBwgAEEcQsAMyBwgAEEcQsANKBAhBGABKBAhGGABQAFgAYPsEaAFwAXgAgAEAiAEAkgEAmAEAyAEIwAEB&sclient=gws-wiz)

[![M](https://upload.wikimedia.org/wikipedia/commons/thumb/e/e1/Logo_of_YouTube_%282015-2017%29.svg/70px-Logo_of_YouTube_%282015-2017%29.svg.png)](https://www.youtube.com/results?search_query=utf-8+validation+python)

- **[UTF-8](https://intranet.hbtn.io/rltoken/06JcOZip0vKo429Lp_Mz6A)** 
- **[Characters, Symbols, and the Unicode Miracle](https://intranet.hbtn.io/rltoken/v4RSq0R9IYkAreClE-0rUg)**


## Requirements
### General
- Allowed editors:  *` vi `* ,  *` vim `* ,  *` emacs `* 
- All files will be interpreted/compiled on Ubuntu 14.04 LTS using  *` python3 `*  (version 3.4.3)
- All files should end with a new line
- The first line of all your files should be exactly  *` #!/usr/bin/python3 `* 
- A  *` README.md `*  file, at the root of the folder of the project, is mandatory
- The code should use the  *` PEP 8 `*  style (version 1.7.x)
- All files must be executable
- The length of files will be tested using  *` wc `*

### Installation :computer:
	
- Clone this repository: `https://github.com/Alexoat76/holbertonschool-interview.git`	
- Access to directory: `cd 0x04-utf8_validation`
- `Compile` accord to `instructions` of each task.

## Files :file_folder:

## Test :heavy_check_mark:

+ **[0-main.py](./0-main.py)**  *`Provided by Holberton School`*.

---

## Tasks

+ [x] 0\. **UTF-8 Validation**

+ **[0-validate_utf8.py](./0-validate_utf8.py)**

Write a method that determines if a given data set represents a valid UTF-8 encoding.
* Prototype:  *` def validUTF8(data) `* 
* Return:  *` True `*  if data is a valid UTF-8 encoding, else return  *` False `* 
* A character in UTF-8 can be 1 to 4 bytes long
* The data set can contain multiple characters
* The data will be represented by a list of integers
* Each integer represents 1 byte of data, therefore you only need to handle the 8 least significant bits of each integer

```python
#!/usr/bin/python3
"""
Main file for testing
"""

validUTF8 = __import__('0-validate_utf8').validUTF8

data = [65]
print(validUTF8(data))

data = [80, 121, 116, 104, 111, 110, 32, 105, 115, 32, 99, 111, 111, 108, 33]
print(validUTF8(data))

data = [229, 65, 127, 256]
print(validUTF8(data))

```

```bash
$ ./0-main.py
True
True
False
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
