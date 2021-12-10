from types import coroutine

test_data = "Day_10/testinput.txt"
real_data = "Day_10/input.txt"

file = real_data
lines = open(file, "r").read().splitlines()


matching_bracket = {'(' : ')', '[' : ']', '{' : '}', '<' : '>'}
closing = {')' , ']' , '}', '>'}

syntax_scores = { ')' : 3, ']' : 57, '}' : 1197, '>' : 25137 }
syntax_score = 0

completetion_scores = {')' : 1, ']' : 2, '}' : 3, '>' : 4 }
completetion_score = []

def compare(char_pop :str, char_last:str) -> bool:
    if matching_bracket[char_pop] == char_last:
        return True
    else:
        return False

def workout_score(left_over_brackets : list) -> int:
    score = 0
    for _ in range(len(left_over_brackets)):
        bracket = matching_bracket[left_over_brackets.pop()]
        score = score*5
        score += completetion_scores[bracket]
    completetion_score.append(score)


for line in lines:
    stack = []
    corrupted = False
    for char in line:
        if char in closing:
            if compare(stack.pop(), char):
                continue
            else:
                corrupted = True
                syntax_score += syntax_scores[char] 
        else:
            stack.append(char)
    if not corrupted : workout_score(stack)
        

print(f"Part 1: {syntax_score}")
print(f"Part 2: {sorted(completetion_score)[int(((len(completetion_score)+1)/2)-1)]}")


