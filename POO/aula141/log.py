#abstração

from pathlib import Path

LOG_FILE = Path(__file__).parent / 'log.txt'

class Log:
    def _log(self, msg):
        raise NotImplementedError('Implemente o método log')
    
    def log_error(self, msg):
        return self._log(f'Erro: {msg}')
    
    def log_success(self, msg):
        return self._log(f'Success: {msg}')
    
class logFileMixin(Log): # um mixim é uma classe para criar métodos para outras classes
    def _log(self, msg):
        msg_format = f'{msg} {self.__class__.__name__}'
        with open(LOG_FILE, 'a') as arquivo:
            arquivo.write(msg_format)
            arquivo.write('\n')
    
class LogPrintMixin(Log):
    def _log(self, msg):
        print(f'{msg} ({self.__class__.__name__})')
        
if __name__ == '__main__':
    l = logFileMixin()
    l.log_error('Teste')
    l.log_success('Teste 1')
    print(LOG_FILE)