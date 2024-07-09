
def filechek():
    while True:
        try:
            with open('output.txt', 'r',  encoding='utf-8') as file:
                text = file.read()
                break
        except Exception:
            print('error file read')
    text = text.strip()
    count_o = 0
    count_oo = 0
    count_DD = 0
    count_D = 0
    count_s = 0
    count_ss = 0
    count_v = 0
    count_vv = 0
    for i in text:
        if i == ')':
            count_o += 1
        elif i == '(':
            count_oo += 1
        elif i == '[':
            count_DD += 1
        elif i == ']':
            count_D += 1
        elif i == '{':
            count_ss += 1
        elif i == '}':
            count_s += 1
        elif i == '<':
            count_vv += 1
        elif i == '>':
            count_v += 1
    if count_o != count_oo or count_DD != count_D or count_ss!=count_s or count_v!= count_vv:
        print('false and your file is deleted')
        with open('output.txt','w')as file:
            file.write("[]<{hehe}>[]")
    else:
        print('true good file')
#filechek()
'''def evclid(a= 12, b = 13):
    while b != 0:
        a, b = b, a % b
    return a
print(evclid(300,4))'''
def evclid_reverse(a=1, b=0):
    if b == 0:
        return a
    else:
        a, b = b, a % b
        return evclid_reverse(a,b)
print(evclid_reverse())
