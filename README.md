# Python 2.7.5 笔记

> 注：此文档是本人在学习和使用Python2进行工程实践中所用到的一些语法/技巧
>
> by：aideny

## lambda

lambda关键字是用来创建内联函数的，调用方式和普通的函数相同。【例1】

优势：

- 可以快速声明，所以用来做回调函数非常理想，和map、filter、reduce这样的函数搭配使用尤其有效。【例2】

  

## str



## map

`map(func, iterable)` 可以把`func`应用到`iterable`的所有元素上，python2返回一个list object。（python3返回一个迭代器序列）【例2】

## list







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
nums_squared = [num * num for num in nums]
print type(nums_squared)
print nums_squared
```

