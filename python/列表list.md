Python 列表（list）是一个有序的、可变的集合，可以包含任意类型的元素。以下是 Python 列表的相关知识点和用法：
访问和修改元素
a.索引访问
numbers = [1, 2, 3, 4, 5]

# 访问元素
first_element = numbers[0]  # 1
last_element = numbers[-1]  # 5

# 修改元素
numbers[0] = 10  # [10, 2, 3, 4, 5]
b. 切片访问
numbers = [1, 2, 3, 4, 5]

# 获取子列表
sublist = numbers[1:4]  # [2, 3, 4]
sublist_from_start = numbers[:3]  # [1, 2, 3]
sublist_to_end = numbers[2:]  # [3, 4, 5]

# 步长切片
every_second_element = numbers[::2]  # [1, 3, 5]
reversed_list = numbers[::-1]  # [5, 4, 3, 2, 1]

列表操作
a. 添加元素
numbers = [1, 2, 3]

# 使用 append() 添加单个元素
numbers.append(4)  # [1, 2, 3, 4]

# 使用 extend() 添加多个元素
numbers.extend([5, 6])  # [1, 2, 3, 4, 5, 6]

# 使用 insert() 在指定位置插入元素
numbers.insert(1, 1.5)  # [1, 1.5, 2, 3, 4, 5, 6]

b. 删除元素
numbers = [1, 2, 3, 4, 5]

# 使用 remove() 删除指定元素
numbers.remove(3)  # [1, 2, 4, 5]

# 使用 pop() 删除指定位置的元素并返回它
last_element = numbers.pop()  # 5, [1, 2, 4]
first_element = numbers.pop(0)  # 1, [2, 4]

# 使用 del 关键字删除指定位置的元素
del numbers[1]  # [2]
c. 查找元素
numbers = [1, 2, 3, 4, 5]

# 使用 index() 查找元素位置
index_of_3 = numbers.index(3)  # 2

# 使用 count() 统计元素出现次数
count_of_2 = numbers.count(2)  # 1

列表排序
a. 使用 sort() 方法排序列表（原地排序）
numbers = [4, 2, 5, 1, 3]

# 升序排序
numbers.sort()  # [1, 2, 3, 4, 5]

# 降序排序
numbers.sort(reverse=True)  # [5, 4, 3, 2, 1]

b. 使用 sorted() 函数排序（返回新列表）
numbers = [4, 2, 5, 1, 3]

# 升序排序
sorted_numbers = sorted(numbers)  # [1, 2, 3, 4, 5]

# 原列表不变
print(numbers)  # [4, 2, 5, 1, 3]

列表推导式
列表推导式是一种简洁的创建列表的方法。
# 创建一个平方数列表
squares = [x**2 for x in range(6)]  # [0, 1, 4, 9, 16, 25]

# 带条件的列表推导式
even_squares = [x**2 for x in range(6) if x % 2 == 0]  # [0, 4, 16]

列表合并
original_list = [1, 2, 3]

# 使用切片复制
copied_list = original_list[:]  # [1, 2, 3]

# 使用 list() 函数复制
copied_list = list(original_list)  # [1, 2, 3]

# 使用 copy() 方法复制（Python 3.3+）
copied_list = original_list.copy()  # [1, 2, 3]

列表长度
numbers = [1, 2, 3, 4, 5]

# 使用 len() 函数获取列表长度
length = len(numbers)  # 5

检查元素是否存在
numbers = [1, 2, 3, 4, 5]

# 使用 in 运算符检查元素是否存在
is_in_list = 3 in numbers  # True
is_not_in_list = 6 not in numbers  # True

列表反转
numbers = [1, 2, 3, 4, 5]

# 使用 reverse() 方法原地反转
numbers.reverse()  # [5, 4, 3, 2, 1]

# 使用切片反转
reversed_numbers = numbers[::-1]  # [1, 2, 3, 4, 5]

