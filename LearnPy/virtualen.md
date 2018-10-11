[TOC]
# 安装 virtualenv
首先安装 pip3，打开 xfce 终端输入下面的命令：


```python
$ sudo apt-get update
$ sudo apt-get install python3-pip
```

用如下命令安装 virtualenv：

```python
$ sudo pip3 install virtualenv
```


# 用法
我们会创建一个叫做 virtual 的目录，在里面我们会有两个不同的虚拟环境。

```python
$ cd /home/shiyanlou
$ mkdir virtual
```
下面的命令创建一个叫做 virt1 的环境。

```python
$ cd virtual
$ virtualenv virt1
```
现在我们激活这个 virt1 环境。

```python
$ source virt1/bin/activate
(virt1)shiyanlou：~/$
```

提示符的第一部分是当前虚拟环境的名字，当你有多个环境的时候它会帮助你识别你在哪个环境里面。

现在我们将安装 redis 这个 Python 模块。

```python
(virt1)$ sudo pip3 install redis
```
使用 deactivate 命令关闭虚拟环境。

```python
(virt1)$ deactivate
```
现在我们将创建另一个虚拟环境 virt2，我们会在里面同样安装 redis 模块，但版本是 2.8 的旧版本。

```python
$ virtualenv virt2
$ source virt2/bin/activate
(virt2)$ sudo pip3 install redis==2.8
```



这样可以为你的所有开发需求拥有许多不同的环境