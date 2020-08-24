import json
from random import randint
from config import languages

class Words():
    def __init__(self, dbms):
        self.__dbms = dbms
        self.__lang = self.__dbms.get_lang()
        self.__qty = self.__dbms.get_send_qty()
        # 
        self.__used_id = []
        with open(languages[self.__lang], 'r', encoding='utf-8') as f:
            self.__words = json.load(f)

    def __get_random(self, words):
        return randint(0, len(words))

    def new_words(self):
        qty = self.__qty[0]
        used = self.__dbms.get_progress(self.__lang)
        i = 0
        res = []
        
        while (i < qty):
            index = randint(0, len(self.__words)-1)
            if index not in used:
                used.append(index)
                res.append(self.__words[index])
                i += 1
        self.__dbms.set_progress(self.__lang, used)

        return res
    
    def repeat_words(self):
        qty = self.__qty[1]
        used = self.__dbms.get_progress(self.__lang)
        
        if len(used) == 0:
            return None
        elif qty >= len(used):
            qty = len(used)
        
        r_used = []
        i = 0
        res = []
        while (i < qty):
            index = used[randint(0, len(used) - 1)]
            if index not in r_used:
                r_used.append(index)
                res.append(self.__words[index])
                i += 1
        
        return res
    
        
        


        
        
