import random
import sys

while True:
    class hang:
         def __init__(self,word):
             self.word=word
         def game(self):
             print('*'*len(self.word))
             a=[]
             b=[]
             for i in range(len(self.word)):
                 b.append('*')
             n=len(self.word)*2
             for c in self.word:
                 a.append(c)
             while(n>0):
                 letter=input("Enter:")
                 for x,y in enumerate(a):
                     if y == letter:
                         b[x]=letter
                 print(b)
                 n=n-1
                 if b==a:
                     print('Congrats!')
                     break
                  
             print("Play again")

    def get_word(level):
        if level==1:
            file=open("C:/Users/user/Desktop/level1.txt",'r')
        elif level==2:
            file=open("C:/Users/user/Desktop/level2.txt",'r')
        else:
            print("Invalid")

        word=file.readline()
        word_list=[]
        while(word!=''):
            a=word.replace('\n','')
            word_list.append(a)
            word=file.readline()
        return random.choice(word_list)
            
    if __name__=='__main__':
        level=int(input('Enter level:'))
        word=get_word(level)
        o=hang(word)
        o.game()
