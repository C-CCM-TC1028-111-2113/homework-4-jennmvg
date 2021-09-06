def main():
  x=0
  y=1
  z=0
  while True:
    index=int(input('Enter the index: '))
    if index>1:
      break
    print("0")
    pass 
  for i in range(0,index):
    z=x+y
    #print(f"{z}",end=" ")
    x=y
    y=z
  #print("")
  print (z)
main()
