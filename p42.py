def read_words(file):
    with open(file, 'r') as f:
        words = f.read().replace('"','').split(',')
    return words

def score(word):
    letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    score = 0
    for s in word.lower():
        score += letters.index(s) + 1
    return score   

if __name__ == "__main__":
    words = read_words("data/p42_words.txt")
    answer = 0
    triangle_numbers = set([k*(k+1)/2 for k in range(1,50)])  
    for word in words:
        if score(word) in triangle_numbers:
            answer += 1
    print(answer)