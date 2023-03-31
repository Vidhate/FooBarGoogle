# Given an array xs of integers, find the maximum possible product of any chosen subset of the array

def solution(xs):
    
    if len(xs)==1:
        return str(xs[0])

    positive_power = [x for x in xs if x>0]
    negative_power = sorted([x for x in xs if x<0], reverse=True)

    if len(negative_power)==1 and len(positive_power)==0:
        return '0'
    
    max_power = 1
    for power in positive_power:
        max_power*=power

    negative_panels = len(negative_power)
    while negative_panels>1:
        max_power*=(negative_power[negative_panels-1]*negative_power[negative_panels-2])
        negative_panels-=2

    return str(max_power)