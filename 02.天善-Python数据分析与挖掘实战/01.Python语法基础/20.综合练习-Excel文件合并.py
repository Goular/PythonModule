import xlrd, xlsxwriter

# 设置要合并的所有文件
allxls = ["./1.xlsx", "./2.xlsx"]
# 设置合并到的文件路径
endxls = "./endxls.xlsx"


# 打开表格
def open_xls(file):
    try:
        fh = xlrd.open_workbook(file)
        return fh
    except Exception as err:
        print("打开出错，错误为:" + err)


# 获取所有sheet
def getSheet(fh):
    return fh.sheets()


# 读取某个sheet的行数
def getnrows(fh, sheet):
    table = fh.sheets()[sheet]
    content = table.nrows
    return content


# 读取某个文件的内容并返回所有行的值
def getFilect(fh, fl, shunum):
    fh = open_xls(fl)
    table = fh.sheet_by_name(shname[shunum])
    num = getnrows(fh, shunum)
    lenrvalue = len(rvalue)
    for row in range(0, num):
        rdata = table.row_values(row)
        rvalue.append(rdata)
    filevalue.append(rvalue[lenrvalue])
    return filevalue


# 存储所有的读取结果
filevalue = []
# 存储一个标签的结果
svalue = []
# 存储一行结果
rvalue = []
# 存储各个sheet的名称
shname = []
