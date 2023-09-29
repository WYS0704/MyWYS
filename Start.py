#此文件没有什么厉害的功能
import time



print('Welcome')
time.sleep(2)
while True:    
    print('''
1.退出
2.日历
''')
    i=input('请输入相应的数字编号(如果不是,将重启):')
    if i==str(1):
        break
    elif i==str(2):
        time.sleep(1)
        print('当前时间:'+time.ctime())
        time.sleep(1)
        continue
    else:
        print('无效指令')
        continue
print('Loding...')
time.sleep(2)
