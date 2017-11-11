import random


# 最開始先產生六顆骰子
def gen_dices():
	dices = [] # 空清單
	for i in range(6): # 做六次
		x = random.randint(1, 6) # 產生1~6的隨機數字
		dices.append(x) # 加到dices清單中
	print('目前骰子是:', dices)
	return dices

# 印出使用方法
def print_usage(): 
	print('請輸入功能')
	print('s: 洗牌')
	print('q: 結束')
	print('1: 大的拿掉')
	print('2: 小的拿掉')
	print('3: 紅的拿掉')
	print('4: 黑的拿掉')
	print('5: 單的拿掉')
	print('6: 雙的拿掉')


def shuffle(dices):
	len_dices = len(dices) # 我們目前有幾棵
	dices = [] # 目前骰子變成空清單
	for i in range(len_dices): 
		x = random.randint(1, 6) # 產生1~6的隨機數
		dices.append(x) # 加進dices清單中
	return dices


def remove_big(dices):
	new_list = []  # 先建立一個新的清單
	for num in dices: # 目前的骰子中的每一個數字
		if num <= 3: # 如果小於等於3
			new_list.append(num) # 就加到新的清單中
	dices = new_list # 把現在持有的骰子變成 新的這個清單(new_list)
	return dices


def remove_small(dices):
	new_list = []
	for dice in dices:
		if dice >= 4:
			new_list.append(dice)
	dices = new_list
	return dices


def remove_red(dices):
	red = [1, 4]
	new_list = []
	for dice in dices:
		if dice not in red:
			new_list.append(dice)
	dices = new_list
	return dices


def remove_black(dices):
	red = [1, 4]
	new_list = []
	for dice in dices:
		if dice in red:
			new_list.append(dice)
	dices = new_list
	return dices


def remove_odd(dices):
	new_list = []
	for dice in dices:
		if dice % 2 == 0:
			new_list.append(dice)
	dices = new_list
	return dices


def remove_even(dices):
	new_list = []
	for dice in dices:
		if dice % 2 == 1:
			new_list.append(dice)
	dices = new_list
	return dices


def play(dices):
	# 開始讓使用者輸入模式
	while True:
		mode = input('請輸入模式: ')
		if mode == 'q': # q 表示quit (離開)
			break
		elif mode == 's': # 如果輸入s則洗牌 (shuffle)
			dices = shuffle(dices)
		elif mode == '1': # 功能一是把持有的骰子淘汰掉大於3的數字
			dices = remove_big(dices)
		elif mode == '2': # 小的拿掉
			dices = remove_small(dices)
		elif mode == '3': # 紅的拿掉
			dices = remove_red(dices)
		elif mode == '4': # 黑的拿掉
			dices = remove_black(dices)
		elif mode == '5': # 單的拿掉
			dices = remove_odd(dices)
		elif mode == '6':
			dices = remove_even(dices)

		print(dices) # 把現在的骰子印出來


def main():
	dices = gen_dices()
	print_usage()
	play(dices)


main()