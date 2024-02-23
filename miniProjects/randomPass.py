#Random Password Generator

import random
import string

#password=""
passwordlen=12
collection= string.ascii_letters + string.digits + string.punctuation
#method1
# for i in range(passwordlen):
#     password+=(random.choice(collection))
# print(password)   

#Method2
password=["".join((random.choice(collection)) for i in range(passwordlen))]
print(password)
  
