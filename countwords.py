
class stringCount:

    def countWords(self,x):
        #define a dictionary to which we shall add the words and there values
        dictionary = {}
        #get the length of the list provided
        num = len(x)
        #iterating through the list provided as input
        iterator = 0

        while iterator<num:
            #seperate each word with in the current string. By default it is spaces
            words = x[iterator].split()
            #loop through each of the separated words
            for k in words:
                #convert each word to lower case
                word = k.lower()
                #check if the word has already been encountered and pushed into the dictionary
                if word in dictionary:
                    #if word already exists in the dictionary increments its value
                    dictionary[word]+=1
                else:
                    #if word doesn't exist then give it a value of 1
                    dictionary[word] = 1
            #increment the iteration factor(acting as our index) so as to access the next element in the sequence     
            iterator+=1


        return dictionary



wordstocount = ["hi there, how are you","are you coming for lunch tonight", "when are we going to the movies"]
newword = raw_input("Type your message here:")
wordstocount.append(newword)
returnedData = stringCount()

print returnedData.countWords(wordstocount)


    
