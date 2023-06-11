#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list == 0:
        return 0
    total_score = 0
    total_weight = 0
    for score, weight in my_list:
        total_score += score * weight
        total_weight += weight
    if total_weight == 0:
        return 0
    average_weight = total_score / total_weight
    return average_weight
