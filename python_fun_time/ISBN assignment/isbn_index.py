import sys

def createIndex():
    dec = { }
    return dec

def recordBook(index, isbm, title):
    index [isbm]=title
	
def findBook(index, isbm):
	if isbm in index:
		return index[isbm]
	else:
		return ""

	
def listBooks(index):
	lis = []
	count = 1
	for key in index:
		s = ""
		s+=str(count) + ") " + key + ": " + index[key]
		lis.append(s)
		count+=1
		
	return lis
		
def formatMenu():
	list = [ 'What would you like to do?', '[r] Record a Book', '[f] Find a Book', '[l] List all Books', '[q] Quit' ]
	return list
	
def formatMenuPrompt():
	return 'Enter an option: '
	
def getUserChoice(inputs):
	inp = input(inputs)
	inp = inp.strip()
	while inp == "":
		inp = input(inputs)
		inp = inp.strip()
	return inp
	
def getISBN():
	inputs = "Enter an ISBN:"
	return getUserChoice(inputs)
	
	
def getTitle():
	inputs = "Enter a book title:"
	return getUserChoice(inputs)
	
def recordBookAction(index):
	isbm = getISBN()
	title = getTitle()
	recordBook(index, isbm, title)
	
def findBookAction(index):
	isbm = getISBN()
	find = findBook(index, isbm)
	if find == "":
		print('No Book Found')
	else:
		print (find)
	
def listBooksAction(index):
	list = listBooks(index)
	if list == []:
		print('No Book Found')
	else:
		for i in list:
			print (i)
	
def quitAction(index):
	print ("Bye! See you next time!")
	sys.exit( 0 )
	
def applyAction(index, string):
	if string == "r":
		return recordBookAction(index)
	elif string == "f":
		return findBookAction(index)
	elif string == "l":
		return listBooksAction(index)
	elif string == "q":
		return quitAction(index)
	else:
		print('Sorry, that option is invalid.')

	
	
def main():
	index = createIndex()
	while True:	
		menu = formatMenu()
		input = formatMenuPrompt()
		input = input.strip()
		for i in menu:
			print (i)
		string = getUserChoice(input)
		applyAction(index, string)
		
	
if __name__ == '__main__':
	main()