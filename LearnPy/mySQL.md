[TOC]

# 创建数据库与插入数据

## 开发准备

打开MySQL 服务并使用 root 登录：

```
# 打开 MySQL 服务
sudo service mysql start        
#使用 root 用户登录，密码为空
mysql -u root                   
```

##  新建数据库

语句格式为 `CREATE DATABASE <数据库名字>;`，（注意不要漏掉分号 `;`），前面的 CREATE DATABASE 也可以使用小写，具体命令为：

```mysql
CREATE DATABASE mysql_shiyan;
```

## 连接数据库

使用语句 `use <数据库名字>`：

```mysql
use mysql_shiyan;
```

## 删除数据库

```mysql
DROP DATABASE mysql_shiyan;
```



## 数据表

查看当前数据库里有几张表

```mysql
show tables;` 
```

在数据库中新建一张表的语句格式为：

```mysql
CREATE TABLE 表的名字
(
列名a 数据类型(数据长度),
列名b 数据类型(数据长度)，
列名c 数据类型(数据长度)
);
```

我们尝试在 `mysql_shiyan` 中新建一张表 `employee`，包含姓名，ID 和电话信息，所以语句为：

```mysql
CREATE TABLE employee (id int(10),name char(20),phone int(12));
```

然后再创建一张表 /`department`，包含名称和电话信息，想让命令看起来更整洁，你可以这样输入命令：

![img](https://doc.shiyanlou.com/MySQL/sql-02-04.png/wm)

这时候再 `show tables;` 一下，可以看到刚才添加的两张表：

![img](https://doc.shiyanlou.com/MySQL/sql-02-05.png/wm)

## 插入数据

通过 INSERT 语句向表中插入数据，语句格式为：

```mysql
INSERT INTO 表的名字(列名a,列名b,列名c) VALUES(值1,值2,值3);
```

我们尝试向 employee 中加入 Tom、Jack 和 Rose：

```mysql
INSERT INTO employee(id,name,phone) VALUES(01,'Tom',110110110);

INSERT INTO employee VALUES(02,'Jack',119119119);

INSERT INTO employee(id,name) VALUES(03,'Rose');
```

你已经注意到了，有的数据需要用单引号括起来，比如 Tom、Jack、Rose 的名字，这是由于它们的数据类型是 CHAR 型。此外 **VARCHAR,TEXT,DATE,TIME,ENUM** 等类型的数据也需要单引号修饰，而 **INT,FLOAT,DOUBLE** 等则不需要。

第一条语句比第二条语句多了一部分：`(id,name,phone)` 这个括号里列出的，是将要添加的数据 `(01,'Tom',110110110)` 其中每个值在表中对应的列。而第三条语句只添加了 `(id,name)` 两列的数据，**所以在表中Rose的phone为NULL**。

### 一条语句插入多条数据

```mysql
INSERT INTO 表的名字(列名a,列名b,列名c) VALUES(值1,值2,值3),……,(值1,值2,值3);
```

```mysql
INSERT INTO employee(id,name,phone) VALUES
(01,'Tom',110110110),
(02,'Jack',119119119),
(03,'Rose',102013223);
```



# SQL约束

## 约束分类

约束是一种限制，它通过对表的行或列的数据做出限制，来确保表的数据的完整性、唯一性。

在MySQL中，通常有这几种约束：

| 约束类型： | 主键        | 默认值  | 唯一   | 外键        | 非空     |
| ---------- | ----------- | ------- | ------ | ----------- | -------- |
| 关键字：   | PRIMARY KEY | DEFAULT | UNIQUE | FOREIGN KEY | NOT NULL |

## 建立包含约束的表

使用 git 命令将需要的数据文件下载到本地文件夹：

```kotlin
git clone https://github.com/shiyanlou/SQL3  在 MySQL 控制台中输入命令：
```

```mysql
source /home/shiyanlou/Desktop/SQL3/MySQL-03-01.sql;
```

```mysql
CREATE DATABASE mysql_shiyan;

use mysql_shiyan;

CREATE TABLE department
(
  dpt_name   CHAR(20) NOT NULL,#非空约束
  people_num INT(10) DEFAULT '10',#默认值约束
  CONSTRAINT dpt_pk PRIMARY KEY (dpt_name)#主键约束
 );

CREATE TABLE employee
(
  id      INT(10) PRIMARY KEY,#主键约束
  name    CHAR(20),
  age     INT(10),
  salary  INT(10) NOT NULL,#非空约束
  phone   INT(12) NOT NULL,
  in_dpt  CHAR(20) NOT NULL,
  UNIQUE  (phone)#唯一约束
  CONSTRAINT emp_fk FOREIGN KEY (in_dpt) REFERENCES department(dpt_name)#外键约束
 );

