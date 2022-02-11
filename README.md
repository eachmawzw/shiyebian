1、安装python3

2、安装pipenv

注：如果安装太慢，可以更换国内源（如更换为阿里源：<code>pip config set global.index-url https://mirrors.aliyun.com/pypi/simple/</code>）


```
$  python3 -m pip install pipenv
```

3、进入到项目目录，安装依赖

注：如果系统的python版本不是3.7，修改 Pipfile 文件，将 python_version = "3.10.2" 修改为系统安装的python版本，并删除Pipfile.lock文件

```
$  pipenv install 
```

4、启动项目

注：在windows环境，需要先进入visualenv （命令：<code>pipenv shell</code>，退出命令为<code>exit</code>）

```
$  python3 main.py
```

5、打包为可执行文件

```
$  python3 -m pip install pyinstaller
$  pyinstaller -F main.py
```