"""方法set，添加键、值，如果添加成功则返回True，如果添加失败则返回False"""

from redis import *
if __name__ == '__main__':
    try:
        # 创建StrictRedis对象，与Redis服务器建立连接
        sr = StrictRedis()
        # 添加键name,值为jhon
        result = sr.set('name', 'jhon')
        # 输出了响应结果，如果添加成功则返回True，否则返回False
        print(result)
        result = sr.set('name1', 'damon')
        print(result)
        result = sr.set('name2', 'tina')
        print(result)
    except Exception as e:
        print(e)
