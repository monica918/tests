## jdk安装
- jenkins是纯java编写的，要先安装jdk
- jenkins依赖的jdk，需要版本11.0及以上，已经不支持jdk8.0了
- jdk可以本地手动下载，然后scp上传到远程机，也可以直接在远程机wget下载，但是因为jdk还需要配置环境变量等操作，更推荐手动下载
- 下载后scp上传到远程机后，tar命令进行解压
- 配置环境变量，配置后source命令生效
- java -version 验证java版本


## jenkins安装
- 登陆远程机，wget命令下载jenkins.war包
- 在阿里云控制台安全组开放8080端口
- cd到jenkins.war目录下，运行java -jar jenkins.war命令来启动jenkins服务
- 远程机终端出现 Jenkins is fully up and running 说明jenkins服务启动成功
- 在本地浏览器输入  http://远程机ip:8080，出现jenkins界面
- 首次登陆，用户名是admin，密码是jenkins给的密码，需要自己进入jenkins重新设置密码
- 设置jenkins汉化版


## 分布式部署(这种配置允许在大规模或复杂的软件开发环境中有效地处理任务，提高效率和资源利用率)
- 主服务器（Master）(部署在远程服务器上的)：  
  - 这是Jenkins的中心控制节点，负责处理用户的请求、管理任务和配置，以及维护整个Jenkins系统。  
  - 主服务器本身并不执行任务，它主要负责分发任务到其他节点。
  - 在主服务器上，您需要安装Jenkins软件（通常是通过安装jenkins.war文件）和Java。Jenkins主服务器运行在Web容器中，如Tomcat或Jetty，以便提供Web界面和处理用户请求。  
- 代理节点（Agent）：  
  - 节点是指Jenkins分布式部署中的一个独立计算机，可以用于执行主服务器发过来的构建任务。  
  - 如果您需要将自己的电脑作为Jenkins的节点来执行任务，您需要在本地安装Jenkins代理（Jenkins Agent）。代理是Jenkins的一个组件，可以让您的本地计算机作为Jenkins分布式部署的一部分，用于执行任务。
  - 在代理节点上，您只需要安装Java，而不需要安装Jenkins本身。代理节点通过运行Jenkins代理的agent.jar文件与主服务器建立连接，并接收任务指令进行执行。  
- 总结起来：
  - 主服务器需要安装Jenkins软件（jenkins.war）和Java，用于管理任务和提供Jenkins的Web界面。  
  - 代理节点只需要安装Java，用于执行来自主服务器的构建任务，不需要安装Jenkins本身。  
  - 通过这样的分布式部署，Jenkins可以在主服务器和多个代理节点之间分发任务，实现任务的并行处理，提高构建效率和资源利用率。
- 节点执行任务：
  - 在分布式部署中，每个节点可以执行不同的任务，也可以执行相同的任务，这取决于您的具体需求和配置。
  - 每个节点执行不同的任务：在一些情况下，您可能希望将不同类型的任务分发给不同类型的节点。例如，您可能有一些节点专门用于构建和测试前端代码，另一些节点用于构建和测试后端代码，还有一些节点用于部署应用程序或执行其他特定任务。这样做的好处是可以根据节点的特性和资源来优化任务分发，提高效率和并行处理能力。
  - 每个节点执行相同的任务：在其他情况下，您可能希望在所有节点上执行相同的任务，以实现负载均衡和容错。例如，如果您有多个相同配置的节点，您可以在所有节点上配置相同的Jenkins代理，并将相同的构建任务分发给所有节点。这样可以平衡节点的负载，确保即使某些节点不可用，任务仍然可以在其他节点上继续执行。
- 登陆jenkins：运维人员在远程服务器上配置好Jenkins后，提供给您一个账号，让您可以在本地登陆Jenkins，这是通过Jenkins的Web界面实现的。
  - （注意：这并不代表我的电脑是节点，节点电脑是执行任务的，我的电脑只是通过web界面化进入jeenkins工作）
- 项目代码放置位置：
  - 在Jenkins中，构建项目的代码通常被保存在Git等版本控制系统中。这样做的好处是，代码能够得到版本控制、管理和跟踪，团队成员可以协同开发，而且构建任务可以自动地从版本控制系统中获取最新代码进行构建。
  
## 新建jenkins项目
- 项目概述
- 源码管理（git）
- 构建的触发器（重点在触发器，什么时候触发构建动作）  
  - 时间构建，设定好定时
  - 代码构建，代码提交或者代码合并时构建（先在Jenkins的触发器中勾选"GitHub hook trigger for GITScm polling"选项，再去Git仓库中配置Webhook。这样Jenkins将设置为等待来自Git仓库的Webhook通知。当有新的代码提交或代码变更时，Git仓库会向Jenkins发送Webhook通知，触发构建任务。）
- 构建步骤（构建命令，分为windows和linux命令）
- 构建后操作（发邮件等）


## 配置地址补充说明
- allure-reports(报告目录)/run.py 都要放在项目根目录下，这样在jenkins配置地址的时候，不需要加路径，直接写命令，比如python run.py   
- 报告是先存到项目代码里的，然后jenkins从项目代码里把报告取出来，进行后续展示或者发送到邮件里。(所以报告的地址要与项目里一致)

## 持续集成
- 旨在将开发人员的代码频繁集成到主干代码库中，然后自动进行构建和测试。在持续集成中，开发人员通常会提交代码到共享的版本控制系统（如Git），当有新的代码提交/代码合并到dev/test/release分支时，持续集成服务器会自动触发构建和测试过程（单元测试等）。

## 持续交付
- 持续交付包括持续集成，持续交付是在持续集成的基础上发展的，它扩展了持续集成的概念，将持续集成的构建和测试阶段进一步扩展到预生产环境的部署阶段，配置了持续交付就不需要配置持续集成了。
- 持续交付意味着代码经过自动构建和测试后，可以随时部署到生产环境，但需要手动触发部署过程。（这意味着开发团队或运维团队需要主动执行一系列操作，如点击按钮或运行命令，以便将代码部署到生产环境。）

## 持续部署
- 持续部署包括持续集成，持续部署是在持续集成的基础上发展的，它扩展了持续集成的概念，将持续集成的构建和测试阶段进一步扩展到预生产环境的部署阶段，配置了持续部署就不需要配置持续集成了。
- 意味着代码通过自动构建和测试后，可以自动部署到生产环境，无需手动干预。（整个部署过程不需要等待人工干预，一旦代码通过了所有测试，并满足部署的条件，它会自动被部署到生产环境。）

## pipeline项目/freestyle项目
- 流水线（Pipeline）项目，适用于持续交付/持续部署
- 流水线项目是为了实现持续且自动化的软件交付流程。流水线是指将软件开发过程分为一系列连续的阶段，并且每个阶段都与下一个阶段紧密衔接，从而形成一个连续的流程，类似于生产线上的流水线。  
流水线的设计允许软件代码在经过自动构建、自动测试和自动部署等多个连续的阶段，最终能够自动交付给用户或预生产环境。流水线的每个阶段都应该自动化，以确保代码的质量和稳定性，并实现持续的软件交付。
- 自由风格（freestyle）项目，适用于持续集成