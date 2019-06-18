"""方法keys,根据正则表达式获取键"""

from redis import *
if __name__ == '__main__':
    try:
        # 创建StrictRedis对象，与Redis服务器建立连接
        sr = StrictRedis()
        # 获取所有的键
        result = sr.keys()
        # 输出响应结果，所有的键构成一个列表，如果没有键则返回空列表
        print(result)
    except Exception as e:
        print(e)
