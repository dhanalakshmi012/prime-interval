# prime-interval
upper=raw_input("enter the num:")
lower=raw_input("enter the num:")
num=raw_input("enter the num:")
for num in range(lower,upper+1)
   if num>1:
      for i in range(2,num)
         if(num%i)!=0:
            print(num)
            break
   
