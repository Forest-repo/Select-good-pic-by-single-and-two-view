备注：
1.需要安装 PIl库 pip install pillow 
2.需要安装 pyinstall库 pip install pyinstaller 

1.将需要打包的内容单独放在一个文件
2.创建一个虚拟环境(打包出来的体积相对小很多)
新建一个虚拟环境python -m venv venv  （第二个venv为起的名字）
修改解释器为虚拟环境(Pycharm里面操作或者vscode操作)
重启命令行终端，使虚拟环境生效（ pip list 可以检测是否生效)
3.安装打包库 pip install pyinstaller
4.执行打包指令 pyinstaller yourprogram.py ; yourprogram.py需要打包的文件，默认只能打包一个文件。
注意:如果使用了第三方工具，有些工具无法打包，特殊的方法才能使用。
5.打包好之后程序会在dist目录，需要检查一下程序是否可以用。
6.在命令行（文件夹位置启动cmd）启动lsl.exe就可以查看错误（不然双击启动，找不到报错的问题，直接就闪现没了。）
pyinstaller -F -w yourprogram.py   #-F 打包为一个exe文件 -w隐藏cmd窗口
默认打包为一个目录下 dist

实战发现：
1.建立一个新的python自带的虚拟环境确实要剩一些内存，比如10.4MB与16.5MB的区别，而且打包的时候要快不少，不过就是新建虚拟环境后 需要重新安装需要的库，这里重点强调在代码里能用啥库就导入，用不到的就不要导入了。
