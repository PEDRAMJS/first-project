import time
import concurrent.futures   
def sleeping(sec):
    print('sleeping for {sec} second(s)...')
    time.sleep(sec)
    print('sone sleeping...')
