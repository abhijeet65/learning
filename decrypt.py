s=input()
n=int(input())
ans=""
for i in range(0,len(s)):
    if(s[i].isdigit()):
        ans=ans*int(s[i])
    else:
        ans=ans+s[i]
print(ans)
print(ans[n])

