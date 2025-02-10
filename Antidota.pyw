import os
import time
from datetime import datetime, timedelta
import logging
import sys

# Настройка логирования
logging.basicConfig(filename='block_dota.log', level=logging.INFO,
                    format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S')

def is_weekend():
    today = datetime.today().weekday()
    return today in [4, 5, 6]

def block_dota():
    last_check_time = datetime.now()
    is_weekend_cache = is_weekend()
    check_interval = timedelta(minutes=30)  # Проверяем каждые 30 минут

    while True:
        try:
            current_time = datetime.now()
            
            # Проверяем, прошло ли достаточно времени с последней проверки
            if current_time - last_check_time >= check_interval:
                is_weekend_cache = is_weekend()
                last_check_time = current_time
                logging.info("Выполнена регулярная проверка дня недели.")

            if not is_weekend_cache:
                os.system("taskkill /f /im dota2.exe > nul 2>&1")
                logging.info("Доступ к Dota 2 заблокирован.")
            
            time.sleep(60)  # Проверяем каждую минуту
        except Exception as e:
            logging.error(f"Произошла ошибка: {str(e)}")
            time.sleep(60)

if __name__ == "__main__":
    try:
        block_dota()
    except KeyboardInterrupt:
        logging.info("Программа остановлена пользователем.")
        sys.exit(0)