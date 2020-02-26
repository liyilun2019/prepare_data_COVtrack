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
        return self.nrows

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

keys=['b96c9a530e17f21ebb195b335f3d1185','6f79cd6692a55591d95172847171f00c']

if __name__=='__main__':
    # with open('exception.txt','w') as f:
    r=XLSReader('data3.xls')
    w=XLSWriter('data4.xls',r.header)
    c=Caller(keys)
    cnt=0
    for i in r:
        city=i['city']
        locations=i['location'].split(';')
        loc_str=''
        for l in locations:
            if(l==''):
                break
            if(not l[1].isdigit()):
                print(l[1:-1])
                cnt+=1
        #         try:
        #             loc=c.get_geo(address=l[1:-1],city=city)
        #         except Exception as e:
        #             loc=f'{l};'
        #         # f.write(f'{w.cur_row},{city},{l}'+'\n')
        #     else :
        #         loc=f'{l};'
        #     # print(l,city,loc)
        #     loc_str=loc_str+loc
        # i['location']=loc_str
        # w.insert(i)
        # print(i['index'])
    print(cnt)
    # w.save()