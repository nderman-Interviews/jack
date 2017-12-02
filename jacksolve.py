import urllib.request, json
import operator
from enum import Enum
from collections import defaultdict
with urllib.request.urlopen("https://s3-eu-west-1.amazonaws.com/yoco-testing/tests.json") as url:
    data = json.loads(url.read().decode())

class Suit(Enum):
     S = 4
     H = 3
     C = 2
     D = 1


tens = {'J','Q','K'}


# print(data)

def checkFaceCard(cardValue):
	if cardValue in tens:
		return 10
	elif cardValue == 'A':
		return 11
	else:
		return int(cardValue)

def sortCards(hand):
	cardlist = list()
	suitlist = list()
	for idx,card in enumerate(hand):
		cardlist.append(checkFaceCard(card[0:-1]))
		suitlist.append(card[-1:])
	cardListSorted = sorted(zip(cardlist,suitlist), reverse = True)
	# print(cardListSorted)
	return cardListSorted


def compareHands(playerAHand, playerBHand):

	sumA = 0
	sumB = 0

	for card,suit in playerAHand:
		sumA = sumA + card
	for card, suit in playerBHand:
		sumB = sumB + card

	if sumA > 21: #if A greater than 21 A loses
		return 0
	elif sumB > 21: #if B > 21 A wins
		return 1
	elif sumA > sumB: #if A>B A wins
		return 1
	elif sumB == sumA: #if equal we're not sure
		pass
	else:			#otherwise B wins
		return 0




	n = min(len(playerAHand),len(playerBHand))
	for i in range(n):
		if(playerAHand[i][0] > playerBHand[i][0]): #if a card is higher a wins
			return 1
		if(playerAHand[i][0] < playerBHand[i][0]): # if b card is higher b wins
			return 0
		if(Suit[playerAHand[i][1]].value > Suit[playerBHand[i][1]].value):
			return 1
		else:
		  	return 0

# loop through json results
for result in data:
	playerAHand = sortCards(result['playerA'])
	playerBHand = sortCards(result['playerB'])
	if compareHands(playerAHand, playerBHand) == result['playerAWins']:
		print('Correct')
		pass
	else:
		print ('Incorrect')
		print(compareHands(playerAHand, playerBHand))
		print (result)
		print(playerAHand)
		print(playerBHand)











