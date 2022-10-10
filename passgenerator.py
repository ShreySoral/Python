import random
caps='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
lows='abcdefghijklmnopqrstuvwxyz'
nums='0123456789'
specials='!@#$%^&*()_+\/?{[]=+-'
length=18
use=caps+lows+nums+specials
password=''.join(random.sample(use,length))
print(password)