from random import randint
import sys, os

def roll(num):
	res = list()

	for x in range(num):
		res.append(randint(1,6))
	return res

def result(atck,dfnd):
	score = "attacking: "+str(atck)+"\tdefending: "+str(dfnd)
	if dfnd > 0 and atck <= 1:
		print("\n\ndefenders win\n\t"+score)
		return "finished"
	elif atck > 1 and dfnd <= 0:
		print("\n\nattackers win\n\t"+score)
		return "finished"
	else:
		print(score)
		return(atck,dfnd)

def fight(atck, dfnd):
	if atck <= 1 or dfnd <= 0:
		return result(atck,dfnd)

	atck_avail = atck - 0
	dfnd_avail = dfnd if dfnd <= 2 else 2

	atck_rolls = roll(atck_avail)
	dfnd_rolls = roll(dfnd_avail)

	for i in range(min([atck_avail, dfnd_avail])): 
		if atck_rolls[i] > dfnd_rolls[i]:
			atck -= 1
		else:
			dfnd -= 1

	return result(atck, dfnd)

def get_int_input(message):
	try:
		return int(input(message))
	except:
		return get_int_input(message)

def fight_all_helper(atck, dfnd):
	f = fight(atck, dfnd)
	if f == 'finished':
		return
	else:
		fight_all_helper(f[0], f[1])


def fight_all(atck, dfnd):
	print("Starting game\n\nScores:")
	res = result(atck, dfnd)
	print()
	fight_all_helper(atck, dfnd)


def callback_helper(score):
	cmd = input("\nwould you like to fight again? ")
	if cmd == 'fight all':
		fight_all(score[0], score[1])
	elif cmd == 'n':
		return
	elif cmd == 'y' or cmd == '':
		fight_callback(score[0], score[1])
	elif cmd == 'clear':
		os.system('clear')
		result(score[0], score[1])
		callback_helper(score)
	else:
		callback_helper(score)

def fight_callback(atck,dfnd):
	score = fight(atck, dfnd)
	print()
	if score == 'finished':
		return

	callback_helper(score)
	

def await_response():


	cmd = input("\n\nType a command:\n--------------\n")

	if cmd == 'clear':
		os.system('clear')
		await_response()
		return

	if cmd == 'help':
		print_help()
		await_response()
	elif cmd == 'fight all':
		print("--------------\npreparing to fight to the death, enter team size.")
		atck = get_int_input("Number of attackers: ")
		dfnd = get_int_input("Number of defenders: ")
		fight_all(atck, dfnd)
		await_response()
	elif cmd == 'fight':
		print("--------------\npreparing to fight, enter team size.")
		atck = get_int_input("Number of attackers: ")
		dfnd = get_int_input("Number of defenders: ")
		print("fight help:\n\ty: fight again\n\tn: finish")
		fight_callback(atck, dfnd)
		await_response()
	elif cmd == 'exit':
		print("\n\nGood game!")
		return
	else:
		print("invalid response: "+cmd)
		print_help()
		await_response()

def print_help():
	print("\nOptions:")
	print("\thelp: display these options")
	print("\tfight all: fight until one army can no longer fight")
	print("\tfight: get the result of one fight")
	print("\texit: leave the command line interface")
	print("\tclear: clear the terminal")	


if __name__ == '__main__':
	print("Welcome to Risk!")
	print_help()
	await_response()















