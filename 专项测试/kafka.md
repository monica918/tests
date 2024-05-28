- 应用于分布式，是多服务与多服务之间的通信，一个服务可以发布多个topic，一个topic也可以被多个服务订阅
- 但是不是服务与服务直接通信，而是引入了一个中间件(kafka),生产服务生产数据，并把数据（key+json）发送给topic下的分区，消费服务从分区里获取数据并进行相关处理
- 生产服务通过数据里的key来决定发送到哪个分区里
- topic是个逻辑概念，用来组织和归类类似消息的（类似于给消息起个名字），同一类型的数据都是同一个topic，不是物理概念，不能存储数据，存储数据是在分区里，消费者通过订阅topic来获取数据
- 分区可以实现分布在不同的服务器上，生产者将数据存储在主题下的不同分区里面
- 一条消息可能带有以下几个数据：1.主题 2.分区 3.键 4.值(想传送的数据)

那消费者如何读取数据呢？引出偏移量
偏移量（offset）：第几个
一个分区里面，每个消息的偏移量都是唯一的
消费者只能顺序读取

Broker是Kafka集群中的一个节点（服务器），它的主要职责是接收来自生产者的消息、存储这些消息并提供给消费者。Kafka集群通常由多个Broker组成，每个Broker都有一个唯一的ID
Broker存储消息数据，数据被分为多个Topic，每个Topic又被分为多个分区（Partition）。
Topic：消息的类别或名称，Kafka中的消息按Topic进行分类。
Partition：每个Topic分为多个分区，消息在分区中是有序的，分区可以分布在不同的Broker上。


kafka作为服务间的数据流转载体，有发送-消费-处理三个阶段
服务a：发送message到topic 
服务b：消费(接受)topic里的message，并进行相关业务处理，比如解析数据/更改状态/把message里的数据提取出来放到其他topic里，再发送给服务c


项目背景：
某些Broker可能会因为特定Topic或分区的高流量而负载过重。通过迁区，可以将分区从负载较重的Broker迁移到负载较轻的Broker，从而实现集群负载的均衡。
当现有的Kafka集群无法再支持当前或预期的工作负载时，需要迁移到一个更大或更强的集群
怎么测kafka迁区
1。触发topic发送
2。kafka源集群查看是否有该topic的发送/消费记录（应该查不到）
3。kafka目标集群查看是否有该topic的发送/消费记录（应该可以查到），并且topic的数据核对正常。


集群示例
假设你有一个包含3个Broker节点的Kafka集群，它们的ID分别是1、2和3。这些Broker节点可以运行在3台独立的服务器上，如下所示：

Broker 1（Server 1）：负责处理Topic A的Partition 0的Leader副本和Topic B的Partition 1的Follower副本。
Broker 2（Server 2）：负责处理Topic A的Partition 1的Leader副本和Topic B的Partition 0的Follower副本。
Broker 3（Server 3）：负责处理Topic A和Topic B的其他副本。
Kafka集群的工作示例
生产者发送消息：

生产者将消息发送到Topic A，Kafka根据分区策略将消息分配到不同的分区，如Partition 0和Partition 1。
Broker存储消息：

Broker 1存储Topic A的Partition 0的消息。
Broker 2存储Topic A的Partition 1的消息。
Broker 3存储这些分区的副本。
消费者读取消息：

消费者从Kafka集群中读取Topic A的消息，Kafka集群会将读取请求路由到相应的Broker上，由负责对应分区的Broker提供消息。







