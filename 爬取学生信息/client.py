import urllib.request
import re

try:
    resp = urllib.request.urlopen("http://127.0.0.1:5000")
    data = resp.read()
    html = data.decode()
    m = re.search(r"<tr>", html)
    n = re.search(r"</tr>", html)
    while m != None and n != None:
        row = html[m.end():n.start()]
        a = re.search(r"<td>", row)
        b = re.search(r"</td>", row)
        while a != None and b != None:
            s = row[a.end():b.start()]
            print(s, end=" ")
            row = row[b.end():]
            a = re.search(r"<td>", row)
            b = re.search(r"</td>", row)
        print()
        html = html[n.end():]
        m = re.search(r"<tr>", html)
        n = re.search(r"</tr>", html)
except Exception as e:
    print(e)

