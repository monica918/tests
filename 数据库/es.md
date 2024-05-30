GET starcharge_baseinfo_stubgroup/_doc/pjjqpw1v-bpk9032s-m9h7ckiv-pwroi38g/_source

GET：HTTP方法，用于获取资源。
starcharge_baseinfo_stubgroup：索引名称。
_doc：文档类型，在Elasticsearch 7.0及以后版本中统一使用。
pjjqpw1v-bpk9032s-m9h7ckiv-pwroi38g：文档ID，唯一标识索引中的一个文档。
_source：用于获取文档的源数据。
这个请求将返回 starcharge_baseinfo_stubgroup 索引中 ID 为 pjjqpw1v-bpk9032s-m9h7ckiv-pwroi38g 的文档的源数据。

在Elasticsearch中，可以将索引（Index）类比为数据库中的表（Table），而将文档（Document）类比为表中的一条数据（Row）。

具体来说：

索引（Index）：在Elasticsearch中，索引是用于存储和组织相关数据的逻辑容器，类似于数据库中的表。每个索引都包含了一组相关的文档，并且具有特定的设置和映射（Mapping）。

文档（Document）：文档是Elasticsearch中存储的基本数据单元，类似于数据库表中的行。每个文档都是一个JSON对象，包含了多个字段和对应的值。文档在索引中存储、检索和分析。

为什么要用Elasticsearch来查询数据？
全文搜索和分析：Elasticsearch专注于全文搜索和实时分析，可以快速地搜索和分析大规模的文本数据，包括结构化、半结构化和非结构化数据。

实时性：Elasticsearch提供实时搜索和分析能力，使得用户可以立即查询最新数据，支持实时监控、实时报告等应用场景。

分布式架构：Elasticsearch采用分布式架构，能够水平扩展，支持处理大规模数据，具有高可用性和容错性。

强大的查询功能：Elasticsearch提供了丰富的查询DSL（Domain Specific Language），支持多种查询类型和聚合功能，可以灵活地构建复杂的查询和分析。

可扩展性：Elasticsearch支持插件和定制化功能，可以根据需求扩展和定制搜索和分析功能，满足不同业务场景的需求。

