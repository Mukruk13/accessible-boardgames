#utils/log_app_banner.py

import logging

logger = logging.getLogger(__name__)

def log_app_banner():
    logger.info("\n" + "-" * 120)
    logger.info("🚀 NEW APPLICATION SESSION STARTED")
    logger.info("-" * 63)
