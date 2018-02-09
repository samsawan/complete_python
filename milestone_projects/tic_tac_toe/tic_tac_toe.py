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
	LINE = '  -----'
	print '  0 1 2'
	print('0 {0}|{1}|{2}').format(board[0][0], board[0][1], board[0][2])
	print LINE
	print('1 {0}|{1}|{2}').format(board[1][0], board[1][1], board[1][2])
	print LINE
	print('2 {0}|{1}|{2}').format(board[2][0], board[2][1], board[2][2])

def take_turn(player):
	prompt = '{0}, please enter the coordinates of the cell you want\n\tFormatted like 0,1: '.format(player['name'])
	choice = raw_input(prompt)
	valid_input, info = parse_input(choice)
	if valid_input:
		row_input, column_input = info
		enter_choice(row_input, column_input, player)
	else:
		print info
		take_turn(player)


def enter_choice(row_input, column_input, player):
	global board
	if cell_empty(row_input, column_input):
		board[row_input][column_input] = player['symbol']
	else:
		print('\tPlease select an empty cell!\n')
		take_turn(player)


def cell_empty(row_input, column_input):
	return board[row_input][column_input] == ' '


def change_player(player):
	return player_two if player == player_one else player_one


def parse_input(choice):
	row_input, column_input = map(lambda choice: int(choice), choice.split(','))
	acceptable_range = range(0, 3)
	if(row_input in acceptable_range and column_input in acceptable_range):
		return True, [row_input, column_input]
	else:
		return False, '\tThe row input and column input must be a number within 0 and 2!'


def winner_check():
	return not (row_check() and diagonal_check() and column_check())


def row_check():
	check = True;
	for row in board:
		key = row[0]
		if key != ' ' and check:
			check = not (row[0] == row[1] and row[0] == row[2])
	return check


def diagonal_check():
	middle = board[1][1]
	first_diagonal = (middle == board[0][0] and middle == board[2][2])
	second_diagonal = (middle == board[0][2] and middle == board[2][0])
	return not (middle != ' ' and (first_diagonal or second_diagonal))


def column_check():
	return check_column(0) and check_column(1) and check_column(2)


def check_column(position):
	key = board[0][position]
	return not (key != ' ' and (key == board[1][position] and key == board[2][position]))


def declare_winner(player):
	print('{0} is the winner! Congratulations!').format(player['name'])


def determine_tie():
	tie = False
	for row in board:
		for cell in row:
			if cell == ' ':
				tie = True
	return not tie

def play_board():
	current_player = player_two
	winner = False
	tie_game = False
	while not winner and not tie_game:
		current_player = change_player(current_player)
		take_turn(current_player)
		tie_game = determine_tie()
		winner = winner_check()
		render_board()
	return tie_game, winner, current_player


def play():
	welcome()
	determine_player_names()
	render_board()
	is_tie_game, winner_determined, final_player = play_board()

	if winner_determined:
		declare_winner(final_player)
	elif is_tie_game:
		print('\nA tie game!')

play()
