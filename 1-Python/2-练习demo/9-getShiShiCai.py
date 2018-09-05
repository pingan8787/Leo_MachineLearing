import urllib.request
import re

url = "http://worldcup.cctv.com/nettv/sports/data/schedule/WCUP_2018-2018.xml"
def get_data(url):
    request = urllib.request.Request(url)
    response = urllib.request.urlopen(request)
    data = response.read()
    data = data.decode('utf-8')
    return data

result_data = get_data(url)
result_data = result_data.find_all('homeName=')
print(result_data)