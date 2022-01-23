with open("sgb-words.txt") as f:
	content = f.read().split("\n")[:~0]

contains = []
places = []
not_pos = []
place_chs = []
guess = "null"

while guess != "":
	guess = input("Guess: ")
	if guess == "":
		break
	cnt = input("Contains: ")
	place = input("Place: ")

	contains += list(cnt) 
	place_temp = [[list(place)[i],int(list(place)[i+1])] for i in range(0,len(list(place)),2)]
	places += place_temp
	for ch in place_temp:
		if ch[0] not in place_chs:
			place_chs.append(ch[0])
	for ch in guess:
		if ch not in contains and ch not in place_chs:
			not_pos.append(ch)
	
	pos = []

	for word in content:
		leave = False
		for ch in contains:
			if ch not in word:
				leave = True
				break
		if leave:
			continue
		for ch in places:
			if ch[0] != word[ch[1]-1]:
				leave = True
				break
		for ch in not_pos:
			if ch in word:
				leave = True
				break
		if leave:
			continue
		pos.append(word)
	
	for word in pos:
		print(word)
	content = pos
