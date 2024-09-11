# -*- coding: utf-8 -*-
"""
Created on Fri May 24 14:19:51 2024

@author: USNA0501
"""

import datetime

def get_current_time_percentage():
    now = datetime.datetime.now()
    midnight = datetime.datetime.combine(now.date(), datetime.time())
    seconds_passed = (now - midnight).seconds
    total_seconds_in_day = 24 * 60 * 60
    percentage = (seconds_passed / total_seconds_in_day) * 100
    return percentage

def generate_loading_bar(percentage, length=50):
    filled_length = int(length * percentage // 100)
    bar = '█' * filled_length + '-' * (length - filled_length)
    return f"[{bar}] {percentage:.2f}%"

if __name__ == "__main__":
    percentage = get_current_time_percentage()
    loading_bar = generate_loading_bar(percentage)
    print(loading_bar)
