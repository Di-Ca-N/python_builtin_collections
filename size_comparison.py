import sys
from collections import deque

NUM_ELEMS = 1000000
BASE_RANGE = range(NUM_ELEMS)

t = tuple(BASE_RANGE)
l = list(BASE_RANGE)
d = dict(enumerate(BASE_RANGE))
s = set(BASE_RANGE)
dq = deque(BASE_RANGE)

tuple_size = sys.getsizeof(t)
list_size = sys.getsizeof(l)
dict_size = sys.getsizeof(d)
set_size = sys.getsizeof(s)
deque_size = sys.getsizeof(dq)

print(f"Size of tuple with {NUM_ELEMS} elements: {tuple_size}")
print(f"Size of list with {NUM_ELEMS} elements: {list_size}")
print(f"Size of dict with {NUM_ELEMS} elements: {dict_size}")
print(f"Size of set with {NUM_ELEMS} elements: {set_size}")
print(f"Size of deque with {NUM_ELEMS} elements: {deque_size}")
print()

print("Relative size comparison with the tuple:")
print(f"The list is {list_size / tuple_size} times bigger")
print(f"The deque is {deque_size / tuple_size} times bigger")
print(f"The set is {set_size / tuple_size} times bigger")
print(f"The dict is {dict_size / tuple_size} times bigger")
