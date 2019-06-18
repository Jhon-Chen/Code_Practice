"""方法delete，删除键及对应的值，如果删除成功则返回受影响的键数，否则则返回0"""

from redis import *
if __name__ == '__main__':
    try:
        # 创建StrictRedis对象，与Redis服务器建立连接
        sr = StrictRedis()
        # 设置键name的值，如果键已经存在则进行修改，如果键不存在则进行添加
        result = sr.set('name', 'damon')
        # 输出响应结果，如果删除成功则返回受影响的键数，否则则返回0
        result = sr.delete('name')

        print(result)
    except Exception as e:
        print(e)
        
