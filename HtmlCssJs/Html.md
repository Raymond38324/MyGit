[TOC]

# 初识Html

## HTML文件结构
![img](https://doc.shiyanlou.com/userid20407labid118time1423123992674/wm)
一般的html文件结构就是下面这样
```html
<html>
    <head>
            <title>.....</title>
    </head>

    <body>
            <p>.....</p>
    </body>
</html>
```
## HTML文档
HTML 文档也被称为网页 HTML 文档包含 HTML 标签和纯文本 Web 浏览器的作用是读取 HTML 文档，并以网页的形式显示出它们。浏览器不会显示 HTML标签（相当于是隐藏的格式描述），而是使用标签来解释页面的内容：
```html
<html>
    <body>

        <h1>First Heading</h1>

         <p>first paragraph</p>

    </body>
</html>
```
< html> 与 < /html> 之间的文本描述网页 < body> 与 < /body> 之间的文本是可见的页面内容 < h1> 与 < /h1> 之间的文本被显示为标题 < p> 与 < /p> 之间的文本被显示为段落
## HTML标签
- 什么是标签

标签就是上面这些< head>、< body>、< table> 等被尖括号“<”和“>”包起来的对象，绝大部分的标签都是成对出现的，如< table>< /table>、< form>< /form>。标签对中的第一个标签是开始标签，第二个标签是结束标签，开始和结束标签也被称为开放标签和闭合标签;当然还有少部分不是成对出现的，如< br>、< hr>等。标签就是用来标记HTML元素的。位于起始标签和结束标签之间的文本就是HTML元素的内容。
## 常用的标签
- HTML标题 Heading 是通过 < h1> - < h6> 等标签进行定义的。 示例：
```Html
<h1>This is first heading</h1>
<h2>This is second heading</h2>
<h3>This is third heading</h3>
```

- HTML段落 paragraph 是通过 < p> 标签进行定义的。 示例：
```Html
<p>This is a paragraph.</p>
<p>This is another paragraph.</p>
```

- HTML链接 链接 是通过 < a> 标签进行定义的。 示例：
```Html
<a href="http://shiyanlou.com">This is a link</a>
```
- HTML图像 image是通过 < img> 标签进行定义的。 示例：
```Html
<img src="shiyanlou.jpg" width="100" height="142" />
```
# HTML文本
## HTML元素
### 什么是HTML元素
HTML 元素指的是从开始标签（start tag）到结束标签（end tag）的所有代码。 HTML网页实际上就是由许许多多各种各样的HTML元素构成的文本文件，并且任何网页浏览器都可以直接运行HTML文件。所以可以这样说，HTML元素就是构成HTML文件的基本对象，HTML元素可以说是一个统称而已。HTML元素就是通过使用HTML标签进行定义的。

<开始标签> 元 素 内 容 <结束标签>
```html
<p>shiyanlou</p>
```
### 元素语法
HTML元素语法特点：

- HTML 元素以开始标签起始
  -HTML 元素以结束标签终止
- 元素的内容是开始标签与结束标签之间的内容
- 某些 HTML 元素具有空内容（empty content）
- 空元素在开始标签中进行关闭（以开始标签的结束而结束）
- 大多数 HTML 元素可拥有属性(下面会讲)

### HTML元素嵌套示例
```html
<html>
    <body>
        <p>let's go to shiyanlou</p>
    </body>
</html>
```
### HTML空元素
某些 HTML 元素具有空内容（empty content），这种元素被叫做空元素。比如说换行符<br/>
< p>标签和< br/>标签有的异同

- 相同之处是<br>和<p>都是有换行的属性及作用
- 区别 <br/>是只需一个单独使用，而<p>和< /p>是一对使用
- <br/>标签是小换行提行（相当于我们平时文本中输入一个回车），<p>标签是大换行（分段，相当与两个回车）,各行作用。

### Htmls属性
关于属性有以下语法规则：

- 是在 HTML 元素的开始标签中定义。
  总是以名称和值对应的形式出现，比如：name="value"。
- 属性值应该始终被包括在引号内。双引号是最常用的，不过使用单引号也没有问题。
  举例：
```html
<a href="http://www.shiyanlou.com">shiyanlou</a>
```
href="http://www.shiyanlou.com"，这一部分就叫做< a>标签的属性，是对< a>标签的补充说明，既指向的网页
通过在标签中加属性来实现标题居中对齐的目的。
```html
<html>
    <head>
        <title>xuexi test</title>
    </head>
    <body>
        <h1 align = "center">This is a h1 text.</h1>
        <p align = "center">Hello world</p>
    </body>
</html>
```
给网页增添背景颜色
```html
<body bgcolor="#000000">
<body bgcolor="rgb(0,0,0)">
<body bgcolor="black">
```
## Html文本格式化
```html
<html>
    <head>
        <title>xuexi test</title>
    </head>
    <body>
        <b>bold type</b><br/>
        <big>bigd type</big><br/>
        <em>em type</em><br/>
        <small>small type</small><br/>
        <i>italic type</i><br/>
        <strong>strong type</strong><br/>
        #预格式文本（所谓预格式文本就是指代码页和网页展示是一样的格式，不用额外添加换行符标签就能换行）
        <pre>
        <b>bold type</b><br/>
        <big>bigd type</big><br/>
        <em>em type</em><br/>
        <small>small type</small><br/>
        <i>italic type</i><br/>
        <strong>strong type</strong><br/>
        </pre>
    </body>
</html>
```
## HTML样式
style 提供了一种改变所有 HTML 元素的样式的通用方法。这里可以将，背景颜色，字体样式，字体尺寸，字体颜色，对齐方式一并定义好。下面我们就再来动手写一个HTML文件
```html
<html>
    <body style = "background-color:powderblue">
    <h1 style = "text-align:center;font-family:verdava;color:gray"></h1>
    <p style = "font-family:time;color:green">time and green word</p>
    <p style = "font-size:40px">the size of these wprds is 40 pixels</p>
    </body>
</html>
```
![img](https://doc.shiyanlou.com/userid20407labid118time1423216239851/wm)

# HTML超文本

## HTML链接

#### 给文字及图片添加超链接

直接给文字添加链接到网页和另外的HTML文件。

HTML内容如下

```html
<html>
<body>

    <p>let's have an example< /p>

    <p>   
        < a href="http://www.shiyanlou.com">shiyanlou< /a>
    </p>

</body>
</html>
```

让这个HTML文件链接到另一个HTML文件。（在相同的文件夹，再添加一个HTML文件)

![img](https://doc.shiyanlou.com/userid20407labid119time1423298769922/wm)

**给图片添加超链接**

![img](https://doc.shiyanlou.com/userid20407labid120time1423450150809/wm)

#### 超链接的打开方式

超级链接标签提供了target属性进行设置，取值分别为*self（自我覆盖，默认）、*blank（创建新窗口打开新页面）

在前面的基础上我们在< a>标签加入target属性：target="_blank"

![img](https://doc.shiyanlou.com/userid20407labid119time1423447370274/wm)

通过与第一张图的对比我们可以看出，*blank属性加上以后，链接到的网页是在新窗口中打开的，而默认的*self属性则是在本页面以覆盖的形式打开

####  超链接添加提示文字

当光标停留在超链接上时，提示语言就会显现，会让页面显现的很简介。设计到的属性就是title，下面我们再来动手实验一把 下面就是实验内容和效果

在前面的基础上，< a>标签加上title属性：title="this word will link to the web of shiyanlou"

![img](https://doc.shiyanlou.com/userid20407labid120time1423452041430/wm)

#### 超链接实现书签

也许你在网页看过小说，当你在页首点击章节的题目，就会自动的跳转到相应的章节，这是怎样实现的呢？。要实现书签，你就要了解，什么是锚（anchor）。锚（anchor）是引自于船只上的锚，锚被抛下后，船只就不容易飘走、迷路。实际上锚就是用于在单个页面内不同位置的跳转，有的地方叫做书签。涉及到的标签当然还是< a>标签,超级链接标签的name属性用于定义锚的名称，一个页面可以定义多个锚，通过超级链接的href属性可以根据name跳转到对应的锚。 如下实现跳转：
```html
<a href="#跳转目的地名称">跳转起始字符</a>
...
<a name="跳转目的地名称">跳转目的地字符</a>
```
具体实现如下

```html
<html>
    <head>
    <title>HTML</title>  
    </head>  
<body style="font-size:20px">

    <p style="text-align:center">HTML LEARNING</p>

    <p>
    <a href="#c1">  HTML chushi</a>
    </p>
    <p>
    <a href="#c2">HTML wenben </a>
    </p>
    <p>
    <a href="#c3">HTML chaowenben 1 </a>
    </p>
    <p>
    <a href="#c4"> HTML chaowenben 2 </a>
    </p>
    <p>
    <a href="#c5">HTML shiyan </a>
    </p>


    <h1><a name="c1"></a>chapter 1 chushi HTML</h1>
    <p>lalalaalalal</p>
    <p>lalalaalalal</p>
    <p>lalalaalalal</p>

    <h1><a name="c2"></a>chapter 2 wenben HTML</h1>
    <p>lalalaalalal</p>
    <p>lalalaalalal</p>
    <p>lalalaalalal</p>

    <h1><a name="c3"></a>chapter 3 chaowenben 1 HTML</h1>
    <p>lalalaalalal</p>
    <p>lalalaalalal</p>
    <p>lalalaalalal</p>

    <h1><a name="c4"></a>chapter 4 chaowenben 2 HTML</h1>
    <p>lalalaalalal</p>
    <p>lalalaalalal</p>
    <p>lalalaalalal</p>

    <h1><a name="c5"></a>chapter 5 shiyan HTML</h1>
    <p>lalalaalalal</p>
    <p>lalalaalalal</p>
    <p>lalalaalalal</p>

    </body>
</html>
```

## HTML表格

HTML 網頁設計不可或缺的元素就是表格（Table），通常表格用來做版面的排版，而表格的用法包含了幾個重要的标签，分別是 table、tr 與 td 這幾個重點，組合起來才是個完整的表格，表格由 < table> 标签来定义。每个表格均有若干行（由 < tr> 标签定义），每行被分割为若干单元格（由 < td> 标签定义）。字母 td 指表格数据（table data），即数据单元格的内容。< th>标签用来定义表头。数据单元格可以包含文本、图片、列表、段落、表单、水平线、表格等等。

```html
<html>
<title >TABLE</title>
<body style="font-size:20px">

    <p style="text-align:center">table practice</p>  

     <table  align="center" border="1">  
            <tr>
            <td>first row and first column</td>
            <td>first row and second column</td>
            <td>first row and third column</td>
            </tr>

             <tr>
             <td>second row and first column</td>
             <td>second row and second column</td>
             <td>second row and third column</td>
             </tr>

     </table>   

</body>
</html>
```

border="1"定义的是最外面边框粗细，为1，你也可以设置为0，就是不显示边框（默认就是没有边框） colspan：控制此单位所占列数, rowspan：控制此单位所占行数

```html
<html>
<title >TABLE</title>
<body style="font-size:30px">
    <p style="text-align:center">table practice</p>
     <table  align="center" border="15" >

        <tr>
         <td align="center" colspan="2">first row and first column</td>
         </tr>

         <tr>
         <td rowspan="2">second row and first column </td>
            <td>second row and second column </td>
            <td >second row and third column</td>
         </tr>
         <tr>
         <td>third row and first column </td>
            <td>third row and second column </td>
         </tr>
        </table>   
</body>
</html>
```

![img](https://doc.shiyanlou.com/userid20407labid119time1423466365267/wm)

表格可定义的其他细节

- 标签：< th>表头< /th>：设置表头
- 标签：< caption>标题< /caption>：设置表的标题
- 属性：cellpadding="..."设置单元格边距
- 属性：bgcolor="..."设置表格背景颜色
- 属性：background="..." 以某张图片作为表格背景

## HTML图像

### 设置一张图片为网页背景图片

在body 属性中加入background属性添加背景图片
![img](https://doc.shiyanlou.com/userid20407labid119time1423473894835/wm)

### 插入一张图片 
```html
   <img src="路径加文件名">
```
### 添加属性调整图片的对齐方式

   在< img>标签中加入align属性，调整对齐。 相对字体的上下可以加的参数有 bottom、middle、top，默认就是我们刚看见的bottom 相对字体左右可加的参数有right，left默认为right

   ```html
   <html>
   <head>
       <title>image test</title>
       </head>
       <body background="./qwe.gif">
   
       <p>let's have an example<img src="./julizi.png"></p>
       <p> align top<img src="./julizi.png" align="top" ></p>
       <p>align middle<img src="./julizi.png" align="middle"></p>
       <p>align left<img src="./julizi.png" align="left" ></p>
   
       </body>
   </html>
   ```

   ![图片描述信息](https://doc.shiyanlou.com/userid20407labid119time1423476154907/wm)

### 调整插入图片尺寸 

大多数的尺寸都没有那么合适，直接插入以后会破换整体页面的效果。所以在插入图片时，很有必要控制其尺寸，这是很容易办到的，就还需要在< img>标签中加入width height 两个属性。 那我们顺势就控制下上面的那几副图吧

```python
width="80" height="80"
```

![img](https://doc.shiyanlou.com/userid20407labid119time1423477212662/wm)

### 创建图像映射

有时我们需要实现，点击图片的不同地方跳转到不同的地方。意思就是，一张图片我们可以创建带有可供点击区域的图像地图，其中每个区域就是一个超链接。涉及到的标签就是< map>标签，用来指定图片,< area>用来指定超链接区域

```html
<img src="xx.jpg" usemap="#mp"/>  
<map name="mp" id="mp">  
    <area>
    ...
    ...
    ...
    </area>  
</map> 
```

这里以一张图片作为地图， 在< area>标签中我们会涉及到shape ，coords， href属性，分别用来指定超链接区域形状，超链接区域坐标，还有超链接跳转地。

这是具体实现内容

```html
<html>
<head>
    <title>image test</title>
    </head>
    <body background="./qwe.gif">

    <p>tap the li zi </p>
    <img src="./julizi.png" usemap="#lizi"/>

    <map name="lizi">
     <area shape="rect" coords="50,10,100,60" href="img.html" target="_blank">
    </map>  

    </body>
</html>
```

然后，当我们点击小松鼠举起的栗子，你就会看见更多栗子 

![img](https://doc.shiyanlou.com/userid20407labid120time1423539023047/wm)
shape属性的取值可以是：rect(矩形)、circle(圆形)、poly(多边形)和default(整个图像区域)。这里采用的是矩形。

coords属性对于矩形而言，coords有4个值，分别用逗号隔开，表示矩形区域左上角x坐标、左上角y坐标、右下角x坐标和右下角y坐标，这里获取坐标的方式，就用截图工具帮忙就好。
