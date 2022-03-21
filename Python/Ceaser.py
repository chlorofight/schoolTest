
def main():
  newMessage = ''
  for character in message:
    if character in alphabet:
      position = alphabet.find(character)
      newPost = (position + key) % 26
      newChar = alphabet[newPost]
      #print (newChar)
      newMessage += newChar
    else:
      newMessage += character
  print(newMessage,'\n')

while True:
  alphabet = 'abcdefghijklmnopqrstuvwxyz'
  newMessage = ''
  key = 1
  
  cringe = input('1 to break and 2 to create \n')
  message = input('Please enter a message \n')


  if cringe == '1':
 
    while key < 25:
      key = key + 1
      main()

  elif cringe == '2':
    key = int(input('please enter you key \n'))
    main()
  restart = input ('woulld you like to break/create again (y/n)')
  if restart == 'y':
    continue
  else:
    break
