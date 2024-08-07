# USB-serial console

The USB-serial console is used by
[MicroPython REPL](./micropython.md)
and Python scripts.

Operating systems access USB-serial console distinctly as below.
If using MicroPython, the REPL is the default program that runs on the Pico.
If the ">>>" prompt isn't seen after connecting, verify that MicroPython is installed on the Pico.

```python
>>> print("Hello")
Hello
```

Once connected to the console, you can copy-paste in scripts, or use
[rshell](./rshell.md)
to edit and upload autorun MicroPython scripts.

## Windows

Look in Windows Device Manager under "Ports".
There should be "COM*" device of a specific number e.g. COM3.

![Windows Device Manager ports](https://cdn.sparkfun.com/assets/3/9/f/5/8/521541a3757b7f92498b456a.jpg)

Use
[PuTTY](https://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html)
to connect at 115200 baud serial.
Under "Serial line" in PuTTY enter "COM3" or whatever device name is seen in Windows Device Manager.
This device name may change if you plug the Pico into a different USB port.

![PuTTY serial port](https://www.scivision.dev/images/2016/putty-serial-main.png)

## macOS

Depending on the Pico program used, the USB-serial device will show up in either of these mount points:

TinyUSB:

```
ls /dev/cu.usbserial*
```

or MicroPython REPL:

```
ls /dev/tty.usbmodem*
```

Connect using
[screen](https://linux.die.net/man/1/screen)
like:

```sh
screen /dev/tty.usbmodem* 115200
```

## Linux

Connect using
[screen](https://linux.die.net/man/1/screen)
like:

```sh
screen /dev/ttyACM* 115200
```
