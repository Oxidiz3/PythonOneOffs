import keyboard as kb

myRecordedDic = {}
recordedMacro = []

def RecordMacro():
	recordedMacro = kb.record(until='esc')
	return recordedMacro

def PlayMacro(recordKey):
	kb.play(myRecordedDic[recordKey], speed_factor=0)

def GetInput():
	keyPressed = kb.read_key(True)
	print(keyPressed)
	if keyPressed == 'r':
		print('pressed r')
		recordKey = kb.read_key()
		#add record macro to dictionary under record key
		myRecordedDic[recordKey] =  RecordMacro()
	elif keyPressed == 'p':
		print('pressed p')
		recordKey = kb.read_key()
		PlayMacro(recordKey)

while True:
	if kb.is_pressed('q'):
		print('1 time through')
		GetInput()

