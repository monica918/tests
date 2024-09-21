# 创建Dockerfile，创建镜像
Dockerfile 是一个文本文档，其中包含组装 Docker 映像的指令。当我们通过执行docker build 命令告诉 Docker 构建我们的镜像时，Docker 会读取这些指令，执行它们，并因此创建一个 Docker 镜像。
用于 Dockerfile 的默认文件名是Dockerfile（没有文件扩展名）。使用默认名称允许您运行docker build命令而无需指定其他命令标志。
使用docker build命令来构建我们的镜像

FROM python:3.8-slim-buster

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]

# 创建docker-compose，定义服务
就是批量部署容器，并自动构建镜像，处理依赖和通信的工具。只需要在一个YAML文件中配置好应用程序的服务，然后通过docker-compose命令就可以创建并启动配置中的所有服务

使用docker-compose有三个基本步骤：

1。在Dockerfile中定义好你的应用程序的环境，以便在任何地方它都可以复制。
2。在docker-compose.ymal中定义组成应用程序的服务，以便它们可以在一个独立的环境中一起运行。
3。运行docker-compose up, docker-compose命令会启动并运行整个应用程序。

Docker Compose依赖于Docker Engine来完成任何有意义的工作，所以请确保在本地或远程安装Docker Engine。


version: "3.9"  # optional since v1.27.0
services:
  web:
    build: .
    ports:
      - "5000:5000"
    volumes:
      - .:/code
      - logvolume01:/var/log
    links:
      - redis
  redis:
    image: redis
volumes:
  logvolume01: {}
  
# docker运行
docker-compose up -d
