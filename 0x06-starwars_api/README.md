<p align="center">
<img src="https://img.shields.io/badge/LINUX-darkgreen.svg"/>
<img src="https://img.shields.io/badge/Shell-ligthgreen.svg"/>
<img src="https://img.shields.io/badge/Vim-green.svg"/>
<img src="https://img.shields.io/badge/NodeJS-yellow.svg"/>
<img src="https://img.shields.io/badge/Markdown-black.svg"/><br>	
</p>

# 0x05. N Queens

This task consist in Create a *`Script`* that prints all characters of a **`Star Wars`** movie. Using Node-JS.

<p align="center">
  <img width="320"  
        src="https://miro.medium.com/max/960/1*6RaEVPng5kXrQubPt8r-qg.gif"
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
	
[![M](https://upload.wikimedia.org/wikipedia/commons/thumb/2/2f/Google_2015_logo.svg/80px-Google_2015_logo.svg.png)](https://www.google.com/search?q=star+wars+api+node&source=lnms&sa=X&ved=2ahUKEwiNhaqp8P75AhU3ZjABHX4MAMgQ_AUoAHoECAEQAg&biw=1920&bih=929&dpr=1)

[![M](https://upload.wikimedia.org/wikipedia/commons/thumb/e/e1/Logo_of_YouTube_%282015-2017%29.svg/70px-Logo_of_YouTube_%282015-2017%29.svg.png)](https://www.google.com/search?q=star+wars+api+node&source=lnms&tbm=vid&sa=X&ved=2ahUKEwiwvKWo8P75AhXVmYQIHdmYBEgQ_AUoAXoECAEQAw&biw=1920&bih=929&dpr=1)


## Requirements
### General
- Allowed editors:  *` vi `* ,  *` vim `* ,  *` emacs `* 
- All files will be interpreted on Ubuntu 14.04 LTS using  *` node `* (version 10.14.x)
- All files should end with a new line
- The first line of all files should be exactly  *` #!/usr/bin/node `*
- A  *` README.md `*  file, at the root of the folder of the project, is mandatory
- The code should be  *` semistandard `*  compliant. **[Rules of Standard](https://intranet.hbtn.io/rltoken/9D55NBEvxCOb2UpyDm1wUQ)** + **[semicolons on top](https://intranet.hbtn.io/rltoken/aHP62g9O1_ZGY34qeberZA)** . Also as reference: **[AirBnB style](https://intranet.hbtn.io/rltoken/Jcjw9xN9Y2IuLuve3yt7ag)**
- All files must be executable
- The length of the files will be tested using  *` wc `*
- Not allowed to use  *` var `*

## More Info
### Install Node 10
```bash
$ curl -sL https://deb.nodesource.com/setup_10.x | sudo -E bash -
$ sudo apt-get install -y nodejs
```

### Install semi-standard
***[Documentation](https://intranet.hbtn.io/rltoken/aHP62g9O1_ZGY34qeberZA)***

```bash
$ sudo npm install semistandard --global
```

### Install request module and use it
***[Documentation](https://intranet.hbtn.io/rltoken/mUx37zH56AfjkWx0O65QaA)***

```bash
$ sudo npm install request --global
$ export NODE_PATH=/usr/lib/node_modules
```

### Installation :computer:
	
- Clone this repository: `https://github.com/Alexoat76/holbertonschool-interview.git`	
- Access to directory: `cd 0x06-starwars_api`
- `Compile` accord to `instructions` of each task.

## Files :file_folder:

## Tasks

+ [x] 0\. **Star Wars Characters**

+ **[0-starwars_characters.js](./0-starwars_characters.js)**

Write a script that prints all characters of a Star Wars movie:
* The first positional argument passed is the Movie ID - example:  *` 3 `*  = “Return of the Jedi” 
* Display one character name per line in the same order as the “characters” list in the  *` /films/ `*  endpoint
* You must use the **[Star wars API](https://intranet.hbtn.io/rltoken/gOFjTqtp8L2xueAR74gqUw)** 
* You must use the  *` request `*  module

```bash
$ ./0-starwars_characters.js 3
Luke Skywalker
C-3PO
R2-D2
Darth Vader
Leia Organa
Obi-Wan Kenobi
Chewbacca
Han Solo
Jabba Desilijic Tiure
Wedge Antilles
Yoda
Palpatine
Boba Fett
Lando Calrissian
Ackbar
Mon Mothma
Arvel Crynyd
Wicket Systri Warrick
Nien Nunb
Bib Fortuna
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
