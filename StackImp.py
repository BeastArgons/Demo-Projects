####### STACK IMPLEMENTATION #######

def isEmpty(stk) :
 if stk == [] :
  return True
 else :
  return False

def push(stk, item) :
 stk.append(item)
 top = len(stk) - 1

def pop(stk):
 if isEmpty(stk) :
  return "Underflow"
 else :
  item = stk.pop()
  if len(stk) == 0:
   top = None
  else :
   top = len(stk) - 1
   return item

def peek(stk):
  if isEmpty(stk) :
    return "overflow"
  else :
    top = len(stk) - 1
    return stk[top]

def Display(stk):
  if isEmpty(stk) :
    print("Stack Empty")
  else :
    top = len(stk) - 1
    print(stk[top], "<-top")
    for a in range(top-1, -1, -1):
      print(stk[a],)


#__main__                   #initially stack is empty
Stack = []
top = None

while True :
  print("STACK OPERATIONS")
  print("1. Push")
  
