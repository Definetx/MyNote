#!/usr/bin/env python3
"""
import fileinput
with fileinput.input() as f_input:
    for line in f_input:
        print(line, end='')
"""
import logging
import logging.config

def main():
    logging.basicConfig(
        filename="test.log",
        level=logging.WARNING,
        format="%(levelname)s:%(asctime)s:%(message)s"
    )

    hostname = 'www.python.org'
    item = 'spam'
    filename = 'data.csv'
    mode = 'r'

    logging.critical("host %s unknown", hostname)
    logging.error("couldn't find %r", item)
    logging.warning("feature is deprecated")
    logging.info("opening file %r, mode=%r", filename, mode)
    logging.debug('got here')

def test():
    logging.config.fileConfig('logconfig.ini')

if __name__ == "__main__":
    main()
