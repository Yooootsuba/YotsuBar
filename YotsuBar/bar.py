import sys
from .cursor import hide_cursor__, atexit__


class YotsuBar:

    def __init__(self,
                 max           = 100,
                 width         = 50,
                 top_text      = None,
                 left_text     = '',
                 right_text    = '',
                 bar_prefix    = '[',
                 bar_fill_char = '=',
                 bar_suffix    = ']',
                 hide_cursor   = False):

        self.index         = 0
        self.max           = max
        self.width         = width
        self.top_text      = top_text
        self.left_text     = left_text
        self.right_text    = right_text
        self.bar_prefix    = bar_prefix
        self.bar_fill_char = bar_fill_char
        self.bar_suffix    = bar_suffix

        if hide_cursor == True:
            hide_cursor__()
            atexit__()


    def next(self):
        self.index += 1
        self.write()


    def write(self):
        sys.stdout.write('\r%s%s%s%s %d%%%s' % (self.left_text,
                                                self.bar_prefix,
                                                (int(self.index / self.max * self.width) * self.bar_fill_char).ljust(self.width, ' '),
                                                self.bar_suffix,
                                                self.get_percent(),
                                                self.right_text))
        sys.stdout.flush()


    def get_percent(self):
        return self.index / self.max * 100
