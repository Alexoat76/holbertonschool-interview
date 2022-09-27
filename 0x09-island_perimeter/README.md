<p align="center">
<img src="https://img.shields.io/badge/LINUX-darkgreen.svg"/>
<img src="https://img.shields.io/badge/Shell-ligthgreen.svg"/>
<img src="https://img.shields.io/badge/Vim-green.svg"/>
<img src="https://img.shields.io/badge/Python-blue.svg"/>
<img src="https://img.shields.io/badge/Markdown-black.svg"/><br>	
</p>

# 0x09. Island Perimeter

Create a function that returns the *` perimeter `* of the island described in **` grid `**. Using Python language.

<p align="center">
  <img width="300"
        src="https://i.pinimg.com/originals/cf/51/ad/cf51ad748537f4ea6899ab44388ad110.gif"
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
	
[![M](https://upload.wikimedia.org/wikipedia/commons/thumb/2/2f/Google_2015_logo.svg/80px-Google_2015_logo.svg.png)](https://www.google.com/search?q=island+perimeter+python&ei=T7kxY-aNDLSzkvQPiK6GmAc&oq=Island+Perimeter&gs_lcp=Cgdnd3Mtd2l6EAEYADIKCAAQRxDWBBCwAzIKCAAQRxDWBBCwAzIKCAAQRxDWBBCwAzIKCAAQRxDWBBCwAzIKCAAQRxDWBBCwAzIKCAAQRxDWBBCwAzIKCAAQRxDWBBCwAzIKCAAQRxDWBBCwAzIHCAAQsAMQQ0oECEEYAEoECEYYAFAAWABg9wloAXABeACAAQCIAQCSAQCYAQDIAQnAAQE&sclient=gws-wiz)

[![M](https://upload.wikimedia.org/wikipedia/commons/thumb/e/e1/Logo_of_YouTube_%282015-2017%29.svg/70px-Logo_of_YouTube_%282015-2017%29.svg.png)](https://www.youtube.com/results?search_query=island+perimeter+python)

## Requirements
### General
- Allowed editors:  *` vi `* ,  *` vim `* ,  *` emacs `* 
- All files will be interpreted/compiled on **` Ubuntu 14.04 LTS `** using  *` python3 `*  (version 3.4.3)
- All files should end with a new line
- The first line of all your files should be exactly  *` #!/usr/bin/python3 `* 
- A  *` README.md `*  file, at the root of the folder of the project, is mandatory
- The code should use the  *` PEP 8 `*  style (version 1.7.x)
- Not allowed to import any module
- The modules and functions must be documented
- All files must be executable

### Installation :computer:
	
- Clone this repository: `https://github.com/Alexoat76/holbertonschool-interview.git`	
- Access to directory: `cd 0x09-island_perimeter`
- `Compile` accord to `instructions` of each task.

## Files :file_folder:

## Test :heavy_check_mark:

+ **[0-main.py](./0-main.py)**  *`Provided by Holberton School`*.

## Tasks

+ [x] 0\. **Island Perimeter**

+ **[0-island_perimeter.py](./0-island_perimeter.py)**

Create a function   *` def island_perimeter(grid): `*   that returns the perimeter of the island described in   *` grid `*  :
*  *` grid `*  is a list of list of integers:
	* 0 represents water
	* 1 represents land
	* Each cell is square, with a side length of 1
	* Cells are connected horizontally/vertically (not diagonally). 
	*  *` grid `*  is rectangular, with its width and height not exceeding 100
* The grid is completely surrounded by water
* There is only one island (or nothing).
* The island doesn’t have “lakes” (water inside that isn’t connected to the water surrounding the island).

```python3
#!/usr/bin/python3
"""
0-main
"""
island_perimeter = __import__('0-island_perimeter').island_perimeter

if __name__ == "__main__":
    grid = [
        [0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 0]
    ]
    print(island_perimeter(grid))

```
```bash
$ 
$ ./0-main.py
12
$ 

```


---

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
