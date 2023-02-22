# Project Overview

![Hbnb_Logo](images/hbnb_logo.jpg)

The goal of this project is to build a clone of the AirBnB website which will eventually be deployed on a server. It will collectively cover fundamental concepts of higher level programming and at the end of the project the complete web application will be composed of:

* A command interpreter to manipulate data without a visual interface like in a Shell
* A website (the front-end) that shows the final product to everyone: static and dynamic
* A database or files that store data (data = objects)
* An API that provides a communication interface between the front-end and your data (retrieve, create, delete, update them)

## First steps: The console

Here we create a Command Line Interface (CLI) to manage objects for the AirBnB clone website. This text based user interface similar to Shell will allow for the following functionalities:

* Create a data model
* Manage objects (create, update, destroy, etc)
* Store and persist objects to a file (JSON file)

### Environment
This project is interpreted/tested on Ubuntu 20.04 LTS using python3 (version 3.8.5)

### Installation
* Clone this repository: `git clone "https://github.com/sotieno/AirBnB_clone.git"`
* Access AirBnb directory: `cd AirBnB_clone`
* Run hbnb(interactively): `./console` and enter command
* Run hbnb(non-interactively): `echo "<command>" | ./console.py`

### Examples of use
In interactive mode:

```
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb)
(hbnb)
(hbnb) quit
$
```
In non-interactive mode:

```
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb)
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb)
$
```
## Preview of final product

![Final_Product1](images/final_product1.jpg)

![Final_Product2](images/final_product2.jpg)

## Authors
Idris Yakub - [Github](https://github.com/driiisdev)
Sylvia Otieno - [Github](https://github.com/sotieno)


