# !/usr/bin/env Python
# -*- coding:utf-8 -*-
# memo.py
# author:chen


import pickle


class Memo():
    
    def __init__(self,name,thing,date):
        self._id = 0
        self.name = name
        self.thing = thing 
        self.date = date
   
    @property
    def id(self):
        "使_id变成属性"
        return self._id
    
    def set_id(self,num):
        "id值自增"
        self._id = num+1

class MemoAdmin():
    """51备忘录的添删改查功能"""
    
    def __init__(self):
        self.memo_list = self.load()
     
    def load(self):
        "读取文件"
        if (self.load): 
            # 做判断，看读取是否为空
            with open('db.pkl', 'wb') as f:
                #写入文件
                pickle.dump([],f)

            with open('db.pkl', 'rb') as f:
                data = pickle.load(f)
                return data
        
        else:
            with open('db.pkl', 'rb') as f:
                #读取文件
                data = pickle.load(f)
                return data
        

    def save(self):
        "写入文件"
        with open('db.pkl','wb')as f:
            f.write(pickle.dumps(self.memo_list))


    def add_memo(self):
        "添加备忘录"
        name = input('请输入备忘录的名字：')
        
        for memo in self.memo_list:
            if memo.name == name:
                print('备忘录已存在！')
                
                break
        else: # 此处并非if判断语句中的else，而是for循环全部走完后才执行的else
            add_thing = input('请输入要记录的事件：')
            add_date = input('请输入时间：')
            memo = Memo(name,add_thing,add_date)
            memo.set_id(self.max_id())
            # 设置id
            self.memo_list.append(memo)
            # 将内容添加至备忘录列表
            self.save()
            # 保存备忘录
    
    def delete_memo(self):
        "删除备忘录"
        if self.memo_list:
            # 判断备忘录是否为空
            name = input('请输入备忘录的名字：')
            for index,memo in enumerate(self.memo_list):
                
                if memo.name == name:
                    # 判断备忘录中有无此备忘录名称
                    del self.memo_list[index]
                else:
                    print('备忘录中无此名字！')
            self.save()
        else:
            print('备忘录为空，无可删除内容，请先添加！')
    
    def modify_memo(self):
        "修改备忘录"
        if self.memo_list:
            "判断备忘录是否为空"
            name = input('请输入备忘录的名字：')
            for memo in self.memo_list:
                if memo.name == name:
                    # 判断备忘录中有无此备忘录名称
                    modify_thing = input('请输入修改的事件：')
                    modify_date = input('请输入修改的时间：')
                    memo.thing = modify_thing
                    memo.date = modify_date
                    print('备忘录已修改完毕！')
                    break
                    self.save()
                else:
                    print('无此备忘录名称')
        else:
            print('备忘录为空，无可修改内容，请先添加！')
    
    def query_memo(self):
        "查询备忘录"
        if self.memo_list:
            # 判断备忘录是否为空
            for memo in self.memo_list:
                print(f'序号{memo.id}\t备忘录名称：{memo.name}\t事件：{memo.thing}\t时长：{memo.date}')    
        else:
            print('备忘录为空，请添加！')        
            
    def max_id(self):
        "取最大id值"
        if self.memo_list:
            # 判断备忘录列表是否为空，不为空则取最后一个对象的id值
            return self.memo_list[-1].id
        else:
            # 若列表为空，则取0
            return 0        
    
    def exit_memo(self):
        "退出备忘录"
        exit()
            
    def interactive(self):
        "交互界面"
        # 界面显示
        desc = '51备忘录'.center(20,'*')
        menu_desc = {
            '1':'添加备忘录',
            '2':'删除备忘录',
            '3':'修改备忘录',
            '4':'查询备忘录',
            '0':'退出备忘录'
        }
        # 菜单相对应功能
        menu = {
            '1':'add_memo',
            '2':'delete_memo',
            '3':'modify_memo',
            '4':'query_memo',
            '0':'exit_memo'
        }
        print(desc)
        for k,v in menu_desc.items():
            print(k, v)

        while True:
            choose = input('请选择您要的操作：')
            if hasattr(self,menu.get(choose)):
                # 判断功能是否存在
                func = getattr(self,menu.get(choose))
                # 获取此功能
                func()
                # 执行此功能


def main():
    admin = MemoAdmin()
    admin.interactive()

if __name__ == '__main__':
    main()








