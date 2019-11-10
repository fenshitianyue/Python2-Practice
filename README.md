# Python 2.7.5 笔记

> 注：此文档是本人在学习和使用Python2进行工程实践中所用到的一些语法/技巧
>
> by：aideny

## lambda

lambda关键字是用来创建内联函数的，调用方式和普通的函数相同。【例1】

优势：

- 可以快速声明，所以用来做回调函数非常理想，和map、filter、reduce这样的函数搭配使用尤其有效。【例2】

  

## str

### 连接字符串

#### 加号

在Python中，String对象是定长对象，一旦创建，长度就不可变化，若是使用+号连接两个字符串，则会新开辟一段长度总和长度的内存，再将两个字符串memcpy进去。如果要连接N个String对象，则要进行N-1次内存申请和拷贝。 这样会有很大的开销，所以不推荐使用这种方法来连接字符串。官方推荐使用join， 因为会先统计所有元素的长度，申请内存，然后拷贝。

#### join

join 用于将序列(列表、元组、字符串、字典）中的元素以指定的字符连接生成一个新的字符串。

> 注：
>
> - join只能连接字典中的键。
> - 序列中的元素也必须是字符串

```python
s = '-'
seq = ['aaa', 'bbb', 'ccc']
print s.join(seq)
>>>>>>>>>>>>>>>>
out: aaa-bbb-ccc
    
# 用加号实现字符串相加
s1 = 'hello'
s2 = 'world'
print s1 + ' ' + s2

# 用join可以这么做：
tmp_list = list(s1, s2)
print ' '.join(tmp_list)
```



实际应用开发时，获取应用的所有进程 ID，然后杀掉所有进程，可以使用 join 拼接出 kill 命令。

```
'kill %s' % ' '.join(['111','22'])
```

拼接结果为：

```
'kill 111 22'
```

使用:

```python
pids = ['111', '22']
subprocess.run('kill  %s' % ' '.join(pids), shell=True)
```

### contains

想要知道目标字符串pos是否包含指定的字符串可以用以下两种方法：

method1:

```python
if '__sum' in pos:
	print 'True'
else:
	print 'False'
```

method2:

```python
# find如果在母串中找到字串，返回字串在母串中的起始下标；否则返回-1
if pos.find('__sum') != -1:
    print 'True'
else:
    print 'False'
```

### 大小写

 ```python
s.lower()  # 字符串s中字符全部转换为小写
s.upper()  # *大写
s.swapcase()  # 字符串s中字符大小写互换
s.capitalize()  # 字符串s首字母转换为大写
 ```

### center

```python
s = 'Content'
s = s.center(40, '-')
>>>>>>>>>>>>>>>>
out:----------------Content-----------------
```

### 字符串统计

```python
s = 'hello world'
print s.count('l')
>>>>>>>>>>>>>>>>
out:3
```

### 字符串切片

```python
str = '0123456789′
print str[0:3]      #截取第一位到第三位的字符
print str[:]        #截取字符串的全部字符
print str[6:]       #截取第七个字符到结尾
print str[:-3]      #截取从头开始到倒数第三个字符之前
print str[2]        #截取第三个字符
print str[-1]       #截取倒数第一个字符
print str[::-1]     #创造一个与原字符串顺序相反的字符串
print str[-3:-1]    #截取倒数第三位与倒数第一位之前的字符
print str[-3:]      #截取倒数第三位到结尾
print str[:-5:-3]   #逆序截取，截取倒数第五位数与倒数第三位数之间
```

### 字符串替换

```python
s = 'field__sum'
s = s.replace('__sum', '?')  # 将__sum替换为?
```



## map

`map(func, iterable)` 可以把`func`应用到`iterable`的所有元素上，python2返回一个list object。（python3返回一个迭代器序列）【例2】

## list

### 列表生成器

```python
# 先到 for x in range(10) 取元素，再把取出来的元素按照 前面的内容(x,x+1,x*2) 进行操作，然后把结果依次放到列表中

a = [x for x in range(10)]
print(a)
a = [x+1 for x in range(10)]
print(a)
a = [x*2 for x in range(10)]
print(a)
结果：
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
[0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10
```

### 列表一次添加多个元素

#### 加号

这块和字符串相加类似，同样是非常浪费资源的，因为必须创建一个新列表并将所有对象复制过去。推荐使用extend方法。

#### extend

```python
x1 = ['field1', 'field2', 'field3', 'field4']
x2 = ['new_field1', 'new_field2']
x1.extent(x2)  # 把列表2中的元素添加到列表1中（列表2依然存在，而且元素不变）
```



## 计时器

测试函数执行时间：

```python
from timeit import timeit
 
def func():
    s = 0
    for i in range(1000):
        s += i
    print s
 
# timeit(函数名, 运行环境，运行次数)
print timeit('func()', 'from __main__ import func', number=1000)
```



## 格式化

```python
s = "i am %s age %d" % ("alex", 18)
  
s = "i am %(name)s age %(age)d" % {"name": "alex", "age": 18}
  
s = "percent %.2f" % 99.97623
  
s = "i am %(pp).2f" % {"pp": 123.425556, }
  
s = "i am %.2f %%" % {"pp": 123.425556, }

s = "i am %s" % "alex"
```





## 内置函数

### enumerate

> tip: 遍历

```python
seq = ['first', 'second', 'third']

# 普通的遍历：
index = 0
for element in seq:
    print index, element
    index += 1

# 使用enumerate的遍历：
for i, element in enumerate(seq):
    print i, element
    
# enumerate返回一个[(index, element)...]
# Python 2.6版本以后，enumerate可以接收一个start参数，用来指定下标开始的值，默认从0开始
# eg: 下标从1开始
for i, element in enumerate(seq, start=1):
    print i, element
```

### filter

> tip: 过滤

```python
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
def is_odd(n):
    return n % 2 == 1
odds = filter(is_odd, nums) # filter返回一个列表，其中存储着令第一个参数可调用对象的值为True的元素

# 也可以用lambda表达式来写
odds = filter(lambda n: n % 2 == 1, nums)
```

### reduce

> tip: 累计
>
> 注：python3 reduce从全局对象命名空间移除，想要使用需要: from functools import reduce

```python
# reduce用来给列表中的元素迭代的应用一个可调用对象

# 逆置字符串
s = 'hello world'
s_r = reduce(lambda x, y: y + x, s)
```

## logging

单文件日志：

```python
import logging
 
logging.basicConfig(filename='testlog.log',     #指定往哪个文件里写
                    format='%(asctime)s - %(name)s - %(levelname)s -%(filename)s:  %(message)s',
                    level=logging.INFO
                    )
 
logging.debug('debug')
logging.info('info')
logging.warning('warning')
logging.error("error")
logging.fatal("fatal")
logging.critical('critical')

# 日志级别和数字的对应关系
# CRITICAL = 50
# FATAL = CRITICAL
# ERROR = 40
# WARNING = 30
# WARN = WARNING
# INFO = 20
# DEBUG = 10
# NOTSET = 0
```

日志记录格式：

![logging日志记录格式](C:\Users\搭错车\Desktop\Study Record\Python 记录\image\logging日志记录格式.png)

## requests

使用requests访问一个HTTP接口：

```python

import requests
import json

# 无参数 GET 请求
ret = requests.get('https://github.com/timeline.json') 
print ret.url
print ret.text
 
 
 
# 有参数 GET 请求
payload = {'key1': 'value1', 'key2': 'value2'}
ret = requests.get("http://httpbin.org/get", params=payload)
print ret.url
print ret.text

# 包含body的 POST 请求
payload = {'key1': 'value1', 'key2': 'value2'}
ret = requests.post("http://httpbin.org/post", data=payload)
print ret.url
print ret.text
 
 
# 包含header和body的 POST 请求
 
url = 'https://api.github.com/some/endpoint'
payload = {'some': 'data'}
headers = {'content-type': 'application/json'}
 
ret = requests.post(url, data=json.dumps(payload), headers=headers)

print(ret.text)
print(ret.cookies)

```

检测QQ号码是否在线：

```python
import urllib
import requests
from xml.etree import ElementTree as ET
 
# 使用内置模块urllib发送HTTP请求，或者XML格式内容
"""
f = urllib.request.urlopen('http://www.webxml.com.cn//webservices/qqOnlineWebService.asmx/qqCheckOnline?qqCode=424662508')
result = f.read().decode('utf-8')
"""
 
 
# 使用第三方模块requests发送HTTP请求，或者XML格式内容
r = requests.get('http://www.webxml.com.cn//webservices/qqOnlineWebService.asmx/qqCheckOnline?qqCode=424662508')
result = r.text
 
# 解析XML格式内容
node = ET.XML(result)
 
# 获取内容
if node.text == "Y":
    print("在线")
else:
    print("离线")
```





## 附录

【例1】

```python
# 普通函数
def square(x):
    return x * x
# lambda函数
square_l = lambda x : x * x

print square(2)
print square_l(2)

```

【例2】

```python
nums = [2, 4, 6, 8, 10]
nums_squared = map(lambda x: x*x, nums)  # lambda函数作为参数，map返回一个list对象
print type(nums_squared)
print nums_squared

# 要达到上面代码的目的，按照传统的写法可以这么写：
nums_squared = [num * num for num in nums]  # 列表生成器
print type(nums_squared)
print nums_squared
```

