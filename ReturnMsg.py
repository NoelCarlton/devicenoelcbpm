class ReturnMsg:
    __status = 0
    __msg = "成功"

    def __init__(self, status, msg):
        self.__status = status
        self.__msg = msg