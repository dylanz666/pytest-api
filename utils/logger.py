import os
import logging
from collections import defaultdict
from datetime import datetime
from utils.file_util import FileUtil

log_path = os.path.join(os.getcwd(), 'logs')


class Logger:
    loggers = defaultdict(logging.getLogger)

    @classmethod
    def initialize(cls):
        FileUtil.makedirs_if_not_exist(log_path)
        now = datetime.now()
        date_str = f"{now.year}-{now.month:02d}-{now.day:02d}"
        cls.log_filename = os.path.join(log_path, f"{date_str}.log")

        # Check if the corresponding logger already exists
        if cls.loggers.get(date_str) is not None:
            return

        # Define a logger container
        logger = logging.getLogger(date_str)
        logger.setLevel(logging.DEBUG)
        cls.loggers[date_str] = logger

        # Create the log input format
        cls.formatter = logging.Formatter(
            '[%(asctime)s][%(levelname)s] %(message)s', datefmt='%Y-%m-%d %H:%M:%S')

        # Create a file handler to store log files
        cls.filelogger = logging.FileHandler(cls.log_filename, mode='a', encoding='utf-8')
        cls.console = logging.StreamHandler()

        # Set the log level for console and file
        cls.console.setLevel(logging.DEBUG)
        cls.filelogger.setLevel(logging.DEBUG)

        # Set the log format
        cls.filelogger.setFormatter(cls.formatter)
        cls.console.setFormatter(cls.formatter)
        logger.addHandler(cls.filelogger)
        logger.addHandler(cls.console)

        cls.loggers[date_str] = logger

    @staticmethod
    def get_logger():
        now = datetime.now()
        date_str = f"{now.year}-{now.month:02d}-{now.day:02d}"
        return Logger.loggers[date_str]

    @staticmethod
    def format_log_info(*info):
        return ' '.join(str(info_item) for info_item in info)

    @classmethod
    def info(cls, *info) -> None:
        log_info = cls.format_log_info(*info)
        Logger.get_logger().info(log_info)

    @classmethod
    def warning(cls, *info) -> None:
        log_info = cls.format_log_info(*info)
        Logger.get_logger().warning(log_info)

    @classmethod
    def error(cls, *info) -> None:
        log_info = cls.format_log_info(*info)
        Logger.get_logger().error(log_info)

    @classmethod
    def debug(cls, *info) -> None:
        log_info = cls.format_log_info(*info)
        Logger.get_logger().debug(log_info)

    @classmethod
    def critical(cls, *info) -> None:
        log_info = cls.format_log_info(*info)
        Logger.get_logger().critical(log_info)


# Initialize Logger
Logger.initialize()

if __name__ == "__main__":
    Logger.info("this is an info log", 123)
    Logger.debug("this is a debug log", 123)
    Logger.error("this is an error log", 123)
    Logger.critical("this is a critical log", 123)
    Logger.warning("this is a warn log", 123)
