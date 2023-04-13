import pandas as pd
import numpy as np
from statsmodels.stats.proportion import proportions_ztest


chat_id = 539377624

def solution(x_success: int, 
             x_cnt: int, 
             y_success: int, 
             y_cnt: int) -> bool:
    alpha = 0.03
    stat, pval = proportions_ztest([x_success, y_success], [x_cnt, y_cnt], alternative='two-sided')
    if pval < alpha:
        return True
    else: return False
