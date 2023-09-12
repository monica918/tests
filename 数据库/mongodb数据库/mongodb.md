MongoDB:主要解决海量数据的访问效率问题。
MongoDB:最类似关系型数据库，支持的查询语言非常丰富。
MongoDB:遵循文档数据模型，它将数据存储为序列化的二进制 JSON（BSON）文档。最大文档大小为 16MB。


## MySQL
MySQL是固定和结构化的数据模式，在存储任何数据之前，MySQL强制要求预先确定如何组织表和列，更改数据模式需要仔细地重新考虑数据库的DDL（数据定义语言）和DML（数据建模语言）。在可靠性/数据一致性/安全上，MySQL还是超过了MongoDB.MySQL用于具有固定数据模式且不打算在数据多样性方面扩展太多的企业或项目
在MySQL中，由于数据模式受到更大的约束，所以表中的每一行都需要相同的列，这在使用大容量数据库时尤其难以管理。因此，MySQL不能像MongoDB那样轻松地处理大型和复杂的数据库。


## MongoDB
在处理大量复杂数据时，MongoDB文档数据库优于MySQL关系数据库。MongoDB 的架构对于扩展大型数据卷非常有用，因为它可以根据磁盘空间提高容量。数据量比较大，采用MongoDB，百万级的数据，千万级、亿级。查询语法非常丰富，嵌套文档查询功能非常强大，不是重度用户可能不能理解
每个MongoDB数据库都包含集合，集合中依次填充了文档。这些文档可以包括各种字段和信息类型，从而可以存储内容和大小不同的文档的数据。
MongoDB是正在成长但数据架构不稳定的业务或项目的最合适选择（业务经常变动，需要不时的添加字段/嵌套文档，业务数据比较复杂，适合嵌套文档式存储）。MongoDB的非关系数据性质允许自由使用和存储文档而无需使用结构，从而使其易于更新和查询。MongoDB通常用于需要内容管理，处理IoT（物联网），执行实时分析等的项目中。



MongoDB语法与现有关系型数据库SQL语法比较
 1MongoDB语法            MySql语法
 2
 3db.test.find({'name':'foobar'})             <==>          select * from test where name='foobar'
 4
 5db.test.find()                                      <==>          select *from test
 6
 7db.test.find({'ID':10}).count()             <==>          select count(*) from test where ID=10
 8
 9db.test.find().skip(10).limit(20)          <==>          select * from test limit 10,20
10
11db.test.find({'ID':{$in:[25,35,45]}})     <==>          select * from test where ID in (25,35,45)
12
13db.test.find().sort({'ID':-1})                 <==>          select * from test order by IDdesc
14
15db.test.distinct('name',{'ID':{$lt:20}}) <==>          select distinct(name) from testwhere ID<20
16
17db.test.group({key:{'name':true},cond:{'name':'foo'},reduce:function(obj,prev){prev.msum+=obj.marks;},initial:{msum:0}})     <==>     select name,sum(marks) from testgroup by name
18
19db.test.find('this.ID<20',{name:1})    <==>           select name from test whereID<20
20
21db.test.insert({'name':'foobar','age':25})    <==>       insertinto test ('name','age') values('foobar',25)
22
23db.test.remove({})                                     <==>       delete * from test
24
25db.test.remove({'age':20})                        <==>       delete test where age=20
26
27db.test.remove({'age':{$lt:20}})                <==>        delete test where age<20
28
29db.test.remove({'age':{$lte:20}})              <==>        delete test where age<=20
30
31db.test.remove({'age':{$gt:20}})              <==>         delete test where age>20
32
33db.test.remove({'age':{$gte:20}})            <==>         delete test where age>=20
34
35db.test.remove({'age':{$ne:20}})             <==>         delete test where age!=20
36
37db.test.update({'name':'foobar'},{$set:{'age':36}})<==> update test set age=36 where name='foobar'
38
39db.test.update({'name':'foobar'},{$inc:{'age':3}})<==> update test set age=age+3 where name='foobar'
40
41模糊查询：$regex
42
43db.test.find({"name":{$regex:"aaa"}})
44
45分组个数过滤
46
47db.getCollection('id_mapper').aggregate([{$group:{ _id :"$contract_id",count:{$sum:1}}},{$match:{count:{$gt:1}}}])
48
49判断是否为空
50
51db.getCollection('id_mapper').find({"sinocardid":{$in:[null]}})