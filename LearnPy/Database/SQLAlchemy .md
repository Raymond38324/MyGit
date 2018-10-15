[TOC]

# SQLAlchemy基础

安装 SQLAlchemy:

```linux
$ sudo apt-get update
$ sudo pip3 install sqlalchemy 
```

## 连接与创建

 在启动 MySQL 之前，我们需要进行一些配置，将 MySQL 默认的 latin1 编码改成 utf8 。

```
$ sudo vim /etc/mysql/my.cnf
```

通过上面的命令打开 MySQL 的配置文件， 添加下面几个配置：

```
[client]
default-character-set = utf8

[mysqld]
character-set-server = utf8

[mysql]
default-character-set = utf8
```

保存退出。现在我们可以启动 MySQL 服务了：

```
$ sudo service mysql start
```

在命令行下输入下面命令启动 MySQL：

```
$ mysql -uroot -p
```
创建一个名为 `blog` 的数据库为下面的使用作准备，后面的所有操作都是在 blog 中进行的。
```mysql
> create database blog;
```

另外，我们需要安装一个 Python 与 MySQL 之间的驱动程序：

```
$ sudo pip3 install pymysql
```

### 连接数据库

新建 `db.py` 文件，并向其中写入如下内容：

```python
# coding: utf-8

from sqlalchemy import create_engine

engine = create_engine('mysql+pymysql://root@localhost:3306/blog')

print(engine)
```

在上面的程序中，我们连接了默认运行在 `3306` 端口的 MySQL 中的 `blog` 数据库。

运行下这个程序，看到下面的信息说明我们已经连接成功了： ![3.1-1](https://doc.shiyanlou.com/document-uid600404labid2382timestamp1530545109116.png/wm)

### 描述表结构

SQLAlchmey 提供了一套 Declarative 系统来完成这个任务。我们以创建一个 `users` 表为例，看看它是怎么用 SQLAlchemy 的语言来描述的：

```python
# coding: utf-8

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer


engine = create_engine('mysql+pymysql://root@localhost:3306/blog?charset=utf8')
Base = declarative_base()


class User(Base):

    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String(64), nullable=False, index=True)
    password = Column(String(64), nullable=False)
    email = Column(String(64), nullable=False, index=True)


    def __repr__(self):
        return '%s(%r)' % (self.__class__.__name__, self.username)

Base.metadata.create_all(engine)    
```

我们看到，在 `User` 类中，用 `__tablename__` 指定在 MySQL 中表的名字。我们创建了三个基本字段，类中的每一个 `Column` 代表数据库中的一列，在 `Colunm` 中，指定该列的一些配置。第一个字段代表类的数据类型，上面我们使用 `String`, `Integer` 俩个最常用的类型，其他常用的包括：

```
Text
Boolean
SmallInteger
DateTime
```

`nullable=False` 代表这一列不可以为空，`index=True` 表示在该列创建索引。

另外定义 `__repr__` 是为了方便调试，你可以不定义，也可以定义的更详细一些。

```
$ python3 db.py
```

运行程序，程序不会有输出信息，但是 sqlalchemy 已经在 MySQL 数据库里面为我们创建了 `users` 表。

可以进入 MySQL，运行图片中的命令看看表是如何创建的：

![3.2-1](https://doc.shiyanlou.com/document-uid600404labid2382timestamp1529656847320.png/wm)

## 关系定义

