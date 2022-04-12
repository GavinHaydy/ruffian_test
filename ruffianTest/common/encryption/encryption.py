import base64
import hashlib
import hmac

"""
@description: 加密方法
"""


def to_md5(s: str, encode: str):
    '''
    :param s: String to be encrypted
    :param encode: String encoding such as UTf8 UTf16
    :return:  md5(str)
    '''
    result = hashlib.md5()
    if encode == 'utf16' or encode == 'utf-16':
        result.update(s.encode(encode)[2:])
    else:
        result.update(s.encode(encode))
    return result.digest()


def md5_base64(bytes_str):
    '''
    : param bytes_str: __to_md5()
    :return: md5(base64):str
    '''
    return base64.b64encode(bytes_str).decode('utf8')


class Encryption:
    def __init__(self, not_encrypted_str, mode='md5', encoding='utf8', key=''):
        """

        :param not_encrypted_str: 未加密字符串
        :param mode: 加密方式 md5、sha256...
        :param encoding: 字符串编码 utf8 utf16
        :param key: 盐 可选
        """
        self.mode = mode  # Es = Encrypted string
        self.key = key
        self.NES = not_encrypted_str
        self.encoding = encoding
    def encryption(self):
        '''
        :return: 加密后的字符串
        '''
        if self.key == '':
            if self.encoding == 'utf16':
                encrypted_string = hashlib.new(self.mode, bytes(self.NES, encoding='utf-16')[2:]).hexdigest()
            else:
                encrypted_string = hashlib.new(self.mode, bytes(self.NES, encoding='utf-8')).hexdigest()
            return encrypted_string
        else:
            if self.encoding == 'utf16':
                encrypted_string = hmac.new(
                    bytes(self.key, encoding='utf-8'), bytes(self.NES, encoding='utf-16')[2:], self.mode)
            else:
                encrypted_string = hmac.new(
                    bytes(self.key, encoding='utf-8'), bytes(self.NES, encoding='utf-8'), self.mode)
            return encrypted_string.hexdigest()

    def md5_base64(self):
        '''
        :return: md5(base64):str
        '''
        return md5_base64(to_md5(self.NES, self.encoding))
