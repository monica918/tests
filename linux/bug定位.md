## 项目出现bug，怎么查看日志
- 定位问题，查看是哪个模块/功能的bug
- 查看相关模块/功能的log文件（每个模块的日志文件通常会按照模块的名称或标识进行命名，以便于区分和查找。例如，订单处理模块的日志可能存储在一个名为"order.log"的日志文件中，库存管理模块的日志存储在"inventory.log"文件中，支付系统的日志存储在"payment.log"文件中，每个模块会有自己的日志记录器，将日志输出到指定的日志文件中）
- 过滤关键字
- 提交给开发


## 日志错误关键字
- Error: 表示发生了一个错误。
- Exception: 表示发生了异常情况。
- Failed: 表示操作或任务失败。
- Warning: 表示发出了一个警告信息。
- Segmentation fault: 表示出现了段错误，通常指向程序的内存访问问题。
- Permission denied: 表示权限被拒绝，通常指向文件或目录权限设置问题。
- Connection refused: 表示连接被拒绝，通常指向网络连接问题。
- Invalid argument: 表示提供了无效的参数或参数格式错误。
- File not found: 表示文件不存在，通常指向文件路径或名称错误。
- Out of memory: 表示内存不足，通常指向内存资源耗尽问题。
- Fatal: 表示致命错误，通常指向无法继续执行的严重问题。
- Timeout: 表示操作超时，通常指向操作在规定时间内未完成。
- Network error: 表示网络错误，通常指向与网络通信相关的问题。
- Database error: 表示数据库操作错误，通常指向与数据库连接或查询有关的问题。
- Input/output error: 表示输入或输出错误，通常指向文件读写或设备访问问题。
- Assertion failed: 表示断言失败，通常指向代码逻辑错误或测试失败。
- Configuration error: 表示配置错误，通常指向配置文件或参数设置问题。
- Internal server error: 表示服务器内部错误，通常指向应用程序或服务的异常状态。
