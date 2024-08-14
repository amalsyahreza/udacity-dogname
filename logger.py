import logging
import os
from logging.handlers import RotatingFileHandler


class Logger:
    def __init__(self, name="DogName", log_file="logs/console.log", level=logging.INFO, max_bytes=1024 * 1024, backup_count=3):
        """
        Initializes a logger with a specific name, logging level, and optional file output.

        :param name: Name of the logger.
        :param log_file: Optional file to log messages to. If None, logs only to the console.
        :param level: Logging level (e.g., logging.DEBUG, logging.INFO).
        :param max_bytes: Maximum file size for the rotating file handler (default is 1MB).
        :param backup_count: Number of backup files to keep if using a rotating file handler.
        """
        self.logger = logging.getLogger(name)
        self.logger.setLevel(level)

        # Formatter for the logs
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

        # Console handler for logging to the console
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)
        self.logger.addHandler(console_handler)

        # If a log file is specified, set up a file handler
        if log_file:
            if not os.path.exists(os.path.dirname(log_file)):
                os.makedirs(os.path.dirname(log_file))

            file_handler = RotatingFileHandler(log_file, maxBytes=max_bytes, backupCount=backup_count)
            file_handler.setFormatter(formatter)
            self.logger.addHandler(file_handler)

    def get_logger(self):
        """
        Returns the logger instance.
        """
        return self.logger
