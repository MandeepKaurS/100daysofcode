from replit import clear
import art
#HINT: You can call clear() to clear the output in the console.
print(art.logo)
condition=True

bids={}
while(condition):
  
  user_name=input("what is your name?")
  bid_price=int(input("How much do you want to bid for?"))
  bids.update({user_name: bid_price})
  more_users=input("Is there any other user who want to bid?(Yes/No)")
  clear()
  if(more_users=="No"):
    condition=False
    break
sortedu=sorted(bids.items(),key=lambda x:x[1],reverse=True)
print(f"{list(dict(sortedu).keys())[0]} won the bid!")
