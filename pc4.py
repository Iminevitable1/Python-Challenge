import  urllib.request
import re

target = 8022

while True:
    source = urllib.request.urlopen("http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=" + str(target)).read().decode('utf-8')
    found = re.findall('[0-9]+', source)
    if found:
        target = found[-1]
        print(target)
    else:
        print(source)
