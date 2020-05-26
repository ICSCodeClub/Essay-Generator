import libraries.splitter as splitter
import libraries.net_gen as net

def generateEssay(string):
        sentences = splitter.sentenceSplit(string)
        topic_sentences = splitter.getEmotionalSelection(string)

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

                # If it generated something, append it
                generated.append(paragraph)
        return generated

def makePrintable(essayList):
        toPrint = '\t'
        for paragraph in generated:
                toPrint = toPrint + '\n\n\t'
                for sentence in paragraph:
                        toPrint = str(toPrint) + str(sentence)
                        if toPrint.endswith('.'):
                                toPrint = str(toPrint) + ' '
                        elif not toPrint.endswith('. '):
                                toPrint = str(toPrint) + '. ' 
        return toPrint[3:]


if __name__ == "__main__":
        string = ''
        with open('input.txt', 'r') as file:
                string = file.read()

        essay = generateEssay(string)
        print('\n')
        print(makePrintable(essay))
