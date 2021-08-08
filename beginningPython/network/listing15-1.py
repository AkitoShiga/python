import requests
from subprocess import Popen, PIPE
import re

p = re.compile('<a href="(/jobs/\\d+)/">(.*?)</a>')
text = requests.get("https://www.python.org/jobs").text

tidy = Popen('tidy', stdin=PIPE, stdout=PIPE, stderr=PIPE)
tidy.stdin.write(text.encode())
tidy.stdin.close()


for url, name in p.findall(text):
    print(f'{name} {(url)}')