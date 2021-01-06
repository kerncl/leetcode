# Question: Easy
"""
Given a string licensePlate and an array of strings words, find the shortest completing word in words.

A completing word is a word that contains all the letters in licensePlate. Ignore numbers and spaces in licensePlate, and treat letters as case insensitive. If a letter appears more than once in licensePlate, then it must appear in the word the same number of times or more.

For example, if licensePlate = "aBc 12c", then it contains letters 'a', 'b' (ignoring case), and 'c' twice. Possible completing words are "abccdef", "caaacab", and "cbca".

Return the shortest completing word in words. It is guaranteed an answer exists. If there are multiple shortest completing words, return the first one that occurs in words.
"""
from collections import Counter
from typing import List
import logging


class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        try:
            licensePlate = licensePlate.replace(' ', '')
        except:
            pass
        licensePlate = licensePlate.lower()
        count_dict = Counter(licensePlate)
        [count_dict.pop(num) for num in set(count_dict.keys()).intersection({'1', '2', '3', '4', '5', '6', '7', '8', '9', '0'})]
        words = sorted(words, key=lambda x:len(x))
        logging.info(f'{count_dict}')
        logging.info(f'{words}')
        for word in words:
            if not set(count_dict.keys()).issubset(set(word)):
                continue
            count = 0
            for _, key in enumerate(count_dict.keys()):
                if count_dict.get(key) > word.count(key):
                    break
                if _ == len(count_dict.keys())-1:
                    return word


