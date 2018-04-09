# coding=utf8

import uuid

class GUID:
    def __init__(self):
        pass

    @staticmethod
    def new_uuid(upper_=True, *format_):
        """
        生成新的uuid字符串
        格式为：xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx
        uuid1(): 基于计算机主机ID和当前时间生成的UUID
        :param upper_: 大小写转换标记
        :param format_: 参数 b、o、x
        :return: uuid字符串
        """
        uuid_ = str(uuid.uuid1())
        if len(format_) == 0:
            uuid_str = uuid_.lower()
        else:
            uuid_str = '{0:' + format_ + '}'.format(uuid_).lower()
        if upper_:
            uuid_str = uuid_.upper()
        return uuid_str

    @staticmethod
    def format(olduuid_, upper_=True, *format_):
        '''
        从已有的uuid字符串转化
        格式为：xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx
        uuid1(): 基于计算机主机ID和当前时间生成的UUID
        :param olduuid_: 符合uuid格式的字符串
        :param upper_: 大小写转换标记
        :param format_: 参数 b、o、x
        :return: 
        '''
        uuid_ = uuid.UUID(olduuid_)
        if len(format_) == 0:
            uuid_str = uuid_.lower()
        else:
            uuid_str = '{0:'+format_+'}'.format(uuid_).lower()
        if upper_:
            uuid_str = uuid_str.upper()
        return uuid_str