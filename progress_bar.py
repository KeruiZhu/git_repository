# -*- coding:UTF-8 -*-
"""
A visuable progress-bar tool for python software
INPUT: iterable, function, *args, **kwargs
"""
import sys

def progress_bar(itera, func, *args, **kwargs):
    n = float(len(itera))
    cnt = 0
    for i in itera:
        sys.stdout.write('progress: | {0}{1} |  {2}% \r'.format('>'*int((cnt/n)*50), '='*(50-int((cnt/n)*50)), str(round((cnt/n)*100, 1))))
        sys.stdout.flush()  # 强制程序执行IO, 否则它将累计一定批量或者时间才执行
        func(i, *args, **kwargs)
        cnt += 1

    print('progress: | {0} |  100.0%'.format('>'*50))
