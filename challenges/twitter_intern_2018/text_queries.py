def tokenize(sentence):
    return sentence.split(" ")
    
class InvertedIndex:    
    def __init__(self):
        self.dict = {}
    
    def get_docs_ids(self, token):
        if token in self.dict:
            return self.dict[token]
        else:
            return []
        
    def put_token(self, token, doc_id):
        if token in self.dict:
            self.dict[token] += [doc_id]
        else:
            self.dict[token] = [doc_id]
            
def add_to_inverted_index(inverted_index, sentence, sentence_id):
    sentence_tokens = tokenize(sentence)
    
    for token in sentence_tokens:
        inverted_index.put_token(token, sentence_id)                

def create_inverted_index(sentences):
    inverted_index = InvertedIndex()
    for index, sentence in enumerate(sentences, start=0):
        add_to_inverted_index(inverted_index, sentence, index)
    
    return inverted_index
    
def is_one_term_query(query):    
    return len(query.split(" ")) == 1
    
def _intersect(list1, list2):            
    result = []    
    i, j = 0, 0    
    
    while i < len(list1) and j < len(list2):    
        if list1[i] == list2[j]:
            result.append(list1[i])
            i += 1
            j += 1        
        else:            
            if list1[i] < list2[j]:
                i += 1
            else:
                j += 1
    
    return result        

def _boolean_search(terms_to_search, inverted_index):
              
    for i, term in enumerate(terms_to_search):
        phrases_ids = inverted_index.get_docs_ids(term)

        if i == 0:
            result = phrases_ids
        else:
            result = _intersect(result, phrases_ids)
            
    return result

def search(query, inverted_index):
    
    if is_one_term_query(query):
        return inverted_index.get_docs_ids(query)
    
    else:    
        terms_to_search = query.split(" ")
        resut
        return _boolean_search(terms_to_search, inverted_index)

def textQueries(sentences, queries):    
    inverted_index = create_inverted_index(sentences)    
    
    for query in queries:
        search_result = search(query, inverted_index)
        
        search_result = list(map(str, search_result))
        print(" ".join(search_result))

if __name__ == '__main__':
	
	N = int(input())
	sentences = []	
		
	for _ in range(N):
		sentence = input()
		sentences.append(sentence)
	
	M = int(input())
	queries = []
	
	for _ in range(M):
		query = input()
		queries.append(query)	
	
	res = braces(values)
	print(res)
		

