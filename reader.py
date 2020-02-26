from req import Caller
import xlrd
import xlwt

class XLSReader():
    def __init__(self,name):
        data=xlrd.open_workbook(name)
        self.table=data.sheet_by_index(0)
        self.nrows=self.table.nrows
        self.ncols=self.table.ncols
        self.header=[]
        for col in range(self.ncols):
            h=self.table.cell(0,col).value
            self.header.append(h)
        print(f"header is :{self.header}")
    def __len__(self):
        return 3

    def __getitem__(self,index):
        if index >= self.__len__():
            raise IndexError
        ret={}
        for col in range(self.ncols):
            item = self.table.cell(index+1,col).value
            ret[self.header[col]]=item
        ret['index']=index+1
        return ret

class XLSWriter():
    def __init__(self,name,header):
        workbook = xlwt.Workbook(encoding = 'ascii')
        worksheet = workbook.add_sheet('My Worksheet')
        style = xlwt.XFStyle() # 初始化样式
        font = xlwt.Font() # 为样式创建字体
        font.name = 'Times New Roman' 
        style.font = font # 设定样式
        self.name=name
        self.worksheet=worksheet
        self.workbook=workbook
        self.style=style
        self.header=header
        self.cur_row=1

        for ind,h in enumerate(header):
            worksheet.write(0,ind,h)

    def insert(self,item:dict):
        for ind,h in enumerate(self.header):
            self.worksheet.write(self.cur_row,ind,item[h],self.style)
        self.cur_row=self.cur_row+1

    def save(self):
        self.workbook.save(self.name)

keys=['1045209d4f9bc833843441ab0c467269']

if __name__=='__main__':
    r=XLSReader('data.xlsx')
    w=XLSWriter('data2.xls',r.header)
    c=Caller(keys[0])
    for i in r:
        city=i['city']
        locations=i['location'].split(';')
        loc_out=[]
        for l in locations:
            loc=c.get_geo(city,l)
            print(city,l,loc)
            loc_out.append(loc)
        print(loc_out)
        loc_str=''
        for l in loc_out:
            loc_str+=f'({l[0]},{l[1]}),'
        i['location']=loc_str
        w.insert(i)
        print(i['index'])
    w.save()