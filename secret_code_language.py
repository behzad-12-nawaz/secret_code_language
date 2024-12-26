import random

coding=(input('Enter 0 for "coding" & 1 for "decoding":'))
coding=bool(coding=="0")
st=(input('Enter your message:'))
words=st.split(' ')
rwords="abcdefghijklmnopqrstuvwxyz"
if(coding):
  code=[]
  for word in words:
    if(len(word)>=3):
      new_words=random.choice(rwords)
      new_words1=random.choice(rwords)
      new_words2=random.choice(rwords)
      stnew=new_words+new_words1+new_words2+word[1:]+word[0]+new_words2+new_words+new_words1
      code.append(stnew)
    else:
      code.append(word[::-1])
  print(' '.join(code))
else:
  code=[]
  for word in words:
    if(len(word)>=3):
      stnew=word[3:-3]
      stnew=stnew[-1]+stnew[:-1]
      code.append(stnew)
    else:
      code.append(word[::-1])
  print(' '.join(code))
y=input()