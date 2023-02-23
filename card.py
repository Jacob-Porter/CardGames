height = 7
width = 7

def Layout(num, string):
    output = ''
    for h in range(0, height):
        if h == 0:
            output += '+-------+\n'
        elif h == height - 1:
            output += '+-------+'
            
        ## NUMBER first
        elif h == 1:
            if num <= 9:
                for w in range(0, width + 1):
                    if w == 0:
                        output += '|'
                    elif w == 1:
                        if num == 1:
                            output += 'A '
                        else:
                            output += str(num) + ' '
                    elif w == width:
                        output += '|\n'
                    else:
                        output += ' '
            else:
                for w in range(0, width + 1):
                    if w == 0:
                        output += '|'
                    elif w == 1:
                        if num == 11:
                            output += 'J '
                        elif num == 12:
                            output += 'Q '
                        elif num == 13:
                            output += 'K '
                        else:
                            output += str(num)
                    elif w == width:
                        output += '|\n'
                    else:
                        output += ' '
        ## NUMBER second
        elif h == 5:
            if num <= 9:
                for w in range(0, width + 1):
                    if w == 0:
                        output += '|'
                    elif w == width - 1:
                        if num == 1:
                            output += ' A'
                        else:
                            output += ' ' + str(num)
                    elif w == width:
                        output += '|\n'
                    else:
                        output += ' '
            else:
                for w in range(0, width + 1):
                    if w == 0:
                        output += '|'
                    elif w == width - 1:
                        if num == 11:
                            output += ' J|\n'
                            break
                        elif num == 12:
                            output += ' Q|\n'
                            break
                        elif num == 13:
                            output += ' K|\n'
                            break
                        else:
                            output += str(num)
                    elif w == width:
                        output += '|\n'
                    else:
                        output += ' '
                                        
        ## SUIT      
        elif h == 3:
            space = width - len(string)
            output += '|'
            if(space % 2 == 0):
                for i in range(int((space/2))):
                    output += ' '
                output += string
                for i in range(int((space/2))):
                    output += ' '
                output += '|\n'
            else:
                for i in range(int((space/2))):
                    output += ' '
                output += string
                for i in range(int((space/2)) + 1):
                    output += ' '
                output += '|\n'

        ## SPACE       
        else:
            output += '|'
            for w in range(width):
                output += ' '
            output += '|\n'
            
    return output ## end of Layout
                
class Card:

    def __init__(self, num, suit):
        self._num = num
        self._suit = suit
              
    def __str__(self):
        return Layout(self._num, self._suit)
    
    def GetNum(self):
        return self._num
    
    def GetSuit(self):
        return self._suit
        
        
        
        
# +-------+
# | 7     |
# |       |
# | Suit  |
# |       |
# |     7 |
# +-------+