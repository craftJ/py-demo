import urllib
import urllib.request


url = "https://www.baidu.com"

request = urllib.request.urlopen(url)

print(request.read)







