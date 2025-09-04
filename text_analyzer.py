class TextAnalyzer(object):
    def __init__(self,text):
        formattedText = text.replace('.','').replace(',','').replace(';','').replace('?','').replace('!','')
        formattedText = formattedText.lower()
        self.fmtText = formattedText

    def freqAll(self):
        #split text into words
        wordList = self.fmtText.split(' ')
        #make dictionary
        freqMap = {}
        for word in set(wordList): #using "set" to remove duplicates in list
            freqMap[word] = wordList.count(word)

        return freqMap

    def freqOf(self,word):
        freqDict = self.freqAll()

        if word in freqDict:
            return freqDict[word]
        else:
            return 0