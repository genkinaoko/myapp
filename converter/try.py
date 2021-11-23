s, t, x = map(int, input().split())

if s < t:
    print("Yes" if s <= x and x < t else "No")
else:
    print("Yes" if x >= s or x < t else "No")