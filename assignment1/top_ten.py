import sys
import json
  
    
def main():

    tweet_file = open(sys.argv[1])
    freq = {}
    
    lines = tweet_file.readlines()
    for line in lines:
        tweet = json.loads(line)
        try:
            hashtags = tweet["entities"]["hashtags"]
        except KeyError:
            hashtags = []
            
        for tag in hashtags:
            count = freq.get(tag["text"], 0)
            freq[tag["text"]] = count+1
    
    freq_list = freq.items()
    freq_list.sort(key = lambda tag: tag[1], reverse = True)

    for (tag_text, f) in freq_list[:10]:
        print tag_text, f

if __name__ == '__main__':
    main()
