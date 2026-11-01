def factoriyal(num):
    if num==0 or num==1:
        return 1
    else:
        return (num*(factoriyal(num-1)))
print(factoriyal(4))
#hii
