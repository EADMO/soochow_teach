# 苏州教到

## Members:
- UI设计 周璇
- 开发工程师 顾天宇，夏春秋
- 产品经理 原明清 (真正的神)
- 测试 李琳炜
- 运维 段欣江

## 环境配置

- _先把该仓库fork到你的个人底下_

- 点击项目右上角的 fork 然后一路确定

```bash
# 在此之前，cd一个目录下准备放这个项目
#  例: (Prog 文件夹必须已经创建)
cd D:/Prog/

# 从github拉取仓库 (这里<user-ID> 就是你的 ID)
git clone https://github.com/<user-ID>/soochow_teach.git

# 切换到soochow_teach 目录下
cd ./soochow_teach/

# 创建并运行 python 虚拟环境
python -m venv ./venv
.\venv\Scripts\activate     # for Windows
```

安装依赖

```bash
(venv)$ pip install -r requirements.txt
```

至此，你已经把环境弄好了

如果使用VsCode的话，需要去配置一下Python Interpreter: 

*这一步不需要启动虚拟环境*

首先点击 VsCode 左上角文件，打开对应的Soochow_Teach文件夹 (不是codes里的) _过程有点不好讲

Vscode Ctrl + Shift + P  然后搜索 Python: Select Interpreter 点击那个带星号的（也就是之前的虚拟环境)

## 更新后的重新 pull

到自己fork的仓库里 点sync 确认同步

然后回到自己的那个目录底下 e.g. D:\Prog\soochow_teach>

输入

```bash
git pull
```

就自动完成同步了

## 上传和 Pull Requeset

利用Vscode的Source Control (左边选项框第三个-前提装了git插件) 点击commit,然后一路确定

回到你个人fork的仓库，点击Contribute - Open PullRequset

然后可以自己同意，也可以等别人看了之后确认Pullrequest

更多内容去看老师那边的参考文件

## 如何运行Django

在Vscode 里打开终端 Ctrl + Shift + `(Esc下面那个) 这时候应该自动启动了虚拟环境

先CD到codes文件夹下 e.g. D:Prog\soochow_teach\codes>
```bash
cd codes
```

然后执行

```bash
python manage.py runserver
```

这时候服务器就启动了 访问127.0.0.1:8000 来查看 index.html

127.0.0.1:8000/base 来查看base.html
