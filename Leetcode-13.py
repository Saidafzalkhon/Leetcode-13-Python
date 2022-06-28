if __name__ == "__main__":
    s = input()
    son1 = 0
    for i in s:
        if i == 'M':
            son1+=1000
        if i == 'D':
            son1+=500
        if i == 'C':
            son1+=100
        if i == 'L':
            son1 +=50
        if i == 'X':
            son1+=10
        if i == 'V':
            son1+=5
        if i == 'I':
            son1+=1
    son2 = 0
    for i in range(len(s)):
        if i < len(s)-1:
            if s[i] == 'C' and s[i+1] == 'M':
                son2 +=200
        if i < len(s)-1:
            if s[i] == 'C' and s[i+1] == 'D':
                son2 +=200
        if i < len(s)-1:
            if s[i] == 'X' and s[i+1] == 'L':
                son2 +=20
        if i < len(s)-1:
            if s[i] == 'X' and s[i+1] == 'C':
                son2+=20
        if i < len(s)-1:
            if s[i] == 'I' and s[i+1] == 'X':
                son2+=2
        if i < len(s)-1:
            if s[i] == 'I' and s[i+1] == 'V':
                son2+=2
    print(son1-son2)