def min_steps(sequence):
    if len(sequence) == 0 or len(sequence) == 1:
        return 0

    curr = list(sequence[0])
    result = 0

    for i, step in enumerate(sequence[1:]):
        while curr != list(step):
            stepped = False
            #case up
            if curr[0] < step[0]:
                curr[0] += 1
                stepped = True

            #case down
            elif curr[0] > step[0]:
                curr[0] -= 1
                stepped = True
            
            #case right
            if curr[1] < step[1]:
                curr[1] += 1
                stepped = True
            
            #case left
            elif curr[1] > step[1]:
                curr[1] -= 1
                stepped = True
            
            if stepped:
                result += 1
    
    return result

if __name__ == "__main__":
    seq = [(0,0), (1,1), (1,2), (3,4)]
    print(min_steps(seq))