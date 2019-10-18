import random

class Card:
	def __init__(self, suit, value):
		self.suit = suit
		self.value = value

	def show(self):
		print("{} of {}".format(self.value, self.suit))


class Deck:
	def __init__(self):
		self.cards = []
		self.build()

	def build(self):
		for s in ["Spades", "Clubs", "Hearts", "Diamonds"]:
			for v in range(1, 14):
				self.cards.append(Card(s, v))

	def show(self):
		for c in self.cards:
			c.show()

	def shuffle(self):
		for i in range(len(self.cards) -1, 0, -1):
			r = random.randint(0, i)
			self.cards[i], self.cards[r] = self.cards[r], self.cards[i]

	def drawCard(self):
		return self.cards.pop()

class Player:
	def __init__(self, name):
		self.hand = []
		self.name = name
		self.team = 0
		self.score = 0

	def __str__(self):
		return self.name

	def draw(self, deck):
		self.hand.append(deck.drawCard())
		return self

	def drawHand(self):
		while len(self.hand) < 11:
			self.draw(deck)

	def showHand(self):
		for card in self.hand:
			card.show()

	def drawFromDiscard(self):
		self.hand.append(game.discard[-1])

	def playHand(self):
		print("\nWhich cards would you like to play? [Enter the numbers next to the listed cards, separated by a comma: \n")
		for a in self.hand:
			print(str(self.hand.index(a)) + ": " + ("{} of {}".format(a.value, a.suit))) 
		y = input("\nSelect the numbers next to the listed cards: \n")
		playList = [x.strip() for x in y.split(',')]
		for z in playList:
			print(z)

	@classmethod
	def from_input(cls):
		return cls(
			input('Name: ')
			)


class Canasta:
	def __init__(self):
		self.players = []
		self.turn = random.randint(0,3)
		self.deck = Deck()
		self.discard = []
		self.melded = False

	def startGame(self):
		self.deck.shuffle()
		self.addPlayers()
		self.dealHands()
		self.showPlayers()
		self.takeTurn()	

	def addPlayers(self):
		while len(self.players) < 4:
			newPlayer = Player.from_input()
			newPlayer.team = len(self.players) % 2
			self.players.append(newPlayer)

	def dealHands(self):
		for p in self.players:
			while len(p.hand) < 11:
				p.draw(self.deck)
		self.discard.append(self.deck.drawCard())


	def showPlayers(self):
		print("Here are your four players: \n")
		for p in self.players: 
			print(p.name)
			print(p.team)

	def showPlayerHands(self):
		for p in self.players:
			print(p.name + "'s hand:")
			p.showHand()

	def showCurrentPlayer(self):
		print(self.players[self.turn].name)
		self.players[self.turn].showHand()

	def takeTurn(self):
		p = self.players[self.turn]
		print("\nIt's " + p.name + "'s turn!\n")
		print("Here's your hand " + p.name + "!\n")
		p.showHand()
		discard = self.discard[-1]
		print("\nThe top card of the discard pile is the " + ("{} of {}".format(discard.value, discard.suit)) + "\n")
		print
		choice = ''
		while choice == '':
			choice = input("What would you like to do? [Press '1' for play, '2' for draw from the deck, '3' for draw from the discard]: \n")
			if choice == '1':
				if self.melded == False:
					print("\nYou need at least 30 points to meld\n")
					p.playHand()
				else:
					p.playHand()
			elif choice == '2':
				p.draw(self.deck)
				print("\nYour hand is now:\n")
				p.showHand()
			elif choice == '3':
				p.drawFromDiscard()
				print("\nYour hand is now:\n")
				p.showHand()
			else:
				print("\nPlease choose either '1', '2', or '3': \n")
				choice == ''

	def startGame(self):
		self.deck.shuffle()
		self.addPlayers()
		self.dealHands()
		self.showPlayers()
		self.takeTurn()			

#deck = Deck()
#deck.shuffle()

game = Canasta()
game.startGame()
#game.addPlayers()
#print("Here are your players: ")
#game.showPlayers()
#game.dealHands()
#game.showPlayerHands()
#game.showTurn()
#game.showCurrentPlayer()



# print("One card")
# card = Card("Hearts", 6)
# card.show()

# print("The deck")


# deck.show()

# print("Pick a card, any card (a number between 1 and 52, please")
# x = input()
# deck.cards[x-1].show()

# y = input("Would you like to shuffle the deck?")
# print(y)
# yes = ('yes', 'Yes', 'y', 'Y')


# if y in yes:
# 	deck.shuffle()
#	deck.show()
# else:
#	deck.show()

# deck.shuffle()
## card = deck.drawCard()
## card.show()

# bob = Player("Bob")
# bob.draw(deck)
# bob.drawHand()
# bob.showHand()


# print(game.turn)

