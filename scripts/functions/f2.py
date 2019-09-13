import random as rn
def get_rand_list():
    a= list()
    for i in range(5):
        a.append(rn.randint(100,200))

get_rand_list()
print(a)