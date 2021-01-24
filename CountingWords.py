introString = input("Enter Your Introduction")
print(introString)
characterCount = 0
wordCount = 1
for I in introString:
    characterCount = characterCount+1
    if(I==' '):
        wordCount = wordCount+1
print(wordCount)

print(characterCount)