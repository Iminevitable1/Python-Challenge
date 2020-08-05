import urllib.request
from pprint import pprint
import pickle

url = urllib.request.urlretrieve("http://www.pythonchallenge.com/pc/def/banner.p", 'pc5.txt')

file = open('pc5.txt', 'rb')
data = pickle.load(file)

pprint(sorted(data, key=len))

def text(lists):
    return "".join(char*num for char, num in lists)
print(*map(text, data), sep = "\n")

file.close()
