# Python基础

<pre>
输出 print
    用print()在括号中加上字符串，就可以向屏幕上输出指定的文字:print('hello, world')
    print()函数也可以接受多个字符串，用逗号“,”隔开，就可以连成一串输出：print('The quick brown fox', 'jumps over', 'the lazy dog')
</pre>

<pre>
输入 input
    Python提供了一个input()，可以让用户输入字符串，并存放到一个变量里：name = input()
</pre>

<pre>
    代码行注释符号: #
        以#开头的语句是注释，注释是给人看的，可以是任意内容，解释器会忽略掉注释。其他每一行都是一个语句，当语句以冒号:结尾时，缩进的语句视为代码块。
        缩进有利有弊。好处是强迫你写出格式化的代码，但没有规定缩进是几个空格还是Tab。按照约定俗成的管理，应该始终坚持使用4个空格的缩进  
    
    Python程序是大小写敏感的
</pre>

<pre>
    数据类型
        整型,浮点,布尔,字符串('...',"...",'''...'''),空值(None)
        列表，字典，元组
        变量，常量
    
    浮点数超出范围后会直接表示为inf(无限大)
</pre>

<pre>
    ord()   :Python提供了ord()函数获取字符的整数表示 
    chr()   :函数把编码转换为对应的字符
</pre>

<pre>
    字符串与字节数组转换
        x = b'ABC'
    
    字符串指定字符编码模式
        str.encode("字符集-名称")
        b'abc'.decode("字符集-名称")
        如果bytes中只有一小部分无效的字节，可以传入errors='ignore'忽略错误的字节：
        b'\xe4\xb8\xad\xff'.decode('utf-8', errors='ignore')
</pre>

<pre>
    len() :如果是str，那么获取的字符长度，如果是字节数组，那么获取的是字节长度
</pre>

<pre>
    由于Python源代码也是一个文本文件，所以，当你的源代码中包含中文的时候，在保存源代码时，就需要务必指定保存为UTF-8编码。当Python解释器读取源代码时，为了让它按UTF-8编码读取，我们通常在文件开头写上这两行：
        #!/usr/bin/env python3
        # -*- coding: utf-8 -*-
    第一行注释是为了告诉Linux/OS X系统，这是一个Python可执行程序，Windows系统会忽略这个注释；
    第二行注释是为了告诉Python解释器，按照UTF-8编码读取源代码，否则，你在源代码中写的中文输出可能会有乱码。
</pre>

<pre>
    字符串的格式化输出
        %运算符就是用来格式化字符串的。在字符串内部，%s表示用字符串替换，%d表示用整数替换，有几个%?占位符，后面就跟几个变量或者值，顺序要对应好。如果只有一个%?，括号可以省略。
        常见的占位符有：

        占位符	替换内容
        %d	整数
        %f	浮点数
        %s	字符串
        %x	十六进制整数
        其中，格式化整数和浮点数还可以指定是否补0和整数与小数的位数
    
        print('%2d-%02d' % (3, 1))
        print('%.2f' % 3.1415926)
    
    还有一种format方法,
        另一种格式化字符串的方法是使用字符串的format()方法，它会用传入的参数依次替换字符串内的占位符{0}、{1}……，不过这种方式写起来比%要麻烦得多：
        >>> 'Hello, {0}, 成绩提升了 {1:.1f}%'.format('小明', 17.125)
        'Hello, 小明, 成绩提升了 17.1%'
</pre>


<pre>
    list
        Python内置的一种数据类型是列表：list。list是一种有序的集合，可以随时添加和删除其中的元素。
     
        classmates = ['Michael', 'Bob', 'Tracy']
        len(classmates) // 获取list的个数
        
        如果要取最后一个元素，除了计算索引位置外，还可以用-1做索引，直接获取最后一个元素：即 classmates[-1]
        
        追加元素
            list是一个可变的有序表，所以，可以往list中追加元素到末尾
            classmates.append('Adam')
        将元素插入指定的位置
            classmates.insert(1, 'Jack')
        删除末尾元素
            classmates.pop()
        删除指定位置元素
            classmates.pop(1)   
        list里面的元素的数据类型也可以不同，比如：
            >>> L = ['Apple', 123, True]
        list元素也可以是另一个list，比如：
            >>> s = ['python', 'java', ['asp', 'php'], 'scheme']
            >>> len(s)
            要拿到'php'可以写p[1]或者s[2][1]，因此s可以看成是一个二维数组，类似的还有三维、四维……数组，不过很少用到             
</pre>

