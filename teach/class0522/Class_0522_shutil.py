import shutil
import os

# 切换当前操作目录
os.chdir("D:/")

# 复制文件对象
# inobj = open("linux系统密码.txt", 'r', encoding='utf-8')
# outobj = open("copy/a/a_pwd.txt", 'w', encoding='utf-8')
# shutil.copyfileobj(inobj, outobj)

# 复制文件
# shutil.copyfile('linux系统密码.txt', 'copy/b/b_pwd.txt')

# 复制权限
# shutil.copymode('linux系统密码.txt', 'copy/b/b_pwd.txt')

# 复制文件状态
# shutil.copystat('linux系统密码.txt', 'copy/b/b_pwd.txt')

# 复制文件或目录
# shutil.copy('temp.png', 'temp0522/')
# shutil.copy('temp0522', 'aaa')

# 复制文件 以及元信息
# shutil.copy2('linux系统密码.txt', 'temp0522/')

# 复制目录树
# shutil.copytree('aaa', 'temp0522_2', ignore=shutil.ignore_patterns('temp*'))

# 删除目标树
# shutil.rmtree('temp0522_2')

# 移动
shutil.move('temp0522_1', 'temp0522')
