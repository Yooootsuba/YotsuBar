import atexit


def show_cursor__():
    print('\x1b[?25h', end = '')


def hide_cursor__():
    print('\x1b[?25l', end = '')


def atexit__():
    atexit.register(show_cursor__)
