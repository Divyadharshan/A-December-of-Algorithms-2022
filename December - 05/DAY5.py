#DAY 5

a=input().split("=")
a=int(a[1])
f=a*2*15 + (a-2)*2*6 + (a+3)*2*10
print(f"Expenditure={f}")

print("\nEXPENDITURE WITHIN LIMIT" if (f<5000) else "\nEXPENDITURE EXCEEDING LIMIT")