if __name__ == '__main__':
    format = '%(asctime)s: %(message)s'
    logging.basicConfig(format=format, level=logging.INFO, datefmt='%H:%M:%S')
    logging.getLogger().setLevel(logging.DEBUG)
    result = Solution()
    licensePlate = "1s3 PSt"
    words = ["step", "steps", "stripe", "stepple"]
    licensePlate2 = "Ah71752"
    words2 = ["suggest", "letter", "of", "husband", "easy", "education", "drug", "prevent", "writer", "old"]
    licensePlate3 = "ESs9799"
    words3 = ["until","gas","problem","official","away","guess","bar","oil","report","form","hit","bag","way","expert","stay","local","move","close","fight","require","new","like","occur","daughter","see","impact","top","there","defense","heavy","lay","million","couple","picture","respond","only","government","man","yard","professional","best","against","remain","keep","summer","different","sort","director","large","wife","pressure","situation","adult","personal","agreement","thing","rest","social","environmental","officer","around","far","build","agency","ground","toward","ok","meeting","interview","marriage","type","own","back","we","where","sport","size","woman","bring","sell","big","environment","discover","day","magazine","example","memory","effect","their","must","answer","heat","think","management","enjoy","determine","war","available","violence","star","prepare","mother","possible","support","hundred","ever","something","according","cold","customer","any","music","team","able","material","voice","sense","describe","south","unit","wishing","model","little","face","value","above","red","reveal","scientist","police","into","billion","short","whose","great","story","victim","late","welcoming","food","eat","control","dog","step","of","guy","be","worry","suggest","interest","help","specific","sister","indeed","staff","fly","lead","set","science","you","worrying","first","even","relationship","degree","western","candidate","affect","raise","our","teacher","visit","special","position","right","private","skill","evening","ask","task","always","weapon","economic","follow","yourself","patient","hold","want","project","or","pretty","along","read","break","difference","commercial","among","have","line","ball","fail","perform","bit","traditional","watch","protect","population","building","data","matter","fear","station","note","baby","night","trade","sea","nation","vote","include","sure","health","doctor","opportunity","door","very","dead","thousand","morning","account","laugh","study","rich","remember","foreign","song","art","period","care","my","truth","boy","major","take","board","lot","group","race","trip","smile","simply","because","sit","tough","bill","practice","improve","operation","machine","culture","maintain","threat","forget","before","check","so","scene","image","huge","factor","key","last","serious","her","bad","rate","under","participant","paper","tonight","push","force","soldier","time","welcomed","policy","enough","whole","happy","church","store","relate","several","should","hour","light","what","establish","ago","mouth","name","quickly","cut","skin","recently","kid","former","two","they","say","start","also","drop","live","main","cause","explain","would","onto","experiencing","legal","kind","particular","trial","travel","town","admit","life","pass","level","out","attack","much","professor","stock","idea","member","seek","public","water","either","risk","without","up","near","author","can","hot","catch","market","activity","die","rule","turn","leader","return","writer","across","consumer","condition","central","discuss","them","window","than","else","itself","process","rather","similar","chance","by","still","everything","leave","run","question","everyone","success","development","recent","coach","cell","instead","article","animal","just","simple","together","bed","less","people","work","product","air","shake","treatment","movie","range","current","few","pattern","begin","nothing","purpose","north","shoot","argue","citizen","space","third","beat","fast","ready","plant","eye","however","open","house","quite","decade","almost","wide","strategy","blue","stand","pain","figure","send","actually","your","ten","list","leg","welcome","foot","score","mind","act","six","security","him","disease","today","whether","prevent","trouble","poor","continue","during","soon","death","decision","nearly","quality","wall","safe","fund","imagine","come","for","over","charge","site","consider","inside","box","generation","go","owner","structure","president","glass","nice","later","edge","fill","here","free","area","as","green","easy","born","method","chair","physical","movement","but","particularly","artist","sometimes","behavior","budget","this","response","feel","book","from","goal","successful","beyond","various","each","letter","it","lie","business","somebody","debate","use","mission","become","allow","five","east","themselves","she","some","give","all","within","measure","compare","side","entire","long","economy","institution","authority","good","identify","place","evidence","general","administration","dinner","phone","modern","radio","industry","on","more","produce","call","everybody","need","option","item","hope","often","let","lose","career","positive","past","me","loss","suddenly","really","manage","outside","community","find","the","working","cup","put","education","fire","write","age","organization","gun","listen","its","head","sing","yet","wait","lawyer","case","prove","pay","weight","expect","teach","world","buy","film","his","design","remove","contain","myself","strong","television","crime","son","mention","hospital","field","a","federal","stuff","reduce","student","offer","class","young","system","source","serve","end","school","tree","old","office","dream","represent","never","high","speech","once","card","necessary","southern","us","oh","treat","month","why","natural","walk","real","color","investment","rock","network","appear","anything","well","approach","experience","politics","claim","senior","blood","talk","who","kitchen","surface","country","body","series","meet","when","role","notice","total","husband","again","player","indicate","seem","responsibility","partner","knowledge","hang","involve","now","shot","especially","address","important","another","small","energy","early","collection","arm","clearly","white","girl","wish","forward","per","center","spring","training","power","manager","grow","front","willing","throughout","price","election","kill","moment","apply","hard","better","page","tell","attention","court","probably","yeah","make","how","present","share","perhaps","if","true","stop","production","too","growth","part","fall","amount","challenge","view","plan","theory","record","exist","media","understand","clear","final","arrive","west","home","three","finish","individual","point","year","develop","benefit","detail","test","character","half","fish","computer","play","executive","off","friend","sex","choice","alone","employee","effort","suffer","happen","herself","many","second","information","cancer","yes","ahead","drug","law","human","maybe","himself","least","someone","street","century","finally","sexual","season","next","same","nor","seven","term","base","college","accept","worker","reach","political","deep","choose","significant","money","course","reality","job","discussion","painting","which","spend","sound","black","standard","thank","thus","experienced","history","military","draw","piece","game","assume","camera","these","cost","look","about","brother","eight","region","program","focus","whom","thought","society","show","number","deal","cover","no","difficult","week","medical","fact","others","car","hand","exactly","nature","love","agent","change","international","will","though","garden","realize","already","beautiful","while","subject","upon","father","such","try","event","direction","one","learn","seat","company","party","agree","result","add","floor","bank","wind","and","through","could","wear","person","mean","then","democratic","low","concern","city","heart","every","feeling","ability","anyone","with","left","sign","enter","national","save","recognize","child","other","behind","statement","news","wrong","likely","state","property","none","speak","believe","that","dark","civil","family","throw","do","get","land","both","resource","rise","in","analysis","most","might","peace","research","message","may","hear","hotel","receive","conference","section","order","attorney","technology","win","hair","majority","miss","fine","capital","despite","provide","certainly","road","reflect","room","tax","stage","since","newspaper","full","down","usually","tend","single","at","language","drive","common","religious","four","action","audience","table","certain","reason","parent","he","wonder","create","middle","not","decide","shoulder","whatever","finger","wondering","between","know","financial","those","carry","future","pick","pull","campaign","word","increase","join","issue","performance","popular","to","after","interesting","although","including","service","firm","avoid","style","minute","cultural"]
    logging.info(f'shortest completing string {result.shortestCompletingWord(licensePlate3, words3)}')
