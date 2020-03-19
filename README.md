1、安装python3

2、安装pipenv

```
$  python3 -m pip install pipenv
```

3、进入到项目目录，安装依赖

```
$  pipenv install 
```

4、启动项目

```
$  python3 main.py
```

5、打包为可执行文件

```
$  python3 -m pip install pyinstaller
$  pyinstaller -F main.py
```