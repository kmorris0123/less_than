import os

less_than_five = []

def less_num_check(list_l):

	for item in list_l:
		item = int(item)
		if item < 5:
			less_than_five.append(item)
	print(less_than_five)

	return less_than_five




def main():
	playing = True
	while playing == True:
		print("")
		print("This will export a list of numbers that are less than 5.")
		print("")
		print("Type a list of numbers seprated by commas.")
		print("")
		print("Example: 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89")
		usr_list = str(input("--> "))

		useable_list = usr_list.replace(", ",",")
		useable_list = useable_list.split(",")
		less_num_check(useable_list)

		play_again = input('Do you want to play again? "Yes" or "No": ')

		if play_again == "yes":
			os.system('clear')

			playing = True

		else:
			print("Thanks for playing!")
			playing = False



if __name__ == '__main__':
  main()			








