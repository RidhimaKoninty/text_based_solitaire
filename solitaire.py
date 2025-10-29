git remote add origin https://github.com/RidhimaKoninty/text_based_solitaire.git
git branch -M main
git push -u origin main

import math, random
class Card:
    def __init__(self, suit, rank, faceUp=False):
        self.suit = suit
        self.rank = rank
        self.faceUp = faceUp
    
    def getColor(self):
        if self.suit == 'H' or self.suit == 'D':
            return "Red"
        else:
            return "Black"
    
    def returnCard(self):
        if(self.faceUp):
            return self.rank + self.suit
        else:
            return "XX"
    
    def cardValue(self):
        if(self.rank == "A"):
            return 1
        elif(self.rank == "2"):
            return 2
        elif(self.rank == "3"):
            return 3
        elif(self.rank == "4"):
            return 4
        elif(self.rank == "5"):
            return 5
        elif(self.rank == "6"):
            return 6
        elif(self.rank == "7"):
            return 7
        elif(self.rank == "8"):
            return 8
        elif(self.rank == "9"):
            return 9
        elif(self.rank == "10"):
            return 10
        elif(self.rank == "J"):
            return 11
        elif(self.rank == "Q"):
            return 12
        else:
            return 13
        

def createDeck():
    deck = []
    ranks = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']
    suits = ['H', 'C', 'D', 'S']
        
    for s in suits:
        for r in ranks:
            deck.append(Card(s,r))
    
    random.shuffle(deck)
    return deck
    
class Solitaire:
    def __init__(self):
        self.draw = []
        self.discard = []
        self.foundation = [[],[],[],[]]
        self.tableau =[[],[],[],[],[],[],[]]
    
    def newGame(self):
        deck = createDeck()
        i=0;
        while i < 7:
            if( i == 0):
                card = deck.pop(0);
                card.faceUp = True;
                self.tableau[0].append(card)
            if( i == 1):
                self.tableau[1].append(deck.pop(0))
                card = deck.pop(0);
                card.faceUp = True;
                self.tableau[1].append(card)
            if( i == 2):
                self.tableau[2].append(deck.pop(0))
                self.tableau[2].append(deck.pop(0))
                card = deck.pop(0);
                card.faceUp = True;
                self.tableau[2].append(card)
            if( i == 3):
                self.tableau[3].append(deck.pop(0))
                self.tableau[3].append(deck.pop(0))
                self.tableau[3].append(deck.pop(0))
                card = deck.pop(0);
                card.faceUp = True;
                self.tableau[3].append(card)
            if( i == 4):
                self.tableau[4].append(deck.pop(0))
                self.tableau[4].append(deck.pop(0))
                self.tableau[4].append(deck.pop(0))
                self.tableau[4].append(deck.pop(0))
                card = deck.pop(0);
                card.faceUp = True;
                self.tableau[4].append(card)
            if( i == 5):
                self.tableau[5].append(deck.pop(0))
                self.tableau[5].append(deck.pop(0))
                self.tableau[5].append(deck.pop(0))
                self.tableau[5].append(deck.pop(0))
                self.tableau[5].append(deck.pop(0))
                card = deck.pop(0);
                card.faceUp = True;
                self.tableau[5].append(card)
            elif(i==6):
                self.tableau[6].append(deck.pop(0))
                self.tableau[6].append(deck.pop(0))
                self.tableau[6].append(deck.pop(0))
                self.tableau[6].append(deck.pop(0))
                self.tableau[6].append(deck.pop(0))
                self.tableau[6].append(deck.pop(0))
                card = deck.pop(0);
                card.faceUp = True;
                self.tableau[6].append(card)
            i+=1
            self.draw = deck;
            
    def printGame(self):
        #cards left in draw pile
        print("---------------------------------------------------")
        print("\nDraw Pile: ", len(self.draw), " cards")
        
        #print discard iif discard not empty
        if len(self.discard) > 0:
            print("Discard:", self.discard[-1].returnCard())
        else:
            print("Discard: Empty")
        
        #Print top card of foundation if not empty
        print("\nFoundation:")
        suit = ['H', 'S', 'C', 'D']
        i = 0
        while i < 4:
            if len(self.foundation[i]) > 0:
                top = self.foundation[i][-1].returnCard()
                print(suit[i] + ":", top)
            else:
                print(suit[i] + ": Empty")
            i += 1
        
        #
        print("\nTableaus:")
        pileNum = 0
        while pileNum < 7:
            print(str(pileNum + 1) + ":", end=" ")#no new lien
            cardNum = 0
            while cardNum < len(self.tableau[pileNum]):
                print(self.tableau[pileNum][cardNum].returnCard(), end=" ")
                cardNum += 1
            print()#new line
            pileNum += 1
        print("\n")
    print("---------------------------------------------------")
    
    def drawCard(self):
        if len(self.draw)>0:
            card = self.draw.pop(0)
            card.faceUp=True
            self.discard.append(card)
        else:
            print("draw pile is empty")
    
    def discardToFoundation(self):
        if len(self.discard)>0:
            card = self.discard[-1]
            cardVal = card.cardValue()
            cardSuit = card.suit
            
            if(cardSuit == "H"):
                f = self.foundation[0]
            elif(cardSuit == 'C'):
                f = self.foundation[1]
            elif(cardSuit == 'D'):
                f = self.foundation[2]
            else:
                f = self.foundation[3]
            
            if(len(f)==0 and cardVal == 1):
                self.discard.pop()
                f.append(card)
                print(card.returnCard(), "moved to foundation ", cardSuit)
            elif len(f)>0 and cardVal == f[-1].cardValue()+1:
                self.discard.pop()
                f.append(card)
                print(card.returnCard(), "moved to foundation ", cardSuit)
            else:
                print("invalid move!")
        else:
            print("discard pile is empty")
            
   
    def discardToTableau(self, destination):
        destination-=1
        
        if len(self.discard)!=0:
            discard = self.discard.pop()
            if len(self.tableau[destination])> 0:
                dCard = self.tableau[destination][-1]
            
                if(dCard.getColor() != discard.getColor()) and (dCard.cardValue() == discard.cardValue()+1):
                    self.tableau[destination].append(discard)
                    print( "moved ", discard, " to pile", destination+1)
                else:
                    self.discard.append(discard)
                    print ("cards must alternate color and be lower value")
                    return 
            elif discard.cardValue()==13 and len(self.tableau[destination])==0:
                self.tableau[destination].append(discard)
                print( "moved ", discard.returnCard, " to pile", destination+1)
            else:
                self.discard.append(discard)
                print("only king can be moved to empty tableau")
                return "invalid"
        else:
            print("discard is empty")
            return
        
    def tableauToFoundation(self, tableauNum):
        if(len(self.tableau[tableauNum]) > 0):
            card = self.tableau[tableauNum].pop()
            cardVal = card.cardValue()
            cardSuit = card.suit
            
            if(cardSuit == "H"):
                f = self.foundation[0]
            elif(cardSuit == 'C'):
                f = self.foundation[1]
            elif(cardSuit == 'D'):
                f = self.foundation[2]
            else:
                f = self.foundation[3]
                
            if(len(f)==0 and cardVal == 1) or (len(f)>0 and cardVal == f[-1].cardValue()+1):
                f.append(card)
                print(card.returnCard(), "moved to foundation ", cardSuit)
                if(len(self.tableau[tableauNum])>0):
                    self.tableau[tableauNum][-1].faceUp=True
            else:
                self.tableau[tableauNum].append(card)
                print("invalid move!")
        else:
            print("selected tableau is empty")
    
    def tableauToTableau(self, source, numCards, destination):
        source-=1
        destination-=1
        
        #invalid moves
        if source < 0 or source > 6 or destination < 0 or destination > 6:
            print ("Invalid move")
            return "invalid"
        if len(self.tableau[source])==0:
            print ("empty source tableau")
            return "invalid"
        if numCards > len(self.tableau[source]):
            print("num cards exceed num cards in sorce tableau")
            return "invalid"
        
        select = self.tableau[source][-numCards:]
        if select[0].faceUp == False:
            print("face down cards cannot be moved")
            return "invalid"
        
        if len(self.tableau[destination])> 0:
            dCard = self.tableau[destination][-1]
            
            if( dCard.getColor() != select[0].getColor()) and (dCard.cardValue() == select[0].cardValue()+1):
                self.tableau[destination].extend(select)
                for i in range(numCards):
                    self.tableau[source].pop()
                if (len(self.tableau[source])>0):
                    self.tableau[source][-1].faceUp = True
                print( "moved ", numCards, " cards to pile", destination+1)
            else:
                print ("cards must alternate color and be lower value")
                return "invalid"
        else:
            if select[0].cardValue()==13:
                self.tableau[destination].extend(select)
                for i in range(numCards):
                    self.tableau[source].pop()
                if (len(self.tableau[source])>0):
                    self.tableau[source][-1].faceUp = True
                print( "moved ", numCards, " cards to pile", destination+1)
            else:
                print("only king can be moved to empty tableau")
                return "invalid"
                
                
        
    def flipCard(self, tableauNum):
        if(len(self.tableau[tableauNum])>0):
            self.tableau[tableauNum][-1].faceUp=True
        
    def resetDraw(self):
        if(len(self.draw)==0):
            while(len(self.discard)>0):
                card = self.discard.pop()
                card.faceUp= False
                self.draw.append(card)
            print("Recycled discard into draw pile")
        else:
            print("Draw Pile not empty, invalid move!")
    

    
