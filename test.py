import time
from YotsuBar.bar import YotsuBar


ASCII_ART = '''
                                     _
                   \_/ _ _|_  _     |_)  _. ._
                    | (_) |_ _> |_| |_) (_| |

            '''


print(ASCII_ART)

bar = YotsuBar(left_text = 'YotsuBar ', hide_cursor = True)

for i in range(100):
    time.sleep(0.05)
    bar.next()

print('\n')
