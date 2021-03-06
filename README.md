# YotsuBar

![image](https://github.com/Yooootsuba/YotsuBar/blob/master/demo.gif)

## Installation

1. Clone this project

```sh
$ git clone https://github.com/Yooootsuba/YotsuBar.git
```

2. Change the working directory

```sh
$ cd YotsuBar
```

3. Install the package

```sh
$ python setup.py install
```

## Example

Customize your progress bar

```py
import time
from YotsuBar import YotsuBar

bar = YotsuBar(max = 50, width = 40, bar_prefix = '|', bar_fill_char = '#', bar_suffix = '|')

for i in range(50):
    time.sleep(0.03)
    bar.flush()
```

Output

```
|################################        | 80%
```

Put the message or some info anywhere you want

```py
import time
from YotsuBar import YotsuBar

bar = YotsuBar(top_text = 'YotsuBar', left_text = 'Processing ', right_text = ' [1/2]')
bar.show_top_text()

for i in range(100):
    time.sleep(0.01)
    bar.flush()
```

Output

```
           [                     YotsuBar                     ]
Processing [==================================================] 100% [1/2]
```

Allow to use context manager operation and hide cursor temporarily

```py
import time
from YotsuBar import YotsuBar

with YotsuBar(hide_cursor = True) as bar:
    for i in range(100):
        time.sleep(0.01)
        bar.flush()
```

## License

MIT License
