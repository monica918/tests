import mysql.connector

# 连接到 MySQL 数据库
connection = mysql.connector.connect(
    host="test-mysql.starcharge.cloud",
    user="test_platform1",
    password="PzALthi89",
    database="star_platform_order_7"
)

# 创建一个数据库游标
cursor = connection.cursor()

# 执行 SQL 查询
query = "select id from t_order_info_20 GROUP BY CREATE_TIME  DESC limit 101;"
cursor.execute(query)

# 获取查询结果
result = cursor.fetchall()

# 打印结果
for row in result:
    print(row)

# 关闭游标和连接
cursor.close()
connection.close()