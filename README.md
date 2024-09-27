# 2024 Fall Miniproject

[ASSIGNMENT](./assignment/)

This project uses the Raspberry Pi Pico WH (wireless, with header pins).

Each student must provide a USB cable that connects to their laptop and has a micro-USB connector on the other end to plug into the Pi Pico.
The student laptop is used to program the Pi Pico.
The laptop software works on macOS, Windows, and Linux.

This miniproject focuses on using
[MicroPython](./doc/micropython.md)
using
[Thonny IDE](./doc/thonny.md).
Other IDE can be used, including Visual Studio Code or
[rshell](./doc/rshell.md).

## Hardware

* Raspberry Pi Pico WH [SC0919](https://www.raspberrypi.com/documentation/microcontrollers/raspberry-pi-pico.html#raspberry-pi-pico-w-and-pico-wh) (WiFi, Bluetooth, with header pins)
* Freenove Pico breakout board [FNK0081](https://store.freenove.com/products/fnk0081)
* Speaker 8 ohm 800 mW [SP-1605](https://www.soberton.com/wp-content/uploads/2018/07/SP-1605-June-2018.pdf)
* [Photoresistor](./doc/photocell.md) and 10k ohm resistor
* 2 [tactile switches](https://sten-eswitch-13110800-production.s3.amazonaws.com/system/asset/product_line/data_sheet/184/TL59-TL58.pdf)


## Code Cleanliness and Automation

1. This repo uses `poetry` for python dependency management. See the [docs](https://python-poetry.org/docs/) for an installation guide and introduction.
   1. Once `poetry` is installed on your computer, you may run `poetry install` to create a virtualenv in which all of your dependencies will be installed (separate from the system python path).

2. `pylint` is as a dev dependency for static code analysis. `pylint` is best described in the [docs](https://pylint.readthedocs.io/en/stable/):
    > Pylint analyses your code without actually running it. It checks for errors, enforces a coding standard, looks for code smells, and can make suggestions about how the code could be refactored.
    1. One may run pylint in this environment by typing: `poetry run pylint *`

3. `mypy` is added as a dependency for type checking. This ensures you don't do silly things like suming an int with a string.
    1. One may run mypy in this environment by typing: `poetry run mypy *`

4. `pre-commit` is added as a dev dependency for a pre-commit hook for `git`. This tool is configured with the `.pre-commit-config.yaml` and is one of the most convenient tools when collaborating with teams, as it automatically fixes your files or alerts you about problems before a commit is made.
   1. `black` (an automatic python code formatter) is run before you make a commit with git.
   2.  You can run `pre-commit` before commiting code by entering `poetry run pre-commit run --all`


## Reference

* [Pico WH pinout diagram](https://datasheets.raspberrypi.com/picow/PicoW-A4-Pinout.pdf) shows the connections to analog and digital IO.
* Getting Started with Pi Pico [book](https://datasheets.raspberrypi.com/pico/getting-started-with-pico.pdf)
