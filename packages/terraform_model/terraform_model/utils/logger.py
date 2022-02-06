# std
import logging


class Log:
    _CRITICAL_LEVEL = 50
    _ERROR_LEVEL = 40
    _WARNING_LEVEL = 30
    _INFO_LEVEL = 20
    _VERBOSE_LEVEL = 15
    _DEBUG_LEVEL = 10
    _TRACE_LEVEL = 5
    _SILLY_LEVEL = 1
    _NOTSET_LEVEL = 0
    _log_levels = {
        'critical': _CRITICAL_LEVEL,
        'error': _ERROR_LEVEL,
        'warning': _WARNING_LEVEL,
        'info': _INFO_LEVEL,
        'verbose': _VERBOSE_LEVEL,
        'debug': _DEBUG_LEVEL,
        'trace': _TRACE_LEVEL,
        'silly': _SILLY_LEVEL,
        'notset': _NOTSET_LEVEL,
    }
    _verbosity_levels = {
        0: 'warning',
        1: 'info',
        2: 'verbose',
        3: 'debug',
        4: 'trace',
        5: 'silly',
    }

    def __init__(self, level: str = 'warning'):
        self._logger = logging.getLogger('terraform-model')
        self._logger.addHandler(logging.StreamHandler())
        self.set_level(level)

    def set_level(self, level: str):
        self._logger.setLevel(self._convert_level(level))

    def _convert_level(self, level: str) -> int:
        return self._log_levels.get(level, 30)

    def set_verbosity(self, number: int = 0):
        self.set_level(self._convert_verbosity_to_level(number))

    def _convert_verbosity_to_level(self, number: int) -> str:
        return self._verbosity_levels.get(number, 'silly')

    def critical(self, msg: str, *args, **kwargs):
        self._logger.log(self._CRITICAL_LEVEL, f'[CRITICAL] {msg}', *args, **kwargs)

    def error(self, msg: str, *args, **kwargs):
        self._logger.log(self._ERROR_LEVEL, f'[ERROR] {msg}', *args, **kwargs)

    def warning(self, msg: str, *args, **kwargs):
        self._logger.log(self._WARNING_LEVEL, f'[WARNING] {msg}', *args, **kwargs)

    def info(self, msg: str, *args, **kwargs):
        self._logger.log(self._INFO_LEVEL, msg, *args, **kwargs)

    def verbose(self, msg: str, *args, **kwargs):
        self._logger.log(self._VERBOSE_LEVEL, msg, *args, **kwargs)

    def debug(self, msg: str, *args, **kwargs):
        self._logger.log(self._DEBUG_LEVEL, msg, *args, **kwargs)

    def trace(self, msg: str, *args, **kwargs):
        self._logger.log(self._TRACE_LEVEL, msg, *args, **kwargs)

    def silly(self, msg: str, *args, **kwargs):
        self._logger.log(self._SILLY_LEVEL, msg, *args, **kwargs)

    def test(self):
        self.critical('[CRITICAL] testing logger')
        self.error('[ERROR] testing logger')
        self.warning('[WARNING] testing logger')
        self.info('[INFO] testing logger')
        self.verbose('[VERBOSE] testing logger')
        self.debug('[DEBUG] testing logger')
        self.trace('[TRACE] testing logger')
        self.silly('[SILLY] testing logger')


log = Log()
