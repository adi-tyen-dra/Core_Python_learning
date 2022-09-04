# ques: detect the series b/w ap, gp and fibonachi and predict the next term.

input1 = 5
input2 = [3, 3, 6, 9, 15]
d = input2[1]-input2[0]
r = input2[1]//input2[0]
for i in range(0, input1):
    if input2[i] == input2[0] + i*d:
        continue
    else:
        break
else:
    ans = input2[input1-1]+d
    print(ans, "ap")

for i in range(1, input1):
    if input2[i] == input2[i-1]*r:
        continue
    else:
        break
else:
    ans = input2[input1-1]*r
    print(ans, "gp")

for i in range(2, input1):
    if input2[i] == input2[i-1]+input2[i-2]:
        continue
    else:
        break
else:
    ans = input2[input1-1] + input2[input1-2]
    print(ans, "fibonache")

# ques: count unique char of str2 from first and last occurrence of string1 char in string 2
string1 = "a"
string2 = "healo amasd frad abl sbjb"
start = 0
end = 0
string2 = string2.replace(" ", "")
for i in string2:
    if i == string1:
        start = string2.index(i)
        break
string2 = string2[::-1]
for j in string2:
    if j == string1:
        end = len(string2)- string2.index(j)
        print(string2.index(j), len(string2))
        break
string2 = string2[::-1]
resultstr = string2.replace(" ", "")[start+1:end-1]
print(resultstr)
arrans=""
ans=0
for elem in resultstr:
    if elem in arrans:
        continue
    else:
        ans +=1
        arrans = arrans+elem
else:
    print(ans)

# ques: reduce given n to one and report the min possible steps; allowed operations- (n/x if x%n == 0) and (n-1)
def mul_finder(n):  #to find highest multiple
    max_mul=0
    for i in range(2,n):
        if n % i == 0:
            max_mul = i
    return max_mul

def resolver(n):  #to resoolve n to 1
    counter=0
    while(n>1):
        mul = mul_finder(n)
        if(mul == 0):
            n-=1
        else:
            n = n//mul
        counter+=1
    return counter

n = int(input())
ans = resolver(n)
print(ans)
