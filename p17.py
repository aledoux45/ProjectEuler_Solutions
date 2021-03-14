def number_to_engligh(n):
    n1to20 = ["one","two","three","four","five","six","seven","eight","nine","ten", \
        "eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen","eighteen","nineteen"]
    n10to90 = ["twenty","thirty","forty","fifty","sixty","seventy","eighty","ninety"]
    dictionary = {k:n1to20[k-1] for k in range(1,20)}
    dictionary.update({k:n10to90[i] for i, k in enumerate(range(20,91,10))})
    dictionary[1000] = "one thousand"
    number = ""
    if n in dictionary:
        number = dictionary[n]
        return number
    # hundreds
    hundreds = n // 100
    if hundreds > 0:
        number += dictionary[hundreds] + " hundred"
    # tens
    after_hundred = n - hundreds*100
    if after_hundred in dictionary:
        if hundreds > 0:
            number += " and "
        number += dictionary[after_hundred]
        return number
    tens = (n - hundreds*100) // 10
    if tens > 0:
        if hundreds > 0:
            number += " and "
        number += dictionary[tens * 10]
    # units
    units = (n - hundreds*100 - tens*10)
    if units > 0:
        if hundreds > 0 and tens == 0:
            number += " and "
        if tens > 0:
            number += "-"
        number += dictionary[units]
    return number

if __name__ == "__main__":
    total = 0
    for n in range(1,1001):
        number = number_to_engligh(n)
        total += len(number.replace(" ","").replace("-",""))
        
    print(total)