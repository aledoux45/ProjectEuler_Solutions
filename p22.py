def score(name):
    letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    score_letters = {c:s+1 for s, c in enumerate(letters)}
    score = 0
    for c in str(name).lower():
        score += score_letters[c]
    return score    
        
def read_names(file):
    names = []
    for line in open(file):
        names += line.strip().replace('"','').split(',')
    names.sort()
    return names

if __name__ == "__main__":
    names = read_names("data/p22_names.txt")
    answer = 0
    for i, name in enumerate(names):
        answer += score(name) * (i+1)
    print(answer)