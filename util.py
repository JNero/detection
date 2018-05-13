import os
import subprocess
import re

def php_opencode(filename):
    """
    转化为opencode
    :param filename:
    :return:
    """
    try:
        output= subprocess.check_output(['php.exe', '-dvld.active=1', '-dvld.execute=0', filename],stderr=subprocess.STDOUT)
        tokens = re.findall(r's(b[A-Z_]+b)s', output)
        print(tokens)
        t = " ".join(tokens)
        print(t)
        return t
    except:
        return("")
def get_php_file(dir):
    """
    获取php 文件
    :param dir:
    :return:
    """
    files_list=[]
    for root ,dirs,files in os.walk(dir):
        count=0
        for filename in files:
            if filename.endswith('.php'):
                try:

                    full_path=os.path.join(root,filename)
                    opencode_file=php_opencode(full_path)
                    count=count+1
                    print("num is {}get_opencode{}".format(count,full_path))
                    files_list.append(opencode_file)
                except:
                    continue


if __name__ == '__main__':
    get_php_file("D:\di")
