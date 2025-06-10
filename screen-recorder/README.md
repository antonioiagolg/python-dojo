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

* For pyautogui, I have to install also python-xlib, pillow and gnome-screenshot (I did not want lots of dependencies in my machine, but I want to
see this working, so I installed them)
```
$ sudo pacman -S python-xlib
$ sudo pacman -S gnome-screenshot
# In your project virtual environment
$ pip install pillow
```

* The cv2.waitKey() function is really strange. I was trying to press the q letter to finish my recording, but nothing happens. Checking the output of this
function, it returned -1. After digging the documentation, foruns, I found out that it only works for an active window opened by opencv. First you need
to open an window, them from this active window, waitKey will listen to the pressed keys. I thought it would work without having to open an window,
it could work just listening to my keyboard, I did not want to open a new window just to listen to my keyboard actions, but I had to. 