CREATE TABLE project
(
  proj_num   INT(10) NOT NULL,
  proj_name  CHAR(20) NOT NULL,
  start_date DATE NOT NULL,
  end_date   DATE DEFAULT '2015-04-01',#默认值约束
  of_dpt     CHAR(20) REFERENCES department(dpt_name),
  CONSTRAINT proj_pk PRIMARY KEY (proj_num,proj_name)#复合主键。主键不仅可以是表中的一列，也可以由表中的两列或多列来共同标识，
    );
```



查看一下这个数据库，输入命令 `show tables;`，可见：

![00](https://doc.shiyanlou.com/MySQL/sql-03-00.png/wm)

### 主键

主键 (PRIMARY KEY)是用于约束表中的一行，作为这一行的唯一标识符，在一张表中通过主键就能准确定位到一行，因此主键十分重要。主键不能有重复且不能为空。

###  默认值约束

DEFAULT 约束只会在使用 INSERT 语句（上一实验介绍过）时体现出来，INSERT语句中，如果被 DEFAULT 约束的位置没有值，那么这个位置将会被 DEFAULT 的值填充，如语句：

```mysql
# 正常插入数据
INSERT INTO department(dpt_name,people_num) VALUES('dpt1',11);

#插入新的数据，people_num 为空，使用默认值
INSERT INTO department(dpt_name) VALUES('dpt2'); 
```

输入命令 `SELECT * FROM department;`，可见表中第二行的people_num 被 DEFAULT 的值 (10) 填充：

![01](https://doc.shiyanlou.com/MySQL/sql-03-01.png/wm)

### 唯一约束

唯一约束 (UNIQUE) 比较简单，它规定一张表中指定的一列的值必须不能有重复值，即这一列每个值都是唯一的。

当 INSERT 语句新插入的数据和已有数据重复的时候，如果有 UNIQUE约束，则 INSERT 失败，比如：

```mysql
INSERT INTO employee VALUES(01,'Tom',25,3000,110110,'dpt1');
INSERT INTO employee VALUES(02,'Jack',30,3500,110110,'dpt2'); 
```

结果如图：

![02](https://doc.shiyanlou.com/MySQL/sql-03-02.png/wm)

### 外键约束

外键 (FOREIGN KEY) 既能确保数据完整性，也能表现表之间的关系。

一个表可以有多个外键，每个外键必须 REFERENCES (参考) 另一个表的主键，被外键约束的列，取值必须在它参考的列中有对应值

在 INSERT 时，如果被外键约束的值没有在参考列中有对应，比如以下命令，参考列 (department 表的 dpt_name) 中没有dpt3，则INSERT 失败：

```mysql
INSERT INTO employee VALUES(02,'Jack',30,3500,114114,'dpt3');
```

可见之后将 dpt3 改为 dpt2（department 表中有 dpt2），则插入成功：

非空约束 (NOT NULL),听名字就能理解，被非空约束的列，在插入值时必须非空。

![13](https://doc.shiyanlou.com/MySQL/sql-03-13.png/wm)

在MySQL中违反非空约束，会报错，比如以下语句：

```mysql
#INSERT 成功 age 为空，因为没有非空约束，表中显示 NULL
INSERT INTO employee(id,name,salary,phone,in_dpt) VALUES(03,'Jim',3400,119119,'dpt2'); 

