class Node:
  pass

import math
def make_node(data,left,right):
  ans=Node()
  ans.data=data
  ans.left=left
  ans.right=right
  return ans
def make_link(data,next):
  ans=Node()
  ans.data=data
  ans.next=next
  return ans

def f(l,depth):    
  if l is None:
    return None,None
  data=l.data
  if depth<=1:
    return make_node(data,None,None),l.next
  left,rest=f(l.next,depth-1)
  right,rest=f(rest,depth-1)
  return make_node(data,left,right),rest
def length(l):
  if l is None:
    return 0
  return 1+length(l.next)

def g(l):
  if l is None:
    return None,None
  head=l.data
  left,left_left_over=g(l.next)
  right,right_leftover=g(left_left_over)
  return make_node(head,left,right),right_leftover  
def convert(l):
  depth=math.log2(length(l))
  ans,rest=f(l,depth)
  assert(rest==None)
  return ans
  

def make_list(s):
  ans=None
  for c in s.split():
    ans=make_link(c,ans)
  return ans

def print_tree(t,indent):
  if t is None:
    #pass
    return print(indent,'-')
  data=t.data
  if (t.left is None and t.right is None):
    return print(indent,'(',data,')')
  indent+=' '
  print(indent,data)
  print_tree(t.left,indent)
  print_tree(t.right,indent)

l=make_list('this is an example of a list, a few more workds becuase it is what it is everytime')
t,_=g(l)
print('first solutib - not balanceed')
print_tree(t,'')
t=convert(l)
print('second solution  balanceed')
print_tree(t,'')
