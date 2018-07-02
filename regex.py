import string

def is_match(text, pattern):
  return isMatchHelper(text, pattern, 0, 0)


def isMatchHelper(text, pattern, textIndex, patIndex):
    # base cases - one of the indexes reached the end of text or pattern
    if (textIndex >= len(text)):
        if (patIndex >= len(pattern)):
            return True
        else:
            if (patIndex+1 < len(pattern)) and  (pattern[patIndex+1] == '*'):
                return isMatchHelper(text, pattern, textIndex, patIndex + 2)
            else:
                return False

    elif (patIndex >= len(pattern)) and (textIndex < len(text)):
        return False

      #string matching for character followed by '*'
    elif (patIndex+1 < len(pattern)) and (pattern[patIndex+1] == '*'):
        if (pattern[patIndex] == '.') or (text[textIndex] == pattern[patIndex]):
            return (isMatchHelper(text, pattern, textIndex, patIndex + 2) or
                    isMatchHelper(text, pattern, textIndex + 1, patIndex))
        else:
            return isMatchHelper(text, pattern, textIndex, patIndex + 2)

    # string matching for '.' or ordinary char.
    elif (pattern[patIndex] == '.') or (pattern[patIndex] == text[textIndex]):
        return  isMatchHelper(text, pattern, textIndex + 1, patIndex + 1)
    else:
        return False

        
