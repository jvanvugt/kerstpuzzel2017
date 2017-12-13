values = {
    'a': 188461,
    'b': 565383,
    'd': 686149,
    'e': 88447,
    'g': 265341,
    'h': 796023,
    'i': 388069,
    'l': 164207,
    'n': 492621,
    'o': 477863,
    's': 433589,
    't': 300767,
    'u': 902301,}
    
letters = list(values)
    
    
def solve(i, left, word=''):
    if left < 0:
        return
    if left == 0:
        print(word)
        return
    if i == len(letters):
        return
    solve(i, left - values[letters[i]], word+letters[i])
    solve(i+1, left, word)
    

nums = [696318, 994738, 186634, 937474, 818450, 387210, 184092, 377231, 999091, 293830, 725605, 893049, 394922]
for num in nums:
    solve(0, num)
    print('--------------')
    