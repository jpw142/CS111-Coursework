s = 'cs111'
t = 'is amazing!'

u = s[1] + t[-4: ] 
s = s[ :2] + (t[-1]*2)
t = t[1:-2:2]
s[::-2]

print(s, t, u)
