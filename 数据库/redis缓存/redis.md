数据库（冰箱）：数据存在磁盘上，容量大，读取速度慢，数据稳定，断电可保存数据，可以长期保存，适合写入数据
redis（工作台）：数据存在内存上，容量小，可以设置过期时间自动清理数据，读取速度快，断电不保存数据，不适合长期保存数据，适合读取不适合写入数据


redis连接：host，port（默认端口6379），password（不需要用户名）

redis是键值对，搜索键来查询值

## Redis 的值可以是以下五种数据类型之一：
- 字符串（String）：最常见的数据类型，可以存储文本、二进制数据等。
SET key "Hello, World!"

- 列表（List）：有序的字符串列表，可以用于实现队列或者栈等数据结构。
LPUSH fruits "apple"
LPUSH fruits "banana"

- 集合（Set）：无序的字符串集合，支持交集、并集等操作。
SADD colors "red"
SADD colors "green"

- 有序集合（Sorted Set）：类似于集合，但每个元素都有一个关联的分数，可以用于排行榜等场景。
ZADD scores 95 "Alice"
ZADD scores 88 "Bob"

- 哈希表（Hash）：键值对的集合，适合存储对象的多个属性。
HSET user:1 name "Alice"
HSET user:1 age 25
HSET user:1 city "New York"



## TTL：过期时间，-1表示永不过期，-2表示已经过期  
在 Redis 中，TTL 是 "Time To Live" 的缩写，表示键（key）的存活时间或过期时间。TTL 是一个用于控制键在 Redis 中存储多长时间的值，以秒为单位。
TTL 在 Redis 中非常有用，它可以用于实现缓存、自动清理过期数据、限时任务等各种功能。通过设置适当的 TTL，你可以根据数据的生命周期来管理 Redis 中的键。
你可以使用 Redis 的 TTL 功能来创建定时任务，而键的值可以为空，仅用于表示任务的存在和过期时间。



