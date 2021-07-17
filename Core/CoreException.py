class MethodException(Exception):
    def __init__(self, method):
        self.method = method
        print('Request method error, not support {} method, please choose ["GET", "POST","PUT","DELETE"]'.format(method))