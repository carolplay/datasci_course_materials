import sys
import json

def hw():
    print 'Hello, world!'

def lines(fp):
    print str(len(fp.readlines()))

def load_afinn(afinnfile):
    #afinnfile = open("AFINN-111.txt")
    
    scores = {} # initialize an empty dictionary
    for line in afinnfile:
        term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
        scores[term] = int(score)  # Convert the score to an integer.
    #print scores.items() # Print every (term, score) pair in the dictionary
    
    return scores

    
def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    #hw()
    #lines(sent_file)
    scores = load_afinn(sent_file)
    #lines(tweet_file)
    
    lines = tweet_file.readlines()
    #lines = json.load(tweet_file)
    for line in lines:    
        #print type(lines[i])
        linedict = json.loads(line)
        try:
            encoded = linedict["text"].encode('utf-8')
            
        except KeyError:
            encoded = ""
        
        words = encoded.split()
        text_sentiment = 0
        for word in words:
            if word.isalpha():
                try:
                    word_sentiment = scores[word]
                except KeyError:
                    word_sentiment = 0
                text_sentiment += word_sentiment
        print text_sentiment

if __name__ == '__main__':
    main()
