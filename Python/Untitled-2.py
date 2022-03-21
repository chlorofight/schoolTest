
alphabet = 'abcdefghijklmnopqrstuvwxyz'
newMessage = ''

message = input('Please enter a message')

def main()
key = 1

for character in message:
  if character in alphabet:
    position = alphabet.find(character)
    newPost = (position + key) % 26
    newChar = alphabet[newPost]
    #print (newChar)
    newMessage += newChar
  else:
    newMessage += character

print(newMessage)
key + 1
main()
if key = 27 break