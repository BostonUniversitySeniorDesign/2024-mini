# rshell MicroPython connection

[rshell](https://github.com/dhylands/rshell/)
Python program is used to test and upload Python scripts on the Pico
[console](./console.md).
If the script is named "main.py", it will autorun when the Pico starts.

NOTE: don't use "sudo" when installing rshell, this is adequate:

```sh
pip install rshell
```

Specify the port of the Pico like:

* macOS: `rshell -p /dev/tty.usbmodem*`
* Linux: `rshell -p /dev/ttyACM*`
* Windows: `rshell -p COM3`  (look in Windows Device Manager under "Ports")

If rshell can't connect, try resetting Pico power (unplug, plug USB) and ensure
[MicroPython](./micropython.md)
is installed on the Pico.

Check which board(s) are connected:

```sh
boards
```

> pyboard @ /dev/tty.usbmodem12201

Start REPL on the Pico from rshell:

```sh
repl
```

> Entering REPL. Use Control-X to exit.
MicroPython; Raspberry Pi Pico with RP2040
Type "help()" for more information.
>>>

Copy a
[Python script](https://github.com/raspberrypi/pico-micropython-examples)
to the Pico.
Any script named "main.py" runs automatically when the Pico is powered on or reset.

```sh
cp ../pico-micropython-examples/adc/temperature.py /pyboard/main.py
```

> Copying 'pico-micropython-examples/adc/temperature.py' to '/pyboard/main.py' ...

Then press type

```sh
repl
```

and press Control-D to restart the Pico and the main.py program runs.
The "adc/temperature.py" script prints the onboard temperature in Celsius every 2 seconds.

> 19.55409
> 20.02224
