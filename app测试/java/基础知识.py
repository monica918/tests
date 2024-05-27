## 变量赋值 要先定义数据类型  理解变量的声明、赋值和作用域
int
day = 3
String
str = "Hello";
List < String > list = new
ArrayList <> ()

Map < String, Integer > map = new
HashMap <> ()
boolean
result = (x == y);

控制流
理解条件语句（if 、 else if 、 else ）和循环语句（ for 、 while 、do- while ）的使用  理解 switch-case 语句的作用和使用场景

方法和函数
理解方法的声明和调用，包括方法参数和返回值

面向对象编程（OOP）
理解类和对象的概念，以及如何创建类和对象

异常处理：
理解
try-catch-finally 语句的使用，以及如何捕获和处理异常

集合框架：
理解常见的集合类型（List、Set、Map）及其特点和用法。
理解迭代器的使用和集合的遍历方法。


常用类库：
熟悉常用类库的使用，比如
String、Math、Date
等。
熟悉
Java
核心类库中的常用工具类，比如
Collections、Arrays、StringUtils
等。

静态语言：在编译时进行类型检查，即在代码编写阶段就检查变量的类型是否正确。如果类型不匹配或存在其他类型错误，编译器会发出错误提示，代码无法编译通过。
变量在声明时需要显式指定数据类型，编译器根据类型信息来分配内存空间和进行类型
通常更加严格和规范，对类型要求更加明确，可以减少一些错误，但也可能增加开发的复杂度。
由于类型检查和内存分配等操作是在编译时进行的，因此通常具有较高的运行效率。
Java、C、C + +
动态语言：在运行时进行类型检查，即在代码执行阶段才会检查变量的类型。因此，变量的类型可以在运行时动态改变，不需要提前声明或指定类型
变量的类型通常是根据赋值的内容自动推断的，不需要显式声明类型。
更加灵活，代码量通常较少，开发速度更快，但也可能导致一些类型相关的错误在运行时才能发现。
在运行时进行类型检查和内存分配，可能会导致一些性能损失，通常运行效率较低。
Python、JavaScript、Ruby

在
Java
中，Map
是一种接口（Interface），它代表着一种键值对（Key - Value）的数据结构，Map
接口定义了一组操作，用于在键和值之间建立映射关系，并提供了对这些映射关系进行操作的方法。
HashMap：基于哈希表实现的
Map，它提供了快速的插入、删除和查找操作。HashMap
允许空键和空值，并且不保证元素的顺序。
TreeMap：基于红黑树实现的有序
Map，它可以根据键的自然顺序或者自定义的比较器对键进行排序。TreeMap
中的键是有序的，按照键的升序排列。

Map
接口定义了一系列方法，用于操作
Map
中的键值对，包括：

put(key, value)：向
Map
中添加键值对。
get(key)：根据键获取对应的值。
containsKey(key)：判断
Map
中是否包含指定的键。
containsValue(value)：判断
Map
中是否包含指定的值。
remove(key)：根据键移除对应的键值对。
keySet()：获取
Map
中所有键的集合。
values()：获取
Map
中所有值的集合。
entrySet()：获取
Map
中所有键值对的集合。
在
Python
中，与
Java
中的
Map
相对应的概念是字典（Dictionary）。字典是一种键值对的数据结构，与
Map
类似，用于存储一组关联的键值对。

my_dict = {"name": "Alice", "age": 30, "city": "New York"}

{name = Alice, age = 30, city = New
York}

// 输出
Map
中的内容
System.out.println(myMap);

if (condition1) {
// 执行某些操作
} else if (condition2) {
// 执行另一些操作
} else {
// 执行默认操作
}

switch(expression)
{
    case
value1:
// 执行操作1
break;
case
value2:
// 执行操作2
break;
default:
// 默认操作
break;
}

public


class Main {
public static void main(String[] args) {
int month = 3;
String season;

if (month == 12 | | month == 1 | | month == 2) {
season = "冬季";
} else if (month == 3 | | month == 4 | | month == 5) {
season = "春季";
} else if (month == 6 | | month == 7 | | month == 8) {
season = "夏季";
} else if (month == 9 | | month == 10 | | month == 11) {
season = "秋季";
} else {
season = "无效的月份";
}

System.out.println("这个月份对应的季节是：" + season);
}
}


public


class Main {
public static void main(String[] args) {
int day = 3;
String dayString;

switch (day) {
case 1:
    dayString = "星期一";


    break;
case
2:
dayString = "星期二";
break;
case
3:
dayString = "星期三";
break;
case
4:
dayString = "星期四";
break;
case
5:
dayString = "星期五";
break;
case
6:
dayString = "星期六";
break;
case
7:
dayString = "星期日";
break;
default:
dayString = "无效的日期";
break;
}

System.out.println("今天是：" + dayString);
}
}


switch
语句：用于根据表达式的值匹配多个可能的情况，并执行相应的操作
if - else 结构可以处理任何类型的条件表达式，例如布尔表达式、比较表达式等。
switch
结构的表达式必须是整数类型（byte、short、int、char）或枚举类型。

switch
结构不能直接处理字符串类型的表达式
String
color = "red";

switch(color)
{
    case
"red":
System.out.println("红色：停车");
break;
错误

String
color = "red";

if (color.equals("red")) {
System.out.println("红色：停车");  正确

因为 switch 结构不能处理字符串类型的表达式。所以在处理字符串类型的条件判断时， if - else 结构是更合适的选择。

public


class Main {
public static void main(String[] args) {
// 定义一个整数数组
int[] numbers = {1, 2, 3, 4, 5};

// 遍历数组并打印每个元素
for (int i = 0; i < numbers.length; i++) {
System.out.println(numbers[i]);
}
}
}


