import libraries.splitter as splitter
import libraries.net_gen as net


def generateEssay(string):
        sentences = splitter.sentenceSplit(string)
        topic_sentences = splitter.getEmotionalSelection(string)
        quotes = splitter.getQuotesDictFromSelectSentences(string, topic_sentences)

        generated = []
        for i in range(len(topic_sentences)):
                paragraph = [topic_sentences[i]]
                
                passes = 0
                while passes < 4 and len(paragraph) < 2:
                        continuation = net.generate(prefix=(str(topic_sentences[i])+' '),start=False)
                        passes += 1
                               
                        for continuationSentence in splitter.sentenceSplit(continuation):
                                if len(continuationSentence) > 1 and '==' not in continuationSentence and '\n' not in continuationSentence and not ('<' in continuationSentence and '>' in continuationSentence):
                                        paragraph.append(continuationSentence)

                if topic_sentences[i] in quotes:
                        for q in quotes[topic_sentences[i]]:
                                continuation = net.generate(prefix=(topic_sentences[i]+' '+q+' '),start=False)
                                paragraph.append(q)
                                for continuationSentence in splitter.sentenceSplit(continuation):
                                        if len(continuationSentence) > 1 and '==' not in continuationSentence and '\n' not in continuationSentence and not ('<' in continuationSentence and '>' in continuationSentence):
                                                paragraph.append(continuationSentence)
                
                # If it generated something, append it
                generated.append(paragraph)
        return generated

def makePrintable(essay):
        toPrint = '\t'
        for paragraph in essay:
                toPrint = toPrint + '\n\n\t'
                for sentence in paragraph:
                        toPrint = str(toPrint) + str(sentence)
                        if toPrint.endswith('.'):
                                toPrint = str(toPrint) + ' '
                        elif not toPrint.endswith('. '):
                                toPrint = str(toPrint) + '. ' 
        return toPrint[3:]

from Levenshtein import distance
def areSimilar(s1, s2):
        dist = distance(str(s1).lower(), str(s2).lower())
        return dist < (len(s1)*0.6) # Can be 60% similar

def essayPostProcessing(essay):
        newEssay = []
        for paragraph in essay:
                newEssay.append([])
                for sentence in paragraph:
                        shouldAdd = True
                        for toCheck in newEssay[-1]:
                                if areSimilar(sentence, toCheck):
                                        shouldAdd = False
                        if shouldAdd:
                                newEssay[-1].append(sentence)
        return newEssay
                        

if __name__ == "__main__":
        string = ''
        with open('input.txt', 'r') as file:
                string = file.read()

        essay = generateEssay(string)
        print('\n')
        print(makePrintable(essayPostProcessing(essay)))
