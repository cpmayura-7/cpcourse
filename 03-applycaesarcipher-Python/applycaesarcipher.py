# A Caesar Cipher is a simple cipher that works by shifting each letter in 
# the given message by a certain number. For example, if we shift the message 
# "We Attack At Dawn" by 1 letter, it becomes "Xf Buubdl Bu Ebxo"
# Write the function applyCaesarCipher(message, shift) which shifts the given 
# message by shift letters. You are guaranteed that message is a string, and 
# that shift is an integer between -25 and 25. Capital letters should stay capital 
# and lowercase letters should stay lowercase, and non-letter characters should not be changed. 
# Note that "Z" wraps around to "A". So, for example:
# assert(applyCaesarCipher("We Attack At Dawn", 1) == "Xf Buubdl Bu Ebxo")
# assert(applyCaesarCipher("zodiac", -2) == "xmbgya")


def fun_applycaesarcipher(msg, shift):
	li=[]
	msg1=msg.split(" ")
	#print(msg1)
	for i in msg1:
		result=""
		for char in i:
			if (char.isupper()):
				result += chr((ord(char) + shift-65) % 26 + 65)
			else:
				result += chr((ord(char) + shift - 97) % 26 + 97)
		li.append(result)
	#print(li)
	st1=""
	if(len(li)>1):
		for i in li:
			st1+=str(i)+" "
		return st1
	else:
		return li[0]




