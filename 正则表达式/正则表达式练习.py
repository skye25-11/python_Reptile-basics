
print('例题1、字符"\d"匹配0-9之间的一个数值。')
import re
reg=r"\d"
m=re.search(reg,"ab23cd")
print(m)

print('\n例题2、字符"+"重复前面一个匹配字符一次或者多次。')
import re
reg=r"b\d+"
m=re.search(reg,"a123b123c")
print(m)
#注意：r"b\d+"第一个字符要匹配"b"，后面是连续的多个数字，因此是"b123"，不是"a12"。

print('\n例题3、字符"*"重复前面一个匹配字符零次或者多次。')
import re
reg=r"ab+"
m=re.search(reg,"acabc")
print(m)
reg=r"ab*"
m=re.search(reg,"acabc")
print(m)

print('\n例题4，字符"?"重复前面一个匹配字符零次或者一次。')
import re
reg=r"ab?"
m=re.search(reg,"abbcabc")
print(m)

print('\n例题5，字符"."代表任何一个字符，但是没有特别声明时不代表字符..................."。"')
import re
s="xaxby"
m=re.search(r"a.b",s)
print(m)