## vue是个js框架/脚手架
## 基本原理（虚拟dom+响应式数据）
- 数据绑定：数据与dom绑定关系，数据变，dom变
- 声明式渲染：通过v-if/v-for等模板语法来声明期望的dom结构
- 组件式开发：组件可以复用和嵌套

## vue项目模块
- api 调接口的
- assets 静态文件夹
- components 通用组件
- views 视图（特定页面组件）
- router 路由
- store 共享数据
- app.vue 根组件
- main.js 入口文件

## 组件分为三部分：模板/逻辑/样式

## 模板
- 指令：v-xxx都是指令
- 表达式：
1.插值表达式：{{name}}/{{name+''+age}}  
2.计算属性：:data=fullname   fullname是属性名
2.方法：    :data=getname()   
- 静态内容：固定文本，不需要计算的

## 指令语句
- v-model   双向数据绑定
- :data/:href  单向绑定（动态数据/动态属性）
- @click   绑定事件
- v-if   条件渲染
- v-for  列表渲染
- v-show 是否展示

## dom
- 元素节点
- 属性节点
- 文本节点
- 注释节点
- 文档节点：整个html

## 逻辑: export default组成部分
- data()
- components
- methods
- computed
- watch()
- created()
- mounted()

