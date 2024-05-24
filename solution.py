import pandas as pd
import numpy as np

chat_id = 280785885 # Ваш chat ID, не меняйте название переменной

def solution(x_success: int, x_cnt: int, y_success: int, y_cnt: int) -> bool:
    # Рассчитываем доли успеха
    p1 = x_success / x_cnt
    p2 = y_success / y_cnt
    
    # Рассчитываем объединенную долю успеха
    p = (x_success + y_success) / (x_cnt + y_cnt)
    
    # Рассчитываем стандартную ошибку
    se = np.sqrt(p * (1 - p) * (1 / x_cnt + 1 / y_cnt))
    
    # Рассчитываем z-значение
    z = (p1 - p2) / se
    
    # Определяем критическое значение для уровня значимости 0.01
    z_critical = np.abs(np.percentile(np.random.normal(0, 1, 1000000), 99.5)) # Для двустороннего теста

    # Проверяем, превышает ли z-значение критическое значение
    return abs(z) > z_critical

