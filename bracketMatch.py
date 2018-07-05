

def bracketMatch(text):

    counter = 0
    ans = 0
    for i in range(len(text)):
        if text[i] == '(':
            counter += 1
        if text[i] == ')':
            counter -= 1
        if counter < 0:
            counter += 1
            ans +=1
    return ans + counter


test="(()"
print(bracketMatch(test))

test = "(())"
print(bracketMatch(test))

test = "())("
print(bracketMatch(test))

test = "()))("
print(bracketMatch(test))

