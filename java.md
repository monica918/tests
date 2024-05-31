基本数据类型（Primitive Data Types）
基本数据类型：byte, short, int, long, float, double, char, boolean
引用数据类型：类、接口、数组、枚举

创建列表
List<String> arrayList = new ArrayList<>();

添加元素
添加单个元素
arrayList.add("Alice");
arrayList.add("Bob");

添加所有元素
List<String> newNames = new ArrayList<>();
newNames.add("Charlie");
newNames.add("David");
arrayList.addAll(newNames);

访问元素
根据索引访问
String name = arrayList.get(0); // 获取第一个元素

修改元素
arrayList.set(1, "Bob Jr."); // 修改索引为1的元素

删除元素


