# -*- coding: utf-8 -*-
import subprocess
#查看工作区状态
def status():
    archiveCmd = 'git status'
    process = subprocess.Popen(archiveCmd,shell=True,stdout=subprocess.PIPE)
    process.wait()
    returndata = process.communicate()
    returndata = str(returndata[0], encoding = "utf-8")
    print(returndata)
    status = returndata.replace('\n','').replace('*','').replace(' ','')
    nothing = 'nothing'
    archiveReturnCode = process.returncode
    if archiveReturnCode != 0:
        print("git status fail")
    else:      
        if nothing in status:
            if 'ahead' in status:
                push()
            else:
                print('nothing to commit')
        else:
            add()

#添加工作区
def add():
    archiveCmd = 'git add --all'
    process = subprocess.Popen(archiveCmd,shell=True)
    process.wait()
    archiveReturnCode = process.returncode
    if archiveReturnCode != 0:
        print("add fail")
    else:
        print("**********add success")
        commit()

#提交本地版本库
def commit():
    inputNote = input("please input commit message:")
    archiveCmd = "git commit -m ' " + inputNote + "'"
    process = subprocess.Popen(archiveCmd,shell=True)
    process.wait()
    archiveReturnCode = process.returncode
    if archiveReturnCode != 0:
        print("commit fail")
    else:
        print("********committed:",inputNote)
        pull()
#拉取
def pull():
    archiveCmd = 'git pull'
    process = subprocess.Popen(archiveCmd,shell=True)
    process.wait()
    archiveReturnCode = process.returncode
    if archiveReturnCode != 0:
        print("pull fail")
    else:
        push()
#推送
def push():
    archiveCmd = 'git push'
    process = subprocess.Popen(archiveCmd,shell=True)
    process.wait()
    archiveReturnCode = process.returncode
    if archiveReturnCode != 0:
        print("git push fail")
    else:
        print("********git push success")
#执行自身
def main():
    status()

if __name__ == '__main__':
    main()
