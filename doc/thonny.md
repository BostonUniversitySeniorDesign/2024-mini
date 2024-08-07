# Thonny IDE

[Thonny](https://projects.raspberrypi.org/en/projects/getting-started-with-the-pico/)
provides a graphical IDE for Python, including MicroPython on microcontrollers like the Pi Pico.
Thonny requires
[MicroPython](./micropython.md)
installed on the Pi Pico.

## Install Thonny

From the laptop Terminal:

```sh
python -m pip install thonny
```

Start Thonny by typing in Terminal:

```sh
thonny
```

### macOS

If on macOS and you used the Thonny .pkg file from
[Thonny.org](https://thonny.org/),
use macOS Spotlight to find Thonny and start it--press <kbd>Command</kbd><kbd>space</kbd>, type "thonny" and press Enter.

### Windows

If on Windows and you used the Thonny .exe file from
[Thonny.org](https://thonny.org/)
or

```sh
winget install AivarAnnamaa.Thonny
```

Thonny is installed in the Windows Start menu under Thonny.

## Initial connection to Pi Pico

Start Thonny and click "Run" "Configure Interpreter" and select "MicroPython (Raspberry Pi Pico)".
The "port or WebREPL" should select "Try to detect port automatically".
You could also
[manually specify a port](./console.md).

Upon clicking "OK" and with a Pico already connected, Thonny shell should show a message like

> MicroPython; Raspberry Pi Pico with RP2040

If you don't see that message or get a connection error, try:

* clicking the Red "stop" button in the Thonny toolbar
* unplugging and plugging in the Pico and click the red "stop" button in the Thonny toolbar

This should give the MicroPython prompt ">>>" upon pressing Enter.

Save Python code to the Pi Pico by pressing <kbd>Ctrl</kbd><kbd>s</kbd> or <kbd>Command</kbd><kbd>s</kbd> and choose to save to the Pi Pico.
Name the file whatever you like and run it from Thonny.
If you name the file "main.py", that program will always run automatically when the Pi Pico powers up.

## Run program

If you named the Pi Pico Python file "main.py" it will run automatically on Pi Pico powerup.
Pressing the "stop" button in Thonny will stop the program and restart main.py.

## Troubleshooting

If when running the MicroPython code you get an error like:

> ModuleNotFoundError: No module named 'machine'

this usually means you're running the code on your computer instead of the Pico.
In Thonny, click "Run" "Configure Interpreter" and select "MicroPython (Raspberry Pi Pico)" to automatically run on the Pi Pico instead of your laptop.
