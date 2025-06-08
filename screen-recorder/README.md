# Takeaways

* I use asdf to manage python instances. By default, when installing python, it does not come with tkinter lib. To install python with
asdf that contains tkinter, please run the following command:
```
PYTHON_CONFIGURE_OPTS="--with-tcltk-includes='$(pkg-config tk --cflags)' --with-tcltk-libs='$(pkg-config tk --libs)'" asdf install python <version>
```
Please install the dependencies before run the command. In arch:
```
$ sudo pacman -Syu tk
```

For pyautogui, I have to install also python-xlib, pillow and gnome-screenshot (I did not want lots of dependencies in my machine, but I want to
see this working, so I installed them)
```
$ sudo pacman -S python-xlib
$ sudo pacman -S gnome-screenshot
# In your project virtual environment
$ pip install pillow
```
