<p align="center">
<img src="https://img.shields.io/badge/LINUX-darkgreen.svg"/>
<img src="https://img.shields.io/badge/Shell-ligthgreen.svg"/>
<img src="https://img.shields.io/badge/Vim-green.svg"/>
<img src="https://img.shields.io/badge/Python-blue.svg"/>
<img src="https://img.shields.io/badge/Markdown-black.svg"/><br>	
</p>

# 0x07. Rotate 2D Matrix

Given an *` n `* x *` n `* **2D matrix**, *` rotate `* it **90 degrees** clockwise. Using Python language.

<p align="center">
  <img width="300"
        src="https://i1.faceprep.in/Companies-1/matrix%20rotation%20by%2090%20degrees.gif"
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
	
[![M](https://upload.wikimedia.org/wikipedia/commons/thumb/2/2f/Google_2015_logo.svg/80px-Google_2015_logo.svg.png)](https://www.google.com/search?q=rotate+2d+matrix+python&oq=Rotate+2D+Matrix&aqs=chrome.2.0i512l6j0i22i30l4.3742j0j15&sourceid=chrome&ie=UTF-8)

[![M](https://upload.wikimedia.org/wikipedia/commons/thumb/e/e1/Logo_of_YouTube_%282015-2017%29.svg/70px-Logo_of_YouTube_%282015-2017%29.svg.png)](https://www.youtube.com/results?search_query=rotate+2d+matrix+python)

## Requirements
### General
- Allowed editors:  *` vi `* ,  *` vim `* ,  *` emacs `* 
- All files will be interpreted/compiled on Ubuntu 14.04 LTS using  *` python3 `*  (version 3.4.3)
- All files should end with a new line
- The first line of all your files should be exactly  *` #!/usr/bin/python3 `* 
- A  *` README.md `*  file, at the root of the folder of the project, is mandatory
- The code should use the  *` PEP 8 `*  style (version 1.7.x)
- Not allowed to import any module
- All modules and functions must be documented
- All files must be executable

### Installation :computer:
	
- Clone this repository: `https://github.com/Alexoat76/holbertonschool-interview.git`	
- Access to directory: `cd 0x07-rotate_2d_matrix`
- `Compile` accord to `instructions` of each task.

## Files :file_folder:

## Test :heavy_check_mark:

+ **[main_0.py](./main_0.py)**  *`Provided by Holberton School`*.

---

## Tasks

+ [x] 0\. **Rotate 2D Matrix**

+ **[0-rotate_2d_matrix.py](./0-rotate_2d_matrix.py)**

Given an   *` n `*   x   *` n `*   2D matrix, rotate it 90 degrees clockwise.

* Prototype:  *` def rotate_2d_matrix(matrix): `* 
* Do not return anything. The matrix must be edited in-place.
* You can assume the matrix will have 2 dimensions and will not be empty.

```python3
#!/usr/bin/python3
"""
Test 0x07 - Rotate 2D Matrix
"""
rotate_2d_matrix = __import__('0-rotate_2d_matrix').rotate_2d_matrix

if __name__ == "__main__":
    matrix = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]]

    rotate_2d_matrix(matrix)
    print(matrix)

```
```bash
$
$ ./main_0.py
[[7, 4, 1],
[8, 5, 2],
[9, 6, 3]]
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
