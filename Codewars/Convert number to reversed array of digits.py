#failed this one, used solution from codewars.com

def digitize(n):
    return map(int, str(n)[::-1])
print(list(digitize(700)))