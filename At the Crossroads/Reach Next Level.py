# Reach Next Level
'''
You are playing an RPG game. Currently your experience points (XP) total is equal to experience. 
To reach the next level your XP should be at least at threshold. If you kill the monster in front of you, 
you will gain more experience points in the amount of the reward.

Given values experience, threshold and reward, check if you reach the next level after killing the monster.
'''

# Example
'''
For experience = 10, threshold = 15, and reward = 5, 
the output should be solution(experience, threshold, reward) = true;

For experience = 10, threshold = 15, and reward = 4, 
the output should be solution(experience, threshold, reward) = false.
'''

# Solution:

def solution(experience, threshold, reward):
    return True if experience + reward >= threshold else False

experience = 10
threshold = 15
reward = 5
print(solution(experience, threshold, reward))

experience = 10
threshold = 15
reward = 4
print(solution(experience, threshold, reward))