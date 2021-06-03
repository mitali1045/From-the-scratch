# -*- coding: utf-8 -*-
"""
Created on Tue May 25 11:42:11 2021

@author: Mitali.Tavildar
"""

"""
Problem : An arcade game player wants to climb to the top of the leaderboard and track their ranking. The game uses Dense Ranking, so its leaderboard works like this:
The player with the highest score is ranked number  on the leaderboard.
Players who have equal scores receive the same ranking number, and the next player(s) receive the immediately following ranking number.
"""

def ranks(ranked,players):
    unique_ranks = sorted(list(set(ranked)),reverse = True)
    ranks = {}
#    rankings = []
    answer = []

    player_ranks = []
    for score in players:
        while unique_ranks and score >= unique_ranks[-1]:
            unique_ranks.pop()
        answer.append(len(unique_ranks) + 1)

    return player_ranks
"""
    for i in range(0,len(unique_ranks)):
        ranks[unique_ranks[i]] = i+1
    #rankings = [ranks[ni] for ni in ranked] 
    for i in range(0,len(players)):
        if players[i] in (ranked):
            answer.append(ranks[players[i]])
        else:
            smallest = ranked[array(ranked) > players[i]].min()
            largest =  ranked[ranked > players[i]].max()
            if abs(players[i]-largest) > abs(players[i]-smallest):
                answer.append(ranks[smallest]) 
            else:
                answer.append(ranks[largest]+1)  
"""
"""
Third cut
    closest_nums = [min(ranked,key = lambda x : abs(x-i)) for i in players]
    closest_num_ranks = [ranks[r] for r in closest_nums]
    
    answer = [closest_num_ranks[i]+1 if closest_nums[i] > players[i] else closest_num_ranks[i] for i in range(0,len(players))]
    return answer
"""
"""
Second cut    
    for i in range(0,len(players)):
        if closest_nums[i] > players[i]:
            answer.append(closest_num_ranks[i]+1)
        else:
            answer.append(closest_num_ranks[i])
"""

"""
#First cut

    for i in players:
        closest_num_rank = ranks[min(ranked, key=lambda x:abs(x-i))]
        closest_num = min(ranked,key = lambda x : abs(x-i))
        #closest_num_idx = (np.abs(i-ranked)).argmin()
        if closest_num < i and closest_num_rank != 1:
            answer.append(closest_num_rank)
        elif closest_num < i and closest_num_rank == 1:
            answer.append(1)
        elif closest_num > i:
            answer.append(closest_num_rank+1)
        else:
            answer.append(closest_num_rank)
"""
            

ranked = [100 ,100, 50, 40, 40, 20, 10]
players = [5 ,25, 50, 120]

result = ranks(ranked,players)
