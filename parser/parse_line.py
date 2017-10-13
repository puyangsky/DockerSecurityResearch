# -*- coding: utf-8 -*-
# @author puyangsky

import command
import logging
import logging.config

logging.config.fileConfig("../logger.conf")
logger = logging.getLogger("parse_line")


if __name__ == '__main__':
    logger.info(command.Add)