apples = ["apple1", "apple2", "apple3"]
oranges = ["orange1", "orange2", "orange3"]

def countApplesAndOranges(s, t, a, b, apples, oranges):
    #start with introducing empty list for orange and apples
    #in apple list we append for i in apples after adding i += a )
    #in orange list we append for j in apples after addind j += b )
    #give us a new list of oranges and apples
    #for i in apples we get for i in range(s, t+1)
    #for j in oranges we get for i in range(s, t+1)
    # return oranges , apples
   
    appleCount = 0
    orangeCount = 0
    for apple in apples:
        newApples = []
        apple += a
        newApples.append(apple)
        for newApple in newApples:
            for newApple in range(s, t+1):
                appleCount += 1


    for orange in oranges:
        newOranges = {}
        orange += b
        
        newOranges.append(orange)
        for newOrange in newOranges:
            for newOrange in range(s, t+1):
                orangeCount += 1
                
                
    return appleCount, orangeCount