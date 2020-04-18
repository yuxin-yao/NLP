class TrieNode: 
      
    # Trie node class 
    def __init__(self): 
        self.children = {}
        # isEndOfWord is True if node represent the end of the word 
        self.isEndOfWord = False
  
class Trie: 
      
    # Trie data structure class 
    def __init__(self): 
        self.root = self.getNode() 
  
    def getNode(self): 
      
        # Returns new trie node (initialized to NULLs) 
        return TrieNode() 
  
  
    def insert(self,key): 
          
        # If not present, inserts key into trie 
        # If the key is prefix of trie node,  
        # just marks leaf node 
        pCrawl = self.root 
        length = len(key) 
        for level in range(length): 
           
  
            # if current character is not present 
            if key[level] not in pCrawl.children.keys(): 
                pCrawl.children[key[level]] = self.getNode() 
            pCrawl = pCrawl.children[key[level]] 
  
        # mark last node as leaf 
        pCrawl.isEndOfWord = True



def calculateLevenshteinDistance(trie, word):

    currentRow = range(len(word) + 1)

    results = []
    
    for letter in trie.root.children:

        wordRecursive(trie.root.children[letter], letter, word, currentRow, results)
    
    
    return min(results)


def wordRecursive(node, letter, word, previousRow, results):

    m = len(word)
    currentRow = [previousRow[0] + 1]

    for j in range(1, m + 1):

        if word[j - 1] != letter:
            cost = 1 + min(currentRow[j - 1], previousRow[j-1], previousRow[j])
        else:                
            cost = previousRow[j - 1]

        currentRow.append(cost)

    if node.isEndOfWord == True:
        results.append(currentRow[-1])

    for letter in node.children:
        wordRecursive(node.children[letter], letter, word, currentRow, results)

def task4(dictionary, raw):
    """
    TODO:
        implement your optimized edit distance function for task 4 here
        dictionary : path of dictionary.txt file
        raw: path of raw.txt file
        return : a list of min_distance of each word in the raw.txt
        compared with words in the dictonary
    example return result : [0,1,0,2]
    """

    dictionary = open(dictionary).read().split('\n')
    raw = open(raw).read().split('\n')


    trie = Trie()
    for word in dictionary:
        if word.strip() != '':
            trie.insert(word.strip())

    result = []

    for word in raw:
        result.append(calculateLevenshteinDistance(trie, word.strip()))
    
    return result


