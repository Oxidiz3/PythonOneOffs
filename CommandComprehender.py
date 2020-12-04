"""
Command Comprehender	
	summary: be able to get a command in a sentence and then understand what 
	it wants and do something
	with it
"""


verb_list = open("Verbs.txt", mode='r').readlines()
object_list = []
adjective_list = []
noun_list = []

def InterpretLists():
	i = 0
	for line in verb_list:
		verb_list[i] = line.rstrip()
		i+=1

def GetCommand():
	command = input("What is your command?\n")
	DisectCommand(command)

def DisectCommand(command):
	wordList = []
	startNum = 0
	endNum = 0
	for word in command:
		# If there is a space then that is one word
		if(word == " "):
			wordList.append(command[startNum:endNum])

			#Move the start num to the letter after the space
			startNum = endNum+1
		endNum += 1
		
	#No space at the end of the file so add that as a word also
	wordList.append(command[startNum:endNum])
	DetermineWordType(wordList)
		

def DetermineWordType(wordList):
	for word in wordList:
		if word in verb_list:
			print(word, "is a verb!")
		else:
			GetWordType(word)
		
def GetWordType(word):
	print("\no:object, n:noun, a:adjective, v:verb")
	wordType = input("What type of word is " + str(word)).lower()
	
	if(wordType == 'o'):
		object_list.append(word)
	elif(wordType == 'n'):
		noun_list.append(word)
	elif(wordType == 'a'):
		adjective_list.append(word)
	elif(wordType == 'v'):
		verb_list.append(word)
	else:
		print("I didnt recognize your input please use only o,n,a,v")
		GetWordType(word)


def main():
	InterpretLists()
	GetCommand()

main()