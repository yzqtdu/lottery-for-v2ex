import hashlib
import requests
from bs4 import BeautifulSoup
import base64
import math

def createHash(content):
    return hashlib.md5(content.encode("utf-8")).hexdigest()

def rankHash(items, origin):
    hashList = map(lambda item: {"id": item["id"], "dif": abs(int(createHash(item["content"]), 16) - int(origin, 16))}, items)
    return sorted(hashList, key=lambda item: item["dif"])

def userList(post):
    res = requests.get("https://v2ex.com/t/" + post)
    soup = BeautifulSoup(res.text, features="html.parser")
    number = soup.select("#Main .box:nth-child(4) .cell > span.gray")[0].contents[0].split()[0]
    print("number:", number)
    final = []
    for i in range(1, (math.floor(int(number) / 100)) + 2):
        parseList = parseHtml(post + '?p=' + str(i))
        print("parse complete " + str(i))
        parseList = [{"id": item["id"], "content": item["id"] + getImg(item["url"])} for item in parseList]
        print("img retrieve complete " + str(i))
        final += parseList
    return final

def getImg(src):
    res = requests.get(src)
    return str(base64.b64encode(res.content).decode("utf-8"))

def parseHtml(post):
    res = requests.get("https://v2ex.com/t/" + post)
    soup = BeautifulSoup(res.text, features="html.parser")
    box = soup.select("#Main .box:nth-child(4) .cell")
    box = [{"url": item.find("img")["src"], "id": item.find("strong").find("a").string} for item in box if item.get("id")]
    return box

l = userList("897658")
print("list parse complete, total length ", len(l))
r = rankHash(l, createHash("3078.55 10829.08 2298.80"))
print(r)
