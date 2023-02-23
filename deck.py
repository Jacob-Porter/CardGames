import random
import card as _card

cardSuits = ['Club', 'Spade', 'Diamond', 'Heart']
cardNums = 13
            
def Display(obj):
    output = ''
    for i in range(len(obj)):
        output += (str(obj[i]))
    return output

def CreateDeck(obj):
    for suitNum in range(len(cardSuits)):
            for num in range(cardNums):
                temp = _card.Card(num + 1, cardSuits[suitNum])
                obj.append(temp)

class Deck:
        
    def __init__(self, deck):
        self._deck = deck
        CreateDeck(self._deck)
            
    def __str__(self):
        return Display(self._deck)

    def Shuffle(self):
        self._deck = []
        CreateDeck(self._deck)
        for i in range(len(self._deck)):
            randomNum = random.randint(0, len(self._deck) - 1)
            temp1 = self._deck[randomNum]
            temp2 = self._deck[i]   
            self._deck[i] = temp1
            self._deck[randomNum] = temp2
    
    def Draw(self):
        val = self._deck[0].GetNum()
        self._deck.pop(0)
        return val
    
    def PrintCard(self, index):
        print(self._deck[index])

    
    def Add(self, card):
        self._deck.append(card)
        
    def Size(self):
        return len(self._deck)
    
    def GetCard(self, index):
        return self._deck[index]



     