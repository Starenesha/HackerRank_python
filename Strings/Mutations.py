#https://www.hackerrank.com/challenges/python-mutations/problem?h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen

def mutate_string(string, position, character):
    string1 = list(string)
    string1[position] = character
    return "".join(string1)
