player_one = {}
player_two = {}
board = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]

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
	print('{0}|{1}|{2}').format(board[0][0], board[0][1], board[0][2])
	print LINE
	print('{0}|{1}|{2}').format(board[1][0], board[1][1], board[1][2])
	print LINE
	print('{0}|{1}|{2}').format(board[2][0], board[2][1], board[2][2])

def take_turn(player):
	global board
	choice = raw_input('Please enter the coordinates of the board you want\n\tFormatted like 0,1: ')
	row_input, column_input = map(lambda choice: int(choice), choice.split(','))
	board[row_input][column_input] = player['symbol']


def play():
	global player_one, player_two
	welcome()
	determine_player_names()
	render_board()
	current_player = player_one
	take_turn(current_player)
	render_board()

play()
