import time
from YotsuBar.bar import YotsuBar


ASCII_ART = '''
                               _
             \_/ _ _|_  _     |_)  _. ._
              | (_) |_ _> |_| |_) (_| |

            '''


print(ASCII_ART)

bar = YotsuBar(top_text = 'YotsuBar', hide_cursor = True)
bar.show_top_text()

for i in range(100):
    time.sleep(0.03)
    bar.flush()

print('\n')
