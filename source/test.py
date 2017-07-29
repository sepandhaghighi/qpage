
'''
>>> from qpage import *
>>> import random
>>> random.seed(1)
>>> list_randomize([1,2,3,5,6])
[2, 1, 5, 3, 6]
>>> email_at("example@yahoo.com")
'example at yahoo.com'
>>> convert_bytes(200)
'200.0 bytes'
>>> convert_bytes(6000)
'5.9 KB'
>>> convert_bytes(80000)
'78.1 KB'
>>> random.seed(1)
>>> random_badge_color()
'yellowgreen'
>>> create_badge()
'https://img.shields.io/badge/qpage-2.0-blue.svg'
>>> random.seed(1)
>>> create_badge(random=True)
'https://img.shields.io/badge/qpage-2.0-yellowgreen.svg'
>>> random.seed(1)
>>> read_lorem(5)
'ipsum \nLorem sit dolor amet,'
>>> print_line(4)
----
>>> print_line(5,"%")
%%%%%
>>> name_standard('test')
'Test'
>>> name_standard('TesT')
'Test'
>>> internet() # if there is stable internet connection
True
>>> wait_func(4)
.
.
.
.
>>> wait_func()
.
.

'''