import sys
import json
  
    
def main():

    tweet_file = open(sys.argv[1])
    freq = {}
    occurences = 0
    
    lines = tweet_file.readlines()
    for line in lines:
        linedict = json.loads(line)
        try:
            encoded = linedict["text"].encode('utf-8')      
        except KeyError:
            encoded = ""
        finally:
            phrase = encoded.split()
        
        occurences += len(phrase)
        for word in phrase:
            if word.isalpha():
                f = freq.get(word, 0)
                freq[word] = f+1
                
    for word in freq:
        print word, freq[word] * 1.0 / occurences

if __name__ == '__main__':
    main()
