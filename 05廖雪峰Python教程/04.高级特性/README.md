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
    列表生成式
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

<pre>
    生成器 (其实就是推算，生成的只是一个结果，而不是像列表生成式那样返回一个列表)
        通过列表生成式，我们可以直接创建一个列表。但是，受到内存限制，列表容量肯定是有限的。而且，创建一个包含100万个元素的列表，不仅占用很大的存储空间，如果我们仅仅需要访问前面几个元素，那后面绝大多数元素占用的空间都白白浪费了。
        如果列表元素可以按照某种算法推算出来，那我们是否可以在循环的过程中不断推算出后续的元素呢？这样就不必创建完整的list，从而节省大量的空间。在Python中，这种一边循环一边计算的机制，称为生成器：generator。
        要创建一个generator，有很多种方法。第一种方法很简单，只要把一个列表生成式的[]改成()，就创建了一个generator
        
        generator保存的是算法，每次调用next(g)，就计算出g的下一个元素的值，直到计算到最后一个元素，没有更多的元素时，抛出StopIteration的错误。
        我们创建了一个generator后，基本上永远不会调用next()，而是通过for循环来迭代它，并且不需要关心StopIteration的错误
        
        generator非常强大。如果推算的算法比较复杂，用类似列表生成式的for循环无法实现的时候，还可以用函数来实现。
    
    yield
        要把fib函数变成generator，只需要把print(b)改为yield b就可以了
         def fib(max):
            n, a, b = 0, 0, 1
            while n < max:
                yield b
                a, b = b, a + b
                n = n + 1
            return 'done' 
    这就是定义generator的另一种方法。如果一个函数定义中包含yield关键字，那么这个函数就不再是一个普通函数，而是一个generator：        
    >>> f = fib(6)
    >>> f
    <generator object fib at 0x104feaaa0>
    
    这里，最难理解的就是generator和函数的执行流程不一样。函数是顺序执行，遇到return语句或者最后一行函数语句就返回。而变成generator的函数，在每次调用next()的时候执行，遇到yield语句返回，再次执行时从上次返回的yield语句处继续执行。

    定义一个generator，依次返回数字1，3，5
    def odd():
        print('step 1')
        yield 1
        print('step 2')
        yield(3)
        print('step 3')
        yield(5)
        
    调用该generator时，首先要生成一个generator对象，然后用next()函数不断获得下一个返回值：
    >>> o = odd()
    >>> next(o)
    step 1
    1
    >>> next(o)
    step 2
    3
    >>> next(o)
    step 3
    5
    >>> next(o)
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    StopIteration   
    
    可以看到，odd不是普通函数，而是generator，在执行过程中，遇到yield就中断，下次又继续执行。执行3次yield后，已经没有yield可以执行了，所以，第4次调用next(o)就报错
    回到fib的例子，我们在循环过程中不断调用yield，就会不断中断。当然要给循环设置一个条件来退出循环，不然就会产生一个无限数列出来。
    
    同样的，把函数改成generator后，我们基本上从来不会用next()来获取下一个返回值，而是直接使用for循环来迭代：
    >>> for n in fib(6):
    ...     print(n)
    ...
    1
    1
    2
    3
    5
    8
    
    但是用for循环调用generator时，发现拿不到generator的return语句的返回值。如果想要拿到返回值，必须捕获StopIteration错误，返回值包含在StopIteration的value中：
    即拿回fib(max)的 return的内容，
    
    >>> g = fib(6)
    >>> while True:
    ...     try:
    ...         x = next(g)
    ...         print('g:', x)
    ...     except StopIteration as e:
    ...         print('Generator return value:', e.value)
    ...         break
    ...
    g: 1
    g: 1
    g: 2
    g: 3
    g: 5
    g: 8
    Generator return value: done
    
    小结：
        generator是非常强大的工具，在Python中，可以简单地把列表生成式改成generator，也可以通过函数实现复杂逻辑的generator。
        要理解generator的工作原理，它是在for循环的过程中不断计算出下一个元素，并在适当的条件结束for循环。对于函数改成的generator来说，遇到return语句或者执行到函数体最后一行语句，就是结束generator的指令，for循环随之结束。
        请注意区分普通函数和generator函数，普通函数调用直接返回结果：
        
        >>> r = abs(6)
        >>> r
        6
        generator函数的“调用”实际返回一个generator对象：
        
        >>> g = fib(6)
        >>> g
        <generator object fib at 0x1022ef948> 
</pre>

<pre>
    数值交换
        Python的a和b之间的数值交换，可以直接写成 a,b = b,a
</pre>