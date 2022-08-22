<p align="center">
<img src="https://img.shields.io/badge/LINUX-darkgreen.svg"/>
<img src="https://img.shields.io/badge/Shell-ligthgreen.svg"/>
<img src="https://img.shields.io/badge/Vim-green.svg"/>
<img src="https://img.shields.io/badge/Python-blue.svg"/>
<img src="https://img.shields.io/badge/Markdown-black.svg"/><br>	
</p>

# 0x03. Log Parsing

This task consist in Create a *`Script`* that reads **`stdin`** line by line and **Computes metrics**. Using Python language.

<p align="center">
  <img width="360"  
        src="https://files.realpython.com/media/Subprocess_Watermarked.6d0e6a5d7d77.jpg"
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
	
[![M](https://upload.wikimedia.org/wikipedia/commons/thumb/2/2f/Google_2015_logo.svg/80px-Google_2015_logo.svg.png)](https://www.google.com/search?q=log+parsing+with+python&bih=929&biw=1920&hl=en&source=hp&ei=JMP6Yqe1N4mMwbkPhpeSkA8&iflsig=AJiK0e8AAAAAYvrRNFxzDmEz9aTNiwcx5DnUV4N_VgUE&ved=0ahUKEwin16eh7cn5AhUJRjABHYaLBPIQ4dUDCAg&uact=5&oq=log+parsing+with+python&gs_lcp=Cgdnd3Mtd2l6EAMyBQgAEIAEMgYIABAeEBYyBggAEB4QFjIGCAAQHhAWMgYIABAeEBYyBggAEB4QFjIGCAAQHhAWMgYIABAeEBYyBggAEB4QFjIGCAAQHhAWUL4HWL4HYIQMaAFwAHgAgAF4iAF4kgEDMC4xmAEAoAECoAEBsAEA&sclient=gws-wiz)

[![M](https://upload.wikimedia.org/wikipedia/commons/thumb/e/e1/Logo_of_YouTube_%282015-2017%29.svg/70px-Logo_of_YouTube_%282015-2017%29.svg.png)](https://www.youtube.com/results?search_query=log+parsing+with+python)

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
- Access to directory: `cd 0x03-log_parsing`
- `Compile` accord to `instructions` of each task.

## Files :file_folder:

## Test :heavy_check_mark:

+ **[0-generator.py](./0-generator.py)**  *`Provided by Holberton School`*.

---

## Tasks

+ [x] 0\. **Log parsing**

+ **[0-stats.py](./0-stats.py)**

Write a script that reads   **` stdin `**   line by line and computes metrics:
* Input format:  *` <IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size> `*  (if the format is not this one, the line must be skipped)
* After every 10 lines and/or a keyboard interruption ( *` CTRL + C `* ), print these statistics from the beginning:* Total file size:  *` File size: <total size> `* 
* where  *` <total size> `*  is the sum of all previous  *` <file size> `*  (see input format above)
* Number of lines by status code: 
	* possible status code: *` 200 `*, *` 301 `*, *` 400 `*, *` 401 `*, *` 403 `*, *` 404 `*, *` 405 `* and *` 500 `* 
	* if a status code doesn’t appear or is not an integer, don’t print anything for this status code
	* format:  *` <status code>: <number> `* 
	* status codes should be printed in ascending order

**Warning**:  In this sample, you will have random value - it’s normal to not have the same output as this one.

```bash
$ cat 0-generator.py
#!/usr/bin/python3
import random
import sys
from time import sleep
import datetime

for i in range(10000):
    sleep(random.random())
    sys.stdout.write("{:d}.{:d}.{:d}.{:d} - [{}] \"GET /projects/260 HTTP/1.1\" {} {}\n".format(
        random.randint(1, 255), random.randint(1, 255), random.randint(1, 255), random.randint(1, 255),
        datetime.datetime.now(),
        random.choice([200, 301, 400, 401, 403, 404, 405, 500]),
        random.randint(1, 1024)
    ))
    sys.stdout.flush()

$ ./0-generator.py | ./0-stats.py 
File size: 5213
200: 2
401: 1
403: 2
404: 1
405: 1
500: 3
File size: 11320
200: 3
301: 2
400: 1
401: 2
403: 3
404: 4
405: 2
500: 3
File size: 16305
200: 3
301: 3
400: 4
401: 2
403: 5
404: 5
405: 4
500: 4
^CFile size: 17146
200: 4
301: 3
400: 4
401: 2
403: 6
404: 6
405: 4
500: 4
Traceback (most recent call last):
  File "./0-stats.py", line 15, in <module>
Traceback (most recent call last):
  File "./0-generator.py", line 8, in <module>
    for line in sys.stdin:
KeyboardInterrupt
    sleep(random.random())
KeyboardInterrupt
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
