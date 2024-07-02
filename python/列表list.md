]




# 使用 index() 查找元素位置
index_of_3 = numbers.index(3)  # 2

# 使用 count() 统计元素出现次数
count_of_2 = numbers.count(2)  # 1






列表推导式
列表推导式是一种简洁的创建列表的方法。
# 创建一个平方数列表
squares = [x**2 for x in range(6)]  # [0, 1, 4, 9, 16, 25]

# 带条件的列表推导式
even_squares = [x**2 for x in range(6) if x % 2 == 0]  # [0, 4, 16]



# 使用 list() 函数复制
copied_list = list(original_list)  # [1, 2, 3]

# 使用 copy() 方法复制（Python 3.3+）
copied_list = original_list.copy()  # [1, 2, 3]

列表长度
numbers = [1, 2, 3, 4, 5]

# 使用 len() 函数获取列表长度





