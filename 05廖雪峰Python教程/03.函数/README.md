<pre>
    类型转换
    Python内置的常用函数还包括数据类型转换函数，比如int()函数可以把其他数据类型转换为整数
    >>> int('123')
    123
    >>> int(12.34)
    12
    >>> float('12.34')
    12.34
    >>> str(1.23)
    '1.23'
    >>> str(100)
    '100'
    >>> bool(1)
    True
    >>> bool('')
    False
</pre>

<pre>
    函数定义
        在Python中，定义一个函数要使用def语句，依次写出函数名、括号、括号中的参数和冒号:，然后，在缩进块中编写函数体，函数的返回值用return语句返回。
    
    引用函数的定义
        如果你已经把my_abs()的函数定义保存为abstest.py文件了，那么，可以在该文件的当前目录下启动Python解释器，用from abstest import my_abs来导入my_abs()函数，注意abstest是文件名（不含.py扩展名）    
    
    空函数
        如果想定义一个什么事也不做的空函数，可以用pass语句
        def nop():
            pass
        缺少了pass，代码运行就会有语法错误
    
    参数检查
        调用函数时，如果参数个数不对，Python解释器会自动检查出来，并抛出TypeError
    
    返回多个值
        但其实这只是一种假象，Python函数返回的仍然是单一值,
        因为其实返回值是一个元组(tuple) ,但是，在语法上，返回一个tuple可以省略括号，而多个变量可以同时接收一个tuple，按位置赋给对应的值，所以，Python的函数返回多值其实就是返回一个tuple，但写起来更方便。      
</pre>

<pre>
    默认参数
        def power(x, n=2)
    
    默认参数最大的坑
        默认参数很有用，但使用不当，也会掉坑里。默认参数有个最大的坑
    当你使用默认参数调用时，一开始结果也是对的：
        >>> add_end()
        ['END']
    但是，再次调用add_end()时，结果就不对了：
        >>> add_end()
        ['END', 'END']
        >>> add_end()
        ['END', 'END', 'END']
    默认参数是[]，但是函数似乎每次都“记住了”上次添加了'END'后的list。
    原因解释如下：
    Python函数在定义的时候，默认参数L的值就被计算出来了，即[]，因为默认参数L也是一个变量，它指向对象[]，每次调用该函数，如果改变了L的内容，则下次调用时，默认参数的内容就变了，不再是函数定义时的[]了。
    
    重点记住:
        定义默认参数要牢记一点：默认参数必须指向不变对象！
    
    要修改上面的例子，我们可以用None这个不变对象来实现：
        def add_end(L=None):
            if L is None:
                L = []
            L.append('END')
            return L        
    
        >>> add_end()
        ['END']
        >>> add_end()
        ['END']   
    为什么要设计str、None这样的不变对象呢？因为不变对象一旦创建，对象内部的数据就不能修改，这样就减少了由于修改数据导致的错误。此外，由于对象不变，多任务环境下同时读取对象不需要加锁，同时读一点问题都没有。我们在编写程序时，如果可以设计一个不变对象，那就尽量设计成不变对象。     
</pre>

<pre>
    可变参数
        def calc(*numbers):
            sum = 0
            for n in numbers:
                sum = sum + n * n
            return sum
        定义可变参数和定义一个list或tuple参数相比，仅仅在参数前面加了一个*号。在函数内部，参数numbers接收到的是一个tuple，因此，函数代码完全不变。但是，调用该函数时，可以传入任意个参数，包括0个参数：

    如果已经有一个list或者tuple，要调用一个可变参数怎么办,
    Python允许你在list或tuple前面加一个*号，把list或tuple的元素变成可变参数传进去
        >>> nums = [1, 2, 3]
        >>> calc(*nums)
        14
    *nums表示把nums这个list的所有元素作为可变参数传进去。这种写法相当有用，而且很常见        
</pre>

