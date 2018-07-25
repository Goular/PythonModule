<pre>
    切片
        >>> L[0:3]
        ['Michael', 'Sarah', 'Tracy']
        L[0:3]表示，从索引0开始取，直到索引3为止，但不包括索引3。即索引0，1，2，正好是3个元素。
        如果第一个索引是0，还可以省略
        类似的，既然Python支持L[-1]取倒数第一个元素，那么它同样支持倒数切片，
        >>> L[-2:]
        ['Bob', 'Jack']
        >>> L[-2:-1]
        ['Bob']
        
        甚至什么都不写，只写[:]就可以原样复制一个list
        >>> L[:]
        [0, 1, 2, 3, ..., 99]
        
        tuple也是一种list，唯一区别是tuple不可变。因此，tuple也可以用切片操作，只是操作的结果仍是tuple：
        >>> (0, 1, 2, 3, 4, 5)[:3]
        (0, 1, 2)
        
        字符串'xxx'也可以看成是一种list，每个元素就是一个字符。因此，字符串也可以用切片操作，只是操作结果仍是字符串：
        >>> 'ABCDEFG'[:3]
        'ABC'
        >>> 'ABCDEFG'[::2]
        'ACEG'
        
        (Python没有截取的函数，使用切片就可以解决问题)
        在很多编程语言中，针对字符串提供了很多各种截取函数（例如，substring），其实目的就是对字符串切片。Python没有针对字符串的截取函数，只需要切片一个操作就可以完成，非常简单
</pre>

<pre>
    迭代
        Python的for循环抽象程度要高于C的for循环，因为Python的for循环不仅可以用在list或tuple上，还可以作用在其他可迭代对象上。
        list这种数据类型虽然有下标，但很多其他数据类型是没有下标的，但是，只要是可迭代对象，无论有无下标，都可以迭代，比如dict就可以迭代
    
    for .... in...
        可以使用到list,dict,string上，但是需要注意，map的顺序是不能确定的
        
        dict的迭代
            key迭代: for value in d.values()
            value迭代: for k, v in d.items()
            
    enumerate
        Python内置的enumerate函数可以把一个list变成索引-元素对，这样就可以在for循环中同时迭代索引和元素本身
                
</pre>

<pre>
    列表生成器
        列表生成式则可以用一行语句代替循环生成上面的list
        >>> [x * x for x in range(1, 11)]
        [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
        写列表生成式时，把要生成的元素x * x放到前面，后面跟for循环，就可以把list创建出来，十分有用，多写几次，很快就可以熟悉这种语法
        
        for循环后面还可以加上if判断，这样我们就可以筛选出仅偶数的平方
        >>> [x * x for x in range(1, 11) if x % 2 == 0]
        [4, 16, 36, 64, 100]
        
        两层循环
        >>> [m + n for m in 'ABC' for n in 'XYZ']
        ['AX', 'AY', 'AZ', 'BX', 'BY', 'BZ', 'CX', 'CY', 'CZ']
        
        for循环其实可以同时使用两个甚至多个变量，比如dict的items()可以同时迭代key和value
        >>> d = {'x': 'A', 'y': 'B', 'z': 'C' }
        >>> for k, v in d.items():
        ...     print(k, '=', v)
        
        运用列表生成式，可以写出非常简洁的代码。例如，列出当前目录下的所有文件和目录名，可以通过一行代码实现：
            >>> import os # 导入os模块，模块的概念后面讲到
            >>> [d for d in os.listdir('.')] # os.listdir可以列出文件和目录
            ['.emacs.d', '.ssh', '.Trash', 'Adlm', 'Applications', 'Desktop', 'Documents', 'Downloads', 'Library', 'Movies', 'Music', 'Pictures', 'Public', 'VirtualBox VMs', 'Workspace', 'XCode']        
        
        isinstance :(重点)使用函数来确定数据的类型
        
        把一个list中所有的字符串变成小写
            >>> L = ['Hello', 'World', 'IBM', 'Apple']
            >>> [s.lower() for s in L]
            ['hello', 'world', 'ibm', 'apple']            
        
</pre>