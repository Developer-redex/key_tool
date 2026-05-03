"""
المشروع: أداة تسجيل ضغطات لوحة المفاتيح
الملف: logger_setup.py
الوصف: إعداد نظام التسجيل المركزي (Logging)
"""

import logging
import logging.handlers
import os
from config import LOG_DIR, LOG_LEVEL, LOG_FORMAT, LOG_FILE_MAX_SIZE, LOG_FILE_BACKUP_COUNT


class ColoredFormatter(logging.Formatter):
    """معالج التنسيق بألوان جميلة للسجلات"""
    
    COLORS = {
        'DEBUG': '\033[36m',      # Cyan
        'INFO': '\033[32m',       # Green
        'WARNING': '\033[33m',    # Yellow
        'ERROR': '\033[31m',      # Red
        'CRITICAL': '\033[41m',   # Red background
    }
    RESET = '\033[0m'
    
    def format(self, record):
        # إضافة اللون
        levelname = record.levelname
        if levelname in self.COLORS:
            record.levelname = f"{self.COLORS[levelname]}{levelname}{self.RESET}"
        
        return super().format(record)


def setup_logger(name: str) -> logging.Logger:
    """
    إعداد logger مركزي مع ملفات وشاشة
    
    Args:
        name (str): اسم Logger
        
    Returns:
        logging.Logger: كائن Logger معدّ
    """
    
    # التأكد من وجود مجلد السجلات
    os.makedirs(LOG_DIR, exist_ok=True)
    
    # إنشاء logger
    logger = logging.getLogger(name)
    logger.setLevel(getattr(logging, LOG_LEVEL))
    
    # تجنب إضافة handlers متعددة
    if logger.handlers:
        return logger
    
    # ════════════════════════════════════════════════════════════
    #  Handler للملفات (مع تدوير تلقائي)
    # ════════════════════════════════════════════════════════════
    log_file = os.path.join(LOG_DIR, f"{name}.log")
    file_handler = logging.handlers.RotatingFileHandler(
        log_file,
        maxBytes=LOG_FILE_MAX_SIZE,
        backupCount=LOG_FILE_BACKUP_COUNT,
        encoding='utf-8'
    )
    file_handler.setLevel(logging.DEBUG)
    file_formatter = logging.Formatter(LOG_FORMAT)
    file_handler.setFormatter(file_formatter)
    logger.addHandler(file_handler)
    
    # ════════════════════════════════════════════════════════════
    #  Handler للشاشة (Console)
    # ════════════════════════════════════════════════════════════
    console_handler = logging.StreamHandler()
    console_handler.setLevel(getattr(logging, LOG_LEVEL))
    console_formatter = ColoredFormatter(LOG_FORMAT)
    console_handler.setFormatter(console_formatter)
    logger.addHandler(console_handler)
    
    return logger


# إنشاء logger عام للمشروع
app_logger = setup_logger("key_tool")


if __name__ == "__main__":
    """اختبار نظام التسجيل"""
    logger = setup_logger("test")
    
    logger.debug("🔵 رسالة DEBUG")
    logger.info("🟢 رسالة INFO")
    logger.warning("🟡 رسالة WARNING")
    logger.error("🔴 رسالة ERROR")
    logger.critical("⚫ رسالة CRITICAL")
    
    print("\n✅ تم إنشاء السجلات في مجلد 'logs'")
