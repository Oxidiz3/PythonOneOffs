"""
Command Comprehender	
	summary: be able to get a command in a sentence and then understand what 
	it wants and do something with it
"""


from os import write

#File Names
verb_fileName = "verbs.txt"
object_fileName = "objects.txt"
adjective_filename = "adjectives.txt"
noun_fileName = "nouns.txt"
obj_indicator_fileName = "objIndicators.txt"
target_indicator_fileName = "targetIndicators.txt"
#Lists
verb_list = open(verb_fileName, mode= 'r').readlines()
object_list = open(object_fileName, mode= 'r').readlines()
adjective_list = open(adjective_filename, mode= 'r').readlines()
noun_list= open(noun_fileName, mode= 'r').readlines()
obj_indicator_list = open(obj_indicator_fileName).readlines()
target_indicator_list = open(target_indicator_fileName).readlines()

list_holder = [verb_list, object_list, adjective_list, noun_list,
               obj_indicator_list, target_indicator_list]

def InterpretList():
	#iterate through the lists and get rid of end characters
	for list in list_holder:
		i = 0
		for line in list:
			list[i] = line.rstrip()
			i+=1

def GetCommand():
	command = input("What is your command?\n").lower()
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
		elif word in object_list:
			print(word, "is an object!")
		elif word in noun_list:
			print(word, "is a noun!")
		elif word in adjective_list:
			print(word, "is an adjective!")
		elif word in obj_indicator_list:
			print(word, "is an object indicator!")
		elif word in target_indicator_list:
			print(word, "is a target indicator!")
		else:
			GetWordType(word)
		
def GetWordType(word):
	print("\no:object, n:noun, a:adjective, v:verb, 1: object indicator, 2: target indicator")
	wordType = input("What type of word is " + str(word) + "?\n").lower()
	
	#Get input then add new word to appropriate list
	if(wordType == 'o'):
		object_list.append(word)
		Write_To_File(object_fileName, word)
	elif(wordType == 'n'):
		noun_list.append(word)
		Write_To_File(noun_fileName, word)
	elif(wordType == 'a'):
		adjective_list.append(word)
		Write_To_File(adjective_filename, word)
	elif(wordType == 'v'):
		verb_list.append(word)
		Write_To_File(verb_fileName, word)
	elif(wordType == '1'):
		obj_indicator_list.append(word)
		Write_To_File(obj_indicator_fileName, word)
	elif(wordType == '2'):
		target_indicator_list.append(word)
		Write_To_File(target_indicator_fileName, word)
	else:
		print("I didn't recognize your input please use only o,n,a,v,1,2")
		GetWordType(word)

def Write_To_File(file_name, new_word):
	with open(file_name, mode = 'a') as open_file:
		open_file.write(new_word)

def __main__():
	InterpretList()
	GetCommand()

__main__()