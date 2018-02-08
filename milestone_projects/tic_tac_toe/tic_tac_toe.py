player_one = {}
player_two = {}
EMPTY_ROW = [' ', ' ', ' ']
board = {'1': EMPTY_ROW, '2': EMPTY_ROW, '3': EMPTY_ROW}

def welcome():
	print 'Welcome to Tic Tac Toe!'

def determine_player_names():
	global player_one, player_two
	player_one_name = raw_input('Please enter the name of player one: ')
	player_two_name = raw_input('Please enter the name of player two: ')
	player_one = {'name': player_one_name, 'symbol': 'X'}
	player_two = {'name': player_two_name, 'symbol': 'O'}

def render_board():
	global board
	# print board
	LINE = '-----'
	print ('{0}|{1}|{2}').format(board['1'][0], board['1'][1], board['1'][2])
	print LINE
	print ('{0}|{1}|{2}').format(board['2'][0], board['2'][1], board['2'][2])
	print LINE
	print ('{0}|{1}|{2}').format(board['3'][0], board['3'][1], board['3'][2])

def take_turn(player):
	global board
	choice = raw_input('Please enter the coordinates of the board you want\n\tFormatted like 1,2: ')
	final_choices = choice.split(',')
	print board
	row_choice = final_choices[0]
	row_to_update = board[row_choice]
	row_to_update[int(final_choices[1]) - 1] = player['symbol']
	print row_to_update
	print board[row_choice]
	# board[row_choice] = row_to_update
	print board

def play():
	global player_one, player_two
	welcome()
	determine_player_names()
	render_board()
	current_player = player_one
	take_turn(current_player)
	render_board()

play()