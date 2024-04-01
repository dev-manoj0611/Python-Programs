d={'January':31,'February':28,'March':31,'April':30,'May':31,'June':30,'July':31,
   'August':31,'September':30,'October':31,'November':30,'December':31}
while(True):
   month=input("Please Enter a month to find its number of days : ").capitalize()
   def number_of_days_in_a_month(month):
      if not month.isalpha():
         print('Only alphabets are allowed')
      elif d.__contains__(month):
         print(month,'has',d.get(month),'days')
         exit(0)
      else:
         print('kindly do spell check / short forms aren\'t allowed')
   number_of_days_in_a_month(month)