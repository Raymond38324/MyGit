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
# 表的修改和删除

数据库源代码

```
git clone https://github.com/shiyanlou/SQL5
```

## 对一张表的修改

### 重命名一张表

重命名一张表的语句有多种形式，以下 3 种格式效果是一样的：

```mysql
RENAME TABLE 原名 TO 新名字;

ALTER TABLE 原名 RENAME 新名;

ALTER TABLE 原名 RENAME TO 新名;
```

### 删除一张表

删除一张表的语句，格式是这样的：

```mysql
DROP TABLE 表名字;
```

## 对表结构的修改

### 增加一列

在表中增加一列的语句格式为：

```mysql
ALTER TABLE 表名字 ADD COLUMN 列名字 数据类型 约束;

或： ALTER TABLE 表名字 ADD 列名字 数据类型 约束;
```

现在 employee 表中有 `id、name、age、salary、phone、in_dpt` 这6个列，我们尝试加入 `height` (身高)一个列并指定DEFAULT 约束：

```mysql
ALTER TABLE employee ADD COLUMN height INT(3) DEFAULT 170;
```

新增加的列，被默认放置在这张表的最右边。如果要把增加的列插入在指定位置，则需要在语句的最后使用AFTER关键词(**“AFTER 列1” 表示新增的列被放置在 “列1” 的后面**)。

比如我们新增一列 `weight` (体重)放置在 `age` (年龄)的后面：

```MYSQL
ALTER TABLE employee ADD COLUMN weight INT(3) DEFAULT 120 AFTER age;
```

上面的效果是把新增的列加在某位置的后面，如果想放在第一列的位置，则使用 `FIRST` 关键词，如语句：

```MYSQL
ALTER TABLE employee ADD test INT(10) DEFAULT 11 FIRST;
```

### 删除一列

删除表中的一列和刚才使用的新增一列的语句格式十分相似，只是把关键词 `ADD` 改为 `DROP` ，语句后面不需要有数据类型、约束或位置信息。具体语句格式：

```MYSQL
ALTER TABLE 表名字 DROP COLUMN 列名字;
或： ALTER TABLE 表名字 DROP 列名字;
```

我们把刚才新增的 `test` 删除：

```MYSQL
ALTER TABLE employee DROP COLUMN test；
```

### 重命名一列

这条语句其实不只可用于重命名一列，准确地说，它是对一个列做修改(CHANGE) ：

```mysql
ALTER TABLE 表名字 CHANGE 原列名 新列名 数据类型 约束;
```

> **注意：这条重命名语句后面的 “数据类型” 不能省略，否则重命名失败。**

当**原列名**和**新列名**相同的时候，指定新的**数据类型**或**约束**，就可以用于修改数据类型或约束。需要注意的是，修改数据类型可能会导致数据丢失，所以要慎重使用。

我们用这条语句将 “height” 一列重命名为汉语拼音 “shengao” 

```mysql
ALTER TABLE employee CHANGE height shengao INT(3);
```

### 改变数据类型

要修改一列的数据类型，除了使用刚才的**CHANGE**语句外，还可以用这样的**MODIFY**语句：

```MYSQL
ALTER TABLE 表名字 MODIFY 列名字 新数据类型;
```

再次提醒，修改数据类型必须小心，因为这可能会导致数据丢失。在尝试修改数据类型之前，请慎重考虑。

## 对表的内容修改

### 修改表中某个值

大多数时候我们需要做修改的不会是整个数据库或整张表，而是表中的某一个或几个数据，这就需要我们用下面这条命令达到精确的修改：

```mysql
UPDATE 表名字 SET 列1=值1,列2=值2 WHERE 条件;
```

比如，我们要把 Tom 的 age 改为 21，salary 改为 3000：

```mysql
 UPDATE employee SET age=21,salary=3000 WHERE name = 'Tom';
```

###  删除一行记录

删除表中的一行数据，也必须加上WHERE条件，否则整列的数据都会被删除。删除语句：

```MYSQL
DELETE FROM 表名字 WHERE 条件;
```

我们尝试把Tom的数据删除：

````MYSQL
DELETE FROM employee WHERE name = 'Tom';
````

# 其他基本操作

## 索引

索引是一种与表有关的结构，它的作用相当于书的目录，可以根据目录中的页码快速找到所需的内容。

当表中有大量记录时，若要对表进行查询，没有索引的情况是全表搜索：将所有记录一一取出，和查询条件进行一一对比，然后返回满足条件的记录。这样做会消耗大量数据库系统时间，并造成大量磁盘 I/O 操作。

而如果在表中已建立索引，在索引中找到符合查询条件的索引值，通过索引值就可以快速找到表中的数据，可以**大大加快查询速度**。

对一张表中的某个列建立索引，有以下两种语句格式：

```mysql
ALTER TABLE 表名字 ADD INDEX 索引名 (列名);

CREATE INDEX 索引名 ON 表名字 (列名);
```

我们用这两种语句分别建立索引：

```mysql
ALTER TABLE employee ADD INDEX idx_id (id);  #在employee表的id列上建立名为idx_id的索引

CREATE INDEX idx_name ON employee (name);   #在employee表的name列上建立名为idx_name的索引
```

索引的效果是加快查询速度，当表中数据不够多的时候是感受不出它的效果的。这里我们使用命令 **SHOW INDEX FROM 表名字;** 查看刚才新建的索引：

