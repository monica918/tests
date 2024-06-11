$ sudo docker pull <image:tag>  下载镜像
$ sudo docker images 列出本地的所有镜像
$ sudo docker rmi <image-id/image-name:tag>：删除指定的镜像。
$ sudo docker push 镜像名  推送镜像
$ sudo docker build -t image-name:tag .：基于当前目录下的 Dockerfile 构建镜像 -t是指定镜像标签


docker run [-d|-it] [-p hostPort:containerPort] [--name container-name] <image:tag> [command]：创建并启动容器，常用选项包括 -d（后台运行）、-it（交互式终端）、-p（端口映射）和 --name（指定容器名）
创建容器的常用参数
参数 	描述
-i 	交互式创建容器
-t 	分配一个伪终端
-d 	运行容器到后台
-e 	设置环境变量
-p 	映射容器端口到主机
-h 	设置容器主机名
--link 	添加连接到另一个容器
--network 	连接容器到一个网络
-v 	挂载宿主机目录到容器
--restart 	容器退出后的重启策略，默认no[always|failure]
--name 	给容器命令

使用 docker run 是创建并启动一个新容器的完整过程，适用于首次运行或者每次都需要新容器的情况。
使用 docker start 是用来重启一个已经存在的容器，适用于容器配置不变，只需要再次运行的场景。


$ sudo docker start|stop|restart｜rm <container-id/container-name>：启动、停止或重启容器。

docker container logs 容器名/ID    查看运行的容器的日志
$ sudo docker container ls  查看容器列表
$ sudo docker container exec -it 容器名/ID command   在运行的容器中执行命令
$ sudo docker container rm 容器名/ID   删除一个容器
docker exec -it <container-id/container-name> bash/sh：进入运行中的容器并启动交互式shell。

docker-compose up -d  命令启动服务
docker-compose stop    停止服务可以使用命令
docker-compose down --volumes  使用down命令删除所有，完全删除容器。通过——volumes来删除Redis容器使用的数据卷

日志与数据
    docker logs <container-id/container-name>：查看容器的日志输出。
    docker cp <container-id>:<src-path> <destination-path>：从容器中拷贝文件或目录到本地，反之亦然。
    
网络管理

    docker network ls：列出所有网络。
    docker network create <network-name>：创建自定义网络。
    docker network connect|disconnect <network-name> <container-id/container-name>：连接或断开容器与网络的连接。


信息与诊断

    docker inspect <container-id/container-name>：查看容器或镜像的详细信息。
    docker stats <container-id/container-name>：显示容器资源使用统计。


Docker让你能够构建和运行容器，而Kubernetes帮助你高效地管理和编排这些容器，特别是在分布式和大规模部署的场景下。两者常常一起使用，Docker作为基础容器平台，Kubernetes作为容器管理的上层编排系统










