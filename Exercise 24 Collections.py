# exercise 24
# Collections special data types fulfil needs other than tuple, list, set and dictionary

from collections import namedtuple, deque, ChainMap, Counter, OrderedDict, defaultdict

# namedtuple access tuple values with names.

a=namedtuple('courses', 'coursename, technology')
my_namedtuple= a('Programming', 'Python')
print(my_namedtuple)


a_list=['a','b','c','d','a','b','c','d']
b_deque = deque(a_list)
print(b_deque)
b_deque.appendleft('new')
print('deque apendleft ', b_deque)
b_deque.popleft()
print('deque popleft ', b_deque)


a_dict={1:'a', 2:'b'}
b_dict={3:'c' , 4:'d'}
c_chainmap= ChainMap(a_dict,b_dict)
print(c_chainmap[3])


int_list=[1,1,1,2,2,3,3,3,3,4,4,4,5,5,5,5,5,5]
int_counter = Counter(int_list)
print(int_counter)
print(int_counter.most_common()) 
print(int_counter.most_common(1))
sub = {2:1 , 5:1}
int_counter.subtract(sub)
print(int_counter.most_common())

o_dict= OrderedDict()

o_dict['3']=333
o_dict[2]=222
o_dict[1]=111
o_dict[5]=555
o_dict[4]=444
o_dict[6]=666

print(o_dict)

a_defaultdict = defaultdict(str)

a_defaultdict['name'] = 'My Name'
a_defaultdict['age'] = 'My Age'
print(a_defaultdict['age'])
print(a_defaultdict['height'])

