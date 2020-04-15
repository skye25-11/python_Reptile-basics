import urllib.request
#这条语句的作用是引入urllib.request程序包，这是Python自 带的程序包，丌需要安装，这个程序包的作用是访问网站。

url="http://127.0.0.1:5000"

resp=urllib.request.urlopen(url)
'''这条语句的作用是打开url网址的网址，这里为了简单说明问 题打开自己的微型网站http://127.0.0.1:5000，
其中 urllib.request是urllib中的一个子程序包，urlopen是打开网 站的函数。 '''

data=resp.read()
'''这个网站打开后就如同打开文件一样，要使用read函数读取 网站的内容，读出的二进制数据。 '''
html=data.decode()
'''这条语句的作用是把二进制数据html转为字符串，转换的编 码是utf-8，默认时decode()是使用utf-8编码，也可以指定 转换编码，
例如：html=html.decode("utf-8")戒者 html=html.decode("gbk")，具体采用什么编码是看网站的 网页是说明编码，如果编码丌正确会出现汉字乱码。 '''
print(html)
