import requests
import threading
from Data import *
# A program to translate into all languages 
# Education use  
# Thank you Google Translate
# developed for learning
# changed
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

# Enter number of operations/threads needed
n = int(input("Enter the value of n: "))
thread_list = ["t" + str(i) for i in range(1, n + 1)]

alllang = []
threads = []
count = 0
thread_count = 0

for lang in languages.values():
    v = payval.replace("lang", lang)
    payload = {"f.req": v}
    if thread_count < n:
        count += 1
        Th = threading.Thread(target=makeTranslateCall, args=(payload, lang, count))
        threads.append(Th)
        Th.start()
        thread_count += 1

# Wait for all threads to complete
for thread in threads:
    thread.join()

# Print the translated results
for translation in alllang:
    print(translation)
print(len(alllang))