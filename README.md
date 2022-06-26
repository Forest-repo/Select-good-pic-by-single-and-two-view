# 1.Select-good-pic-by-single-view
## 功能描述
用python自带tkinter完成的gui功能：在单视角数据集挑选有可学习特征的图片，复制到输出目录。（注意这里是1个视角，对应输出到1个目录）
有详细的代码和文件，并且有打包为exe功能，可以直接在别人电脑运行，有打包的说明。

### Select-good-pic-by-single-view的流程说明：
1.点击按钮1，打开要挑选的单视角下的某个类别的目录
比如：D:/lsl-e/赵锟-2021-研究生/论文和数据集/Multi_view_Datasets/cvbrct_dataset/cvbrct/aerial/apartment

2.点击按钮2，找到要输出的目标类别目录，需要提前手动建立好这个类别目录，跟原来的目录结构保持一致。
比如：D:/lsl-e/赵锟-2021-研究生/论文和数据集/Multi_view_Datasets/cvbrct_dataset/good_single_view/aerial/apartment

3.点击上一张或下一张 查看并选择图片。

4.如果觉得有特征就点击 本张有可学习特征的按钮，会自动复制输出到目标目录。

5.记住当前的类别和index，以防下次时忘记挑选到哪了，下次直接输入index，点击 跳转按钮，
可以直接选择到index对应的图片。

6.注意在选完一个类别后，需要关闭后再重新启动，进行下一个类别的挑选
### 演示图片：
![Markdown](show_pngs/show1.png)



# 2.Select-goodmatch-pic-by-good-twoviews
## 功能描述
用python自带tkinter完成的gui功能：在挑选出的双视角数据集挑选同时存在且完美匹配的图片，复制到输出目录。（注意这里应该是2个视角，对应输出到2个目录）
有详细的代码和文件，并且有打包为exe功能，可以直接在别人电脑运行，有打包的说明。

### Select-goodmatch-pic-by-good-twoviews的流程说明：
1.跟单视角差不多，按顺序点击即可

2.输出目标类别目录，例子为：Multi_view_Datasets/cvbrct_dataset/good_double_views 即可，会自动找到视角和类别。

3.注意在选完一个类别后，需要关闭后再重新启动，进行下一个类别的挑选

# 安装备注：
1.需要安装 PIl库 pip install pillow 

2.需要安装 pyinstall库 pip install pyinstaller 

3.打包命令 pyinstaller -F -w yourprogram.py   #注意大小写  -F 打包为一个exe文件 -w 隐藏cmd窗口   默认打包为一个目录下 dist

打包建议：
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

结果就是新建一个python以前的虚拟环境python -m venv venv ，需要安装pillow和pyinstaller，打包的内存瞬间下降了很多，之前是300多MB，现在是10.6MB。

# 参考网址(实际用上的网址)
1.[http://c.biancheng.net/tkinter/what-is-gui.html](http://c.biancheng.net/tkinter/what-is-gui.html)

2.[https://sunhwee.com/posts/80fa3a85.html](https://sunhwee.com/posts/80fa3a85.html)

