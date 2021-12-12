'''
 install libraries from pypi without using cmd just copy

'''
import clipboard
import time
import os

while True:
	time.sleep(5)
	text = clipboard.paste().strip()
	if text.startswith('pip install'):
		os.system(text)
		clipboard.copy('')
