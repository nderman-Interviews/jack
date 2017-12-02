import urllib.request, json
import operator
with urllib.request.urlopen("https://s3-eu-west-1.amazonaws.com/yoco-testing/tests.json") as url:
    data = json.loads(url.read().decode())


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
	cardlist = {}
	for idx, card in enumerate(hand):
		cardlist[card[-1:]] = checkFaceCard(card[0:-1])
	cardListSorted = sorted(cardlist.items(), key=operator.itemgetter(1), reverse = True)
	return cardListSorted

def compareHands(playerAHand, playerBHand):

	sumA = 0
	sumB = 0

	for card in playerAHand:
		sumA = sumA + card[1]
	for card in playerBHand:
		sumB = sumB + card[1]

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
		if(playerAHand[i][1] > playerBHand[i][1]): #if a card is higher a wins
			return 1
		if(playerAHand[i][1] < playerBHand[i][1]): # if b card is higher b wins
			return 0

	#finally compare suits
	print(playerAHand)
	print(playerBHand)
	print('****')

# loop through json results
for result in data:
	playerAHand = sortCards(result['playerA'])
	playerBHand = sortCards(result['playerB'])
	compareHands(playerAHand, playerBHand)









