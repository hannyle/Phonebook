def phonebook_manager():
  N= int(input())
  
  if N<1 or N>10**5:
    print("Error")  
  else:
    phonebook={}
    number_list=[]
    
    for i in range(N):
      s=str(input().strip())
      s_split=s.split()

      if s_split[0]=='add':
        number=s_split[1]
        name=s_split[2]
        if len(number)<=7 and len(name)<=15 and name!="not found":
          number_list.append(int(number))
          phonebook[name]=number_list      
          
        
      

      elif s_split[0]=='delete':
        if name in phonebook:
          del phonebook[name]

      elif s_split[0]=='find':
        if name in phonebook:
          find_output=phonebook.get(name)
          min_value = find_output[0]
          for i in range(len(find_output)):
            if min_value > find_output[i]:
              min_value = find_output[i]
          print(min_value)
        else:
          print('Not found')
    
    
    
    
