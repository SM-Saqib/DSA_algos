class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        
#         print(paragraph)
#         print("break")
#         print("banned")
        paragraph_list = paragraph.replace(".","").replace(",","").replace("!","").split(" ")
        paragraph_list = [i for i in paragraph_list if not i in banned]
        # paragraph_set = set(paragraph_list)
        dict_occurence = {}
        for elem in paragraph_list:
            if elem.lower() in dict_occurence:
                dict_occurence[elem.lower()] += 1
            else:
                dict_occurence[elem.lower()] = 1
        max_key = max(dict_occurence,key = dict_occurence.get)
        print(max_key)
        return max_key
            
            
        # print(paragraph_list)
        
