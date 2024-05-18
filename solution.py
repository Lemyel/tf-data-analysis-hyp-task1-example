import pandas as pd
import numpy as np


chat_id = 280785885 # Ваш chat ID, не меняйте название переменной

def solution(x_success: int, 
             x_cnt: int, 
             y_success: int, 
             y_cnt: int) -> bool:
    p1 = x_success / x_cnt
    p2 = y_success / y_cnt
    p_combined = (x_success + y_success) / (x_cnt + y_cnt)
    difference = p2 - p1
    z_value = difference / ((p_combined * (1 - p_combined) * (1/x_cnt + 1/y_cnt)) ** 0.5)
    z_critical = 1.96
    
    return z_value > z_critical
