"""方法get，添加键对应的值，如果键存在则返回对应的值，如果键不存在则返回None"""

from redis import *
if __name__ == '__main__':
    try:
        # 创建StrictRedis对象，与Redis服务器建立连接
        sr = StrictRedis()
        # 获取键name的值
        result = sr.get('name')
        # 输出键的值，如果键不存在则返回None
        print(result)
    except Exception as e:
        print(e)
