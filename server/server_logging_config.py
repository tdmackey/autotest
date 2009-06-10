import common
import logging, os
from autotest_lib.client.common_lib import logging_config

class ServerLoggingConfig(logging_config.LoggingConfig):
    def add_debug_file_handlers(self, log_dir, log_name=None):
        if not log_name:
            log_name = 'autoserv'
        self.add_file_handler(log_name + '.stdout', logging.DEBUG,
                              log_dir=log_dir)
        self.add_file_handler(log_name + '.stderr', self.STDERR_LEVEL,
                              log_dir=log_dir)


    def configure_logging(self, results_dir=None, use_console=True):
        super(ServerLoggingConfig, self).configure_logging(use_console)

        if results_dir:
            log_dir = os.path.join(results_dir, 'debug')
            if not os.path.exists(log_dir):
                os.mkdir(log_dir)
            self.add_debug_file_handlers(log_dir)
