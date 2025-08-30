import string
def open_read():
  name = input("Enter file name: ")
  try:
    handle = open(name, 'r')
  except:
    print("File doesn't open")
    quit()

  data = handle.read()
  return data

def data_clean(data):
  data = data.lower()

  translator = str.maketrans('','', string.punctuation)
  translate = data.translate(translator)
  translate = translate.split()

  return translate

def word_count(data):
  word_count = dict()
  for word in data:
    word_count[word] = word_count.get(word, 0) + 1
  return word_count

def common_word(data):
  lst = list()
  for (k,v) in data.items():
    lst.append((v,k))
  lst = sorted(lst, reverse=True)

  for v,k in lst[:10]:
    print(k,v)


data = open_read()
data = data_clean(data)
data = word_count(data)
common_word(data)
