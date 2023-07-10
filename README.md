# 苏州教到

## Members:
- UI设计 周璇
- 开发工程师 顾天宇，夏春秋
- 产品经理 原明清
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

Vscode Ctrl + Shift + P  然后搜索 Python: Select Interpreter 点击那个带星号的（也就是之前的虚拟环境)
