import sys
import json


def lines(fp):
    print str(len(fp.readlines()))

def load_afinn(afinnfile):  
    scores = {} # initialize an empty dictionary
    for line in afinnfile:
        term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
        scores[term] = int(score)  # Convert the score to an integer.
    return scores

def construct_sent(word, score, terms):
    item = terms.get(word)
    if item == None:
        score += 0.0
        terms[word] = {'appearances': 1, 'score': score}
    else: 
        x = item['appearances']
        score = ( score + item['score']*x ) / (x+1)
        item = {'appearances': x+1, 'score': score}
        terms[word] = item
    
    
       
def calculate_sentiment(tweet_file, scores):
    #print "function calculate sentiment"
    terms = {}  # Dictionary: word: {apperences: , score: , }
    lines = tweet_file.readlines()
    
    for line in lines:    
        #print type(lines[i])
        linedict = json.loads(line)
        try:
            encoded = linedict["text"].encode('utf-8')
            
        except KeyError:
            encoded = ""
        
        words = encoded.split()
       
        text_sentiment = 0
        new_words_count = 0
        for word in words:
            #print word
            if word.isalpha():
                try:
                    word_sentiment = scores[word]
                except KeyError:
                    new_words_count += 1
                    word_sentiment = 0
                text_sentiment += word_sentiment
                #print text_sentiment
        if new_words_count != 0:   
            avg_sentiment = text_sentiment / new_words_count
            for word in words:
                if word not in scores:
                    construct_sent(word, avg_sentiment, terms)
    
    #print terms    
    for item in terms:
        print item, terms[item]['score']
            
        
    return terms    
        #print text_sentiment
  
    
def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    scores = load_afinn(sent_file)
    calculate_sentiment(tweet_file, scores)

if __name__ == '__main__':
    main()
