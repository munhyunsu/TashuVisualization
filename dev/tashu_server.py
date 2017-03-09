#!/usr/bin/python3

import configparser
import sys
import logging
from http.server import HTTPServer
from http.server import CGIHTTPRequestHandler


INIFILE = 'tashu_server.ini'


class TashuServerHandler(CGIHTTPRequestHandler):
    # print nothing!
    def log_message(self, format, *args):
        logging.debug('{0} {1} {2}'.format(
                     self.client_address, self.command, self.path))
        return

def main():
    """HTTP 서버 데몬 생성
    """
    # ini 파일 위치 확인
    config_file = INIFILE
    config = configparser.ConfigParser()
    config.read(config_file)
    # ini 서버 옵션
    if not 'server' in config:
        logging.critical('설정 파일에 server 세션이 필요합니다.')
        sys.exit(0)
    if not 'port' in config['server']:
        logging.critical('설정 파일 server 세션에 '
                        + 'port 항목이 필요합니다.')
        sys.exit(0)
    http_port = int(config['server']['port'])
    # ini 로그 옵션
    if not 'log' in config:
        logging.critical('설정 파일에 log 세션이 필요합니다.')
        sys.exit(0)
    if not 'level' in config['log']:
        logging.critical('설정 파일 log 세션에 '
                        + 'level 항목이 필요합니다.')
        sys.exit(0)
    if not 'file' in config['log']:
        logging.critical('설정 파일 log 세션에 '
                        + 'file 항목이 필요합니다.')
        sys.exit(0)
    # 로그 레벨, 파일 이름 불러오기
    log_level = getattr(logging, config['log']['level'])
    log_file = config['log']['file']
    # 로그 레벨 세팅
    logging.basicConfig(filename = log_file,
                        level = log_level,
                        format = '%(asctime)s '
                               + '%(levelname)s:'
                               + '%(message)s',
                        datefmt = '%Y.%m.%d %H:%M:%S')
    # HTTP 데몬 생성
    try:
        logging.info('서버를 시작합니다. 중지하려면 Ctrl+C를 누르세요.')
        tashu_server = HTTPServer(('', http_port),
                                          TashuServerHandler)
        tashu_server.serve_forever()
    except KeyboardInterrupt:
        logging.info('서버를 중지합니다.')

if __name__ == '__main__':
    main()