<pre>
    tuple
        元组：tuple。tuple和list非常类似，但是tuple一旦初始化就不能修改，比如同样是列出同学的名字：
            classmates = ('Michael', 'Bob', 'Tracy')
        
        tuple的陷阱：当你定义一个tuple时，在定义的时候，tuple的元素就必须被确定下来

        如果要定义一个空的tuple，可以写成()
         >>> t = ()
         >>> t
         ()
         
        但是，要定义一个只有1个元素的tuple，如果你这么定义：
            >>> t = (1)
            >>> t
            1           
        定义的不是tuple，是1这个数！这是因为括号()既可以表示tuple，又可以表示数学公式中的小括号，这就产生了歧义，因此，Python规定，这种情况下，按小括号进行计算，计算结果自然是1。

        所以，只有1个元素的tuple定义时必须加一个逗号,，来消除歧义：
            >>> t = (1,)
            >>> t
            (1,)
        Python在显示只有1个元素的tuple时，也会加一个逗号,，以免你误解成数学计算意义上的括号
        
        '可变的'Tuple （重点）
            >>> t = ('a', 'b', ['A', 'B'])
            >>> t[2][0] = 'X'
            >>> t[2][1] = 'Y'
            >>> t
            ('a', 'b', ['X', 'Y'])
            
            表面上看，tuple的元素确实变了，但其实变的不是tuple的元素，而是list的元素。tuple一开始指向的list并没有改成别的list，所以，tuple所谓的“不变”是说，tuple的每个元素，指向永远不变。即指向'a'，就不能改成指向'b'，指向一个list，就不能改成指向其他对象，但指向的这个list本身是可变的！
            理解了“指向不变”后，要创建一个内容也不变的tuple怎么做？那就必须保证tuple的每一个元素本身也不能变。
            
</pre>

<pre>
    elif是else if的缩写，完全可以有多个elif，所以if语句的完整形式就是：
    
    if <条件判断1>:
        <执行1>
    elif <条件判断2>:
        <执行2>
    elif <条件判断3>:
        <执行3>
    else:
        <执行4>   
</pre>

<pre>
    pass 空操作
</pre>

<pre>
    loop
        Python的循环有两种，一种是for...in循环，依次把list或tuple中的每个元素迭代出来，看例子：

        names = ['Michael', 'Bob', 'Tracy']
        for name in names:
            print(name)
            
        while n > 0:
            sum = sum + n
            n = n - 2    
            
    range(start, stop[, step])
        如果要计算1-100的整数之和，从1写到100有点困难，幸好Python提供一个range()函数，可以生成一个整数序列，再通过list()函数可以转换为list。比如range(5)生成的序列是从0开始小于5的整数：
            >>> list(range(5))
            [0, 1, 2, 3, 4]       
    
    break
        在循环中，break语句可以提前退出循环  
         
    continue
        在循环过程中，也可以通过continue语句，跳过当前的这次循环，直接开始下一次循环
        
                    
</pre>

<pre>
    dict : {}
        Python内置了字典：dict的支持，dict全称dictionary，在其他语言中也称为map，使用键-值（key-value）存储，具有极快的查找速度。
        
        添加数据: >>> d['Adam'] = 67
        
        如果key不存在，dict就会报错,要避免key不存在的错误，有两种办法，一是通过in判断key是否存在：
            >>> 'Thomas' in d
                False
        二是通过dict提供的get()方法，如果key不存在，可以返回None，或者自己指定的value：
            >>> d.get('Thomas')
            >>> d.get('Thomas', -1)
                -1
            注意：返回None的时候Python的交互环境不显示结果。
        删除key
            要删除一个key，用pop(key)方法，对应的value也会从dict中删除：
            >>> d.pop('Bob')
                    
</pre>

<pre>
    dict 重点
        dict可以用在需要高速查找的很多地方，在Python代码中几乎无处不在，正确使用dict非常重要，需要牢记的第一条就是dict的key必须是不可变对象。

    dict 与 list 比较
    和list比较，dict有以下几个特点：
        查找和插入的速度极快，不会随着key的增加而变慢；
        需要占用大量的内存，内存浪费多。
        而list相反：
        
        查找和插入的时间随着元素的增加而增加；
        占用空间小，浪费内存很少。
        所以，dict是用空间来换取时间的一种方法
</pre>

<pre>
    set
        set和dict类似，也是一组key的集合，但不存储value。由于key不能重复，所以，在set中，没有重复的key。
        
        要创建一个set，需要提供一个list作为输入集合：
            >>> s = set([1, 2, 3])
            >>> s
            {1, 2, 3}
        
        add
           通过add(key)方法可以添加元素到set中，可以重复添加，但不会有效果
           
        remove
            通过remove(key)方法可以删除元素
            
        set和dict的唯一区别仅在于没有存储对应的value，但是，set的原理和dict一样，所以，同样不可以放入可变对象，因为无法判断两个可变对象是否相等，也就无法保证set内部“不会有重复元素”。试试把list放入set，看看是否会报错。            
</pre>

<pre>
    不可变对象
        上面我们讲了，str是不变对象，而list是可变对象。
        当我们调用a.replace('a', 'A')时，实际上调用方法replace是作用在字符串对象'abc'上的，而这个方法虽然名字叫replace，但却没有改变字符串'abc'的内容。相反，replace方法创建了一个新字符串'Abc'并返回，如果我们用变量b指向该新字符串，就容易理解了，变量a仍指向原有的字符串'abc'，但变量b却指向新字符串'Abc'了
</pre>