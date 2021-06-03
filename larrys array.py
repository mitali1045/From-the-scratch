# -*- coding: utf-8 -*-
"""
Created on Wed Jun  2 12:31:12 2021

@author: Mitali.Tavildar
"""

def larrysArray(A):         
    def stat_val(A_val):
        stat = []
        for i in range(0,len(A_val)):
            if A_val[i] == position_dict[A_val.index(A_val[i])]:
                stat.append("Correct")
            else:
                stat.append("rearrange")
        return stat
           
    def rearrange(combo,required_position):
        combo[0],combo[1],combo[2] = combo[1],combo[2],combo[0]
        if sorted(combo) == combo or combo[0] == position_dict[required_position] or combo[0] == min(combo):
            return combo
        else:
            combo = rearrange(combo,required_position)
            return combo
    
    def rearrange_call(A_val):  
        stat = stat_val(A_val)    
        for i in range(0,len(stat)-2):
            if stat[i] == "rearrange":
                required_position = i
                combo = [A_val[i+x] for x in range(0,3)]
                positions = [i+x for x in range(0,3)]
                rearranged_combo = rearrange(combo,required_position)
                for i,val in zip(positions,rearranged_combo):
                    A_val[i] = val
        return A_val

    executed = 0
    max_A = max(A)
    position_dict = {}
    for i in range(0,max_A+1):
        position_dict[i] = i+1
        
    while(executed != len(A)):
        A_val = A
        A_val = rearrange_call(A_val)
        executed += 1
    if A == sorted(A):
        return "YES"
        
    else:
        return "NO"
           
    
A = [1,2,3,5,4]
final_val = larrysArray(A)

"""    
    def check_position(val):
        if val == position_dict[A_val.index(val)]:
            return "Correct"
        else:
            return "rearrange"
"""  