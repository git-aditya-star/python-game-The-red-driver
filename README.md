# The Red Driver Game
A simple python game where you have to control a car ,avoid rocks , collect coins and travel your way

## Starting up :

 1. Should have `python` installed in the system.
 2. Install `pip install poetry`
 3. Setup the project `poetry install`
 4. Run the game `poetry run python ./race/race.py`


# Game play :
 
 MOVE RIGHT - RIGHT ARROW KEY
 MOVE LEFT  - LEFT ARROW KEY

## Screenshots 
!["Screen1"](images/ss1.png "Screen1")
!["Screen2"](images/ss2.png "Screen2")
!["Screen3"](images/ss3.png "Screen3")
!["Screen4"](images/ss4.png "Screen4")

## Troubleshooting

### Running in Docker Dev Container

Error message: 
    ImportError: Library "GL" not found

1. `pip install pyqt5`
2. `pip install pyqtwebengine`
3. `pip install pyglet`
4. `sudo apt install -y libgl1`

### Running in CodeSpaces (Ubuntu 22)

Error message: 
    ImportError: Library "GL" not found
    ImportError: Library "GLU" not found.

1. `sudo apt install -y libgl1`
2. `sudo apt install -y libglu1`

## Credits
[Original repository](https://github.com/git-aditya-star/python-game-The-red-driver) by [Aditya Chavan](https://github.com/git-aditya-star)