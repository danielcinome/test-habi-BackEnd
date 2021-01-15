# Habi Test

The project is based on a technical test of Habi.
It consists of a program that prints numbers in the style of an LCD screen.

## Description
For the solution of this project we used the Python programming language, below you will find the steps to run the project in your local machine
1. clone the repository
	`git clone https://github.com/danielcinome/test-habi-BackEnd.git`
2. go to the folder **test-habi-BackEnd**
	`cd test-habi-BackEnd`
below you will find this series of
---
File Name|Description
---|---|---
[display.py](https://github.com/danielcinome/test-habi-BackEnd/blob/main/display.py)| In this file is the main function, here once you run the user can enter the information which is validated to ensure proper functioning
[memory_letters.py](https://github.com/danielcinome/test-habi-BackEnd/blob/main/memory_letters.py)| It contains the information to structure from the display a letter which is made up of an array of numbers that establish that it should be printed. **currently the program does not have this function**
[memory_numbers.py](https://github.com/danielcinome/test-habi-BackEnd/blob/main/memory_numbers.py)|Contains the information to structure the number from the display, which is made up of an array of numbers that establish that it should be printed
[test_display.py](https://github.com/danielcinome/test-habi-BackEnd/blob/main/test_display.py)| contains unit tests of display methods

---
now that you have some context of the files, it's time to run it. to run the program write the following command;
	`python3 display.py`
	
![N|Solid](https://i.ibb.co/vmHZj1P/run.png)

Here you will find a small description that will indicate the structure where you will indicate the size and number to print

![N|Solid](https://i.ibb.co/pPS0qW3/2021.png)

if writing an incorrect structure or a size outside the range of 1-10 you will get an error like this

![N|Solid](https://i.ibb.co/7b7QLHW/error.png)

The basis of this project will allow printing letters.
this is a small example
![N|Solid](https://i.ibb.co/qk5f56x/letters.png)

## Author

- Daniel Chinome - [Github](https://github.com/danielcinome) / [Twitter](https://twitter.com/DanielChinome)
