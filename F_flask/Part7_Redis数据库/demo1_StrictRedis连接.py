
from redis import *

if __name__ == '__main__':
    try:
    # 创建StrictRedis对象，与Redis服务器建立连接
        sr = StrictRedis()

    except Exception as e:
        print(e)
                                           
