import urllib.request
import re

# contents = urllib.request.urlretrieve("http://www.pythonchallenge.com/pc/def/equality.html", "pc3.txt")

file = open("pc3.txt").read()

x = re.findall("[a-z][A-Z]{3}([a-z])[A-Z]{3}[a-z]", file)

y = ''.join(x)

print(y)