game = Solitaire()
game.newGame()
def printCommands():
    print("""
commands:
    1. draw
    2. discard to foundation
    3. discard to tableau
    4. tableau to foundation
    5. tableau to tableau
    6. flip card
    7. reset draw pile
    8. help
    9. quit
    """)
    
printCommands()
game.printGame()
inPlay = True

while inPlay:
    command = input("enter a number command: ")
    
    if(command == "1"):
        game.drawCard()
    elif(command == "2"):
        game.discardToFoundation()
    elif(command == "3"):
        num = input("enter tableau number: ")
        if num.isdigit():
            if int(num)<8 and int(num)>0:
                game.discardToTableau(int(num))
        else:
            print("invalid tableau number")
    elif(command == "4"):
        num = input("enter tableau number: ")
        if num.isdigit():
            if int(num)<8 and int(num)>0:
                game.tableauToFoundation(int(num)-1)
        else:
            print("invalid tableau number")
    elif command == "5":
        source = input("source tableau pile(1-7): ")
        numCard = input("number of cards: ")
        destination = input("Destination tableau pile(1-7): ")
        if source.isdigit() and numCard.isdigit() and destination.isdigit():
            game.tableauToTableau(int(source), int(numCard), int(destination))
        else:
            print("invalid move")
    elif command == "6":
        num = input("tableau number: ")
        if num.isdigit():
            if int(num) >0 and int(num)<8: 
                game.flipCard(int(num)-1)
            else:
                print("invalid tableau number")
        else:
            print("invalid")
    elif command == "7":
        game.resetDraw()
    elif command == "8":
        printCommands()
    elif command == "9":
        print("game ended")
        inPlay = False
    else:
        print("invalid command")
    game.printGame()
