import time


class TimeUtil:
    default_formater = "%Y-%m-%d %H:%M:%S"

    def __init__(self):
        pass

    @staticmethod
    def get_current_timestamp():
        return time.time()

    @classmethod
    def get_timestamp_from_string(cls, time_string, formater):
        formater = formater if formater else cls.default_formater
        return time.mktime(time.strptime(time_string, formater))

    @classmethod
    def get_current_time(cls, formater=None):
        formater = formater if formater else cls.default_formater
        return time.strftime(formater, time.localtime())


if __name__ == "__main__":
    TimeUtil.get_current_time()
    TimeUtil.get_current_time(formater="%a %b %d %H:%M:%S %Y")