<pre>
    关键字参数
        可变参数允许你传入0个或任意个参数，这些可变参数在函数调用时自动组装为一个tuple。而关键字参数允许你传入0个或任意个含参数名的参数，这些关键字参数在函数内部自动组装为一个dict。
    例子:    
        def person(name, age, **kw):
            print('name:', name, 'age:', age, 'other:', kw)   
        
        函数person除了必选参数name和age外，还接受关键字参数kw。在调用该函数时，可以只传入必选参数：
            >>> person('Michael', 30)
            name: Michael age: 30 other: {}  
        
        也可以传入任意个数的关键字参数：
            >>> person('Bob', 35, city='Beijing')
            name: Bob age: 35 other: {'city': 'Beijing'}
            >>> person('Adam', 45, gender='M', job='Engineer')
            name: Adam age: 45 other: {'gender': 'M', 'job': 'Engineer'}
            
        和可变参数类似，也可以先组装出一个dict，然后，把该dict转换为关键字参数传进去,
            >>> extra = {'city': 'Beijing', 'job': 'Engineer'}
            >>> person('Jack', 24, **extra)
                name: Jack age: 24 other: {'city': 'Beijing', 'job': 'Engineer'}        
        **extra表示把extra这个dict的所有key-value用关键字参数传入到函数的**kw参数，kw将获得一个dict，注意kw获得的dict是extra的一份拷贝，对kw的改动不会影响到函数外的extra           

    命名关键字参数
        对于关键字参数，函数的调用者可以传入任意不受限制的关键字参数。至于到底传入了哪些，就需要在函数内部通过kw检查。
        仍以person()函数为例，我们希望检查是否有city和job参数：

        def person(name, age, **kw):
            if 'city' in kw:
                # 有city参数
                pass
            if 'job' in kw:
                # 有job参数
                pass
            print('name:', name, 'age:', age, 'other:', kw)
            
        但是调用者仍可以传入不受限制的关键字参数：
             >>> person('Jack', 24, city='Beijing', addr='Chaoyang', zipcode=123456)
        
        如果要限制关键字参数的名字，就可以用命名关键字参数，例如，只接收city和job作为关键字参数。这种方式定义的函数如下：
            def person(name, age, *, city, job):
                print(name, age, city, job)     
                
        和关键字参数**kw不同，命名关键字参数需要一个特殊分隔符*，*后面的参数被视为命名关键字参数。
           >>> person('Jack', 24, city='Beijing', job='Engineer')
                Jack 24 Beijing Engineer   
                
        如果函数定义中已经有了一个可变参数，后面跟着的命名关键字参数就不再需要一个特殊分隔符*了：
           def person(name, age, *args, city, job):
                print(name, age, args, city, job) 
        
        由于调用时缺少参数名city和job，Python解释器把这4个参数均视为位置参数，但person()函数仅接受2个位置参数。
        
        命名关键字参数可以有缺省值，从而简化调用：
           def person(name, age, *, city='Beijing', job):
                print(name, age, city, job)   
        
        由于命名关键字参数city具有默认值，调用时，可不传入city参数：
           >>> person('Jack', 24, job='Engineer')
           Jack 24 Beijing Engineer
        
        使用命名关键字参数时，要特别注意，如果没有可变参数，就必须加一个*作为特殊分隔符。如果缺少*，Python解释器将无法识别位置参数和命名关键字参数:
            def person(name, age, city, job):
            # 缺少 *，city和job被视为位置参数
            pass          
                                
</pre>

<pre>
    参数组合
       在Python中定义函数，可以用必选参数、默认参数、可变参数、关键字参数和命名关键字参数，这5种参数都可以组合使用。但是请注意，参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数。

        比如定义一个函数，包含上述若干种参数：
        
        def f1(a, b, c=0, *args, **kw):
            print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)
        
        def f2(a, b, c=0, *, d, **kw):
            print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw) 
            
        >>> f1(1, 2)
        a = 1 b = 2 c = 0 args = () kw = {}
        >>> f1(1, 2, c=3)
        a = 1 b = 2 c = 3 args = () kw = {}
        >>> f1(1, 2, 3, 'a', 'b')
        a = 1 b = 2 c = 3 args = ('a', 'b') kw = {}
        >>> f1(1, 2, 3, 'a', 'b', x=99)
        a = 1 b = 2 c = 3 args = ('a', 'b') kw = {'x': 99}
        >>> f2(1, 2, d=99, ext=None)
        a = 1 b = 2 c = 0 d = 99 kw = {'ext': None}   
        
    所以，对于任意函数，都可以通过类似func(*args, **kw)的形式调用它，无论它的参数是如何定义的
         
</pre>

<pre>
    Python的函数具有非常灵活的参数形态，既可以实现简单的调用，又可以传入非常复杂的参数。
        默认参数一定要用不可变对象，如果是可变对象，程序运行时会有逻辑错误！
        要注意定义可变参数和关键字参数的语法：
        *args是可变参数，args接收的是一个tuple；
        **kw是关键字参数，kw接收的是一个dict。
        
    以及调用函数时如何传入可变参数和关键字参数的语法：
    可变参数既可以直接传入：func(1, 2, 3)，又可以先组装list或tuple，再通过*args传入：func(*(1, 2, 3))；
    关键字参数既可以直接传入：func(a=1, b=2)，又可以先组装dict，再通过**kw传入：func(**{'a': 1, 'b': 2})。
    使用*args和**kw是Python的习惯写法，当然也可以用其他参数名，但最好使用习惯用法。
    命名的关键字参数是为了限制调用者可以传入的参数名，同时可以提供默认值。
    定义命名的关键字参数在没有可变参数的情况下不要忘了写分隔符*，否则定义的将是位置参数。    
</pre>