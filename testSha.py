import sha1 as sha

hashString = ''
exits = ''
while(exits != 'exit'):
    hashString = input("Enter String to Hash... ")
    print(sha.sha1(hashString))
    exits = input("Type exit to close program...")
    