![01](https://doc.shiyanlou.com/MySQL/sql-06-01.png/wm)

在使用SELECT语句查询的时候，语句中WHERE里面的条件，会**自动判断有没有可用的索引**。

## 视图

视图是从一个或多个表中导出来的表，是一种**虚拟存在的表**。它就像一个窗口，通过这个窗口可以看到系统专门提供的数据，这样，用户可以不用看到整个数据库中的数据，而只关心对自己有用的数据。

注意理解视图是虚拟的表：

- 数据库中只存放了视图的定义，而没有存放视图中的数据，这些数据存放在原来的表中；
- 使用视图查询数据时，数据库系统会从原来的表中取出对应的数据；
- 视图中的数据依赖于原来表中的数据，一旦表中数据发生改变，显示在视图中的数据也会发生改变；
- 在使用视图的时候，可以把它当作一张表。

创建视图的语句格式为：

```MYSQL
CREATE VIEW 视图名(列a,列b,列c) AS SELECT 列1,列2,列3 FROM 表名字;
```

可见创建视图的语句，后半句是一个SELECT查询语句，所以**视图也可以建立在多张表上**，只需在SELECT语句中使用**子查询**或**连接查询**，这些在之前的实验已经进行过。

现在我们创建一个简单的视图，名为 **v_emp**，包含**v_name**，**v_age**，**v_phone**三个列：

```MYSQL
CREATE VIEW v_emp(v_name,v_age,v_phone) AS SELECT name,age,phone FROM employee;
```

![02](https://doc.shiyanlou.com/MySQL/sql-06-02.png/wm)

创建一个包含连接查询的视图

```mysql
 CREATE VIEW v_join(v_name, v_salary ,v_projname) AS SELECT name,salary, proj_name FROM  employee JOIN project ON employee.in_dpt = project.of_dpt;
```

创建一个包含子查询的视图

```mysql
CREATE VIEW v_son(v_dpt,v_number) AS SELECT of_dpt,COUNT(proj_name) FROM project GROUP BY of_dpt HAVING of_dpt IN (SELECT in_dpt FROM employee WHERE name= 'Tom');
```

## 导入和导出

不适用与ＳＱＬ

### 导入

导入操作，可以把一个文件里的数据保存进一张表。导入语句格式为：

```mysql
LOAD DATA INFILE '文件路径和文件名' INTO TABLE 表名字;
```

### 导出

导出与导入是相反的过程，是把数据库某个表中的数据保存到一个文件之中。导出语句基本格式为：

```nysql
SELECT 列1，列2 INTO OUTFILE '文件路径和文件名' FROM 表名字;
```

**注意：语句中 “文件路径” 之下不能已经有同名文件。**

现在我们把整个employee表的数据导出到 /var/lib/mysql-files/ 目录下，导出文件命名为 **out.txt** 具体语句为：

```mysql
SELECT * INTO OUTFILE '/var/lib/mysql-files/out.txt' FROM employee;
```

## 备份和恢复

### 备份

数据库中的数据或许十分重要，出于安全性考虑，在数据库的使用中，应该注意使用备份功能。

> 备份与导出的区别：导出的文件只是保存数据库中的数据；而备份，则是把数据库的结构，包括数据、约束、索引、视图等全部另存为一个文件。

**mysqldump** 是 MySQL 用于备份数据库的实用程序。它主要产生一个 SQL 脚本文件，其中包含从头重新创建数据库所必需的命令CREATE TABLE INSERT 等。

使用 mysqldump 备份的语句：

```mysql
mysqldump -u root 数据库名>备份文件名;   #备份整个数据库

mysqldump -u root 数据库名 表名字>备份文件名;  #备份整个表
```

我们尝试备份整个数据库 `mysql_shiyan`，将备份文件命名为 `bak.sql`，先 `Ctrl+Z` 退出 MySQL 控制台，再打开 Xfce 终端，在终端中输入命令：

```musql
cd /home/shiyanlou/
mysqldump -u root mysql_shiyan > bak.sql;
```

使用命令 “ls” 可见已经生成备份文件 `bak.sql`：

![07](https://doc.shiyanlou.com/MySQL/sql-06-07.png/wm)

> 你可以用gedit查看备份文件的内容，可以看见里面不仅保存了数据，还有所备份的数据库的其他信息。

### 恢复

用备份文件恢复数据库

```mysql
source /tmp/SQL6/MySQL-06.sql
```

这就是一条恢复语句，它把 MySQL-06.sql 文件中保存的`mysql_shiyan` 数据库恢复。

还有另一种方式恢复数据库，但是在这之前我们先使用命令新建一个**空的数据库 test**：

```mysql
mysql -u root          #因为在上一步已经退出了MySQL，现在需要重新登录

CREATE DATABASE test;  #新建一个名为test的数据库
```

再次 **Ctrl+Z** 退出MySQL，然后输入语句进行恢复，把刚才备份的 **bak.sql** 恢复到 **test** 数据库：

```sql
mysql -u root test < bak.sql
```

我们输入命令查看 test 数据库的表，便可验证是否恢复成功：

```mysql
mysql -u root          #因为在上一步已经退出了MySQL，现在需要重新登录

use test               #连接数据库test

SHOW TABLES;           #查看test数据库的表
```

