import requests
import threading
from Data import *
# A program to translate into all languages 
# Education use  
# Thank you Google Translate

def parse(count,unparse,lang):
    ind = unparse.index('"'+lang)
    need = unparse[ind:]
    need2 = need.split(",")[7]
    need3 = need2.split('"')[1]
    ans = str(count)+" . "+lang+" : "+ need3[:-1]
    return ans


text = input(" Enter your text: ")
# text = "happy onam to you"


payval = '[[["MkEWBc","[[\\"'+text+'\\",\\"auto\\",\\"lang\\",1],[]]","null","generic"]]]'

def makeTranslateCall(payload, lang, count):
    response = requests.post(url, headers=headers, data=payload, params=params)
    print(response.text)
    try:
        translated = parse(count, response.text, lang)
        alllang.append(translated)
    except Exception as e:
        print("failed for : ", payload, "Exception : ", e)

alllang = []
threads = []
count = 0

for lang in languages.values():
    v = payval.replace("lang", lang)
    payload = {"f.req": v}
    count += 1
    t1 = threading.Thread(target=makeTranslateCall, args=(payload, lang, count))
    threads.append(t1)
    t1.start()

# Wait for all threads to complete
for thread in threads:
    thread.join()

# Print the translated results
for translation in alllang:
    print(translation)
print(len(alllang))