#报错 salary 被非空约束，插入数据失败
INSERT INTO employee(id,name,age,phone,in_dpt) VALUES(04,'Bob',23,123456,'dpt1'); 
```

结果如图，插入数据失败

![img](https://doc.shiyanlou.com/document-uid600404labid73timestamp1529106622613.png/wm)

# SELECT语句详解

数据库源代码



### 基本的select语句

SELECT 语句的基本格式为：

```mysql
SELECT 要查询的列名 FROM 表名字 WHERE 限制条件;
```

如果要查询表的所有内容，则把 **要查询的列名** 用一个星号 `*` 号表示，代表要查询表中所有的列。 而大多数情况，我们只需要查看某个表的指定的列，比如要查看employee 表的 name 和 age：

```mysql
SELECT name,age FROM employee;
```

### 数学符号条件

SELECT 语句常常会有 WHERE 限制条件，用于达到更加精确的查询。WHERE限制条件可以有数学符号 (`=,<,>,>=,<=`) ，刚才我们查询了 name 和 age，现在稍作修改：

```mysql
SELECT name,age FROM employee WHERE age>25;
```

筛选出 age 大于 25 的结果：

或者查找一个名字为 Mary 的员工的 name,age 和 phone：

```mysql
SELECT name,age,phone FROM employee WHERE name='Mary';
```

### AND 和 OR

WHERE 后面可以有不止一条限制，而根据条件之间的逻辑关系，可以用** OR(或) ** 和 ** AND(且) ** 连接：

```mysql
#筛选出 age 小于 25，或 age 大于 30
SELECT name,age FROM employee WHERE age<25 OR age>30;  
#筛选出 age 大于 25，且 age 小于 30
SELECT name,age FROM employee WHERE age>25 AND age<30; 
```

而刚才的限制条件 **age>25 AND age<30** ，如果需要包含25和30这两个数字的话，可以替换为 **age BETWEEN 25 AND 30** ：

### IN 和 NOT IN

关键词**IN**和**NOT IN**的作用和它们的名字一样明显，用于筛选**“在”**或**“不在”**某个范围内的结果，比如说我们要查询在**dpt3**或**dpt4**的人:

```mysql
SELECT name,age,phone,in_dpt FROM employee WHERE in_dpt IN ('dpt3','dpt4');
```

而**NOT IN**的效果则是，如下面这条命令，查询出了不在**dpt1**也不在**dpt3**的人：

```mysql
SELECT name,age,phone,in_dpt FROM employee WHERE in_dpt NOT IN ('dpt1','dpt3');
```

### 通配符

关键字 **LIKE** 在SQL语句中和通配符一起使用，通配符代表未知字符。SQL中的通配符是 `_` 和 `%` 。其中 `_` 代表一个未指定字符，`%` 代表**不定个**未指定字符。

比如，要只记得电话号码前四位数为1101，而后两位忘记了，则可以用两个 `_` 通配符代替：

```mysql
SELECT name,age,phone FROM employee WHERE phone LIKE '1101__';
```

另一种情况，比如只记名字的首字母，又不知道名字长度，则用 `%`通配符代替不定个字符：

```mysql
SELECT name,age,phone FROM employee WHERE name LIKE 'J%';
```

### 对结果排序

为了使查询结果看起来更顺眼，我们可能需要对结果按某一列来排序，这就要用到 **ORDER BY** 排序关键词。默认情况下，**ORDER BY**的结果是**升序**排列，而使用关键词**ASC**和**DESC**可指定**升序**或**降序**排序。 比如，我们**按salary降序排列**，SQL语句为：

```mysql
SELECT name,age,salary,phone FROM employee ORDER BY salary DESC;
```

### SQL内置函数和计算

SQL 允许对表中的数据进行计算。对此，SQL 有 5 个内置函数，这些函数都对 SELECT 的结果做操作：

| 函数名： | COUNT | SUM  | AVG      | MAX    | MIN    |
| -------- | ----- | ---- | -------- | ------ | ------ |
| 作用：   | 计数  | 求和 | 求平均值 | 最大值 | 最小值 |

> 其中 COUNT 函数可用于任何数据类型(因为它只是计数)，而 SUM 、AVG 函数都只能对数字类数据类型做计算，MAX 和 MIN 可用于数值、字符串或是日期时间数据类型。

具体举例，比如计算出salary的最大、最小值，用这样的一条语句：

```mysql
SELECT MAX(salary) AS max_salary,MIN(salary) FROM employee;
```

有一个细节你或许注意到了，**使用AS关键词可以给值重命名**，比如最大值被命名为了max_salary：

### 子查询

时必须处理多个表才能获得所需的信息。例如：想要知道名为 "Tom" 的员工所在部门做了几个工程。员工信息储存在 employee 表中，但工程信息储存在project 表中。

对于这样的情况，我们可以用子查询：

```mysql
SELECT of_dpt,COUNT(proj_name) AS count_project FROM project GROUP BY of_dpt
HAVING of_dpt IN
(SELECT in_dpt FROM employee WHERE name='Tom');
```

### 连接查询

在处理多个表时，子查询只有在结果来自一个表时才有用。但如果需要显示两个表或多个表中的数据，这时就必须使用连接 **(join)** 操作。 连接的基本思想是把两个或多个表当作一个新的表来操作，如下：

```mysql
SELECT id,name,people_num
FROM employee,department
WHERE employee.in_dpt = department.dpt_name
ORDER BY id;
```

这条语句查询出的是，各员工所在部门的人数，其中员工的 id 和 name 来自 employee 表，people_num 来自 department 表：

![img](https://doc.shiyanlou.com/MySQL/sql-04-14.png/wm)
另一个连接语句格式是使用 JOIN ON 语法，刚才的语句等同于：

```mysql
SELECT id,name,people_num
FROM employee JOIN department
ON employee.in_dpt = department.dpt_name
ORDER BY id;
```

