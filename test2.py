def get_minimum_connections(matrix):
    test_m= matrix
    rows = len(test_m)
    counts=0
    for i in range (rows):
        if matrix([i],[])==1:
            counts = counts+1
    return counts
    
matrix = \
    [ 
        [0, 1, 0, 0, 1], 
        [1, 0, 0, 0, 0], 
        [0, 0, 0, 1, 0], 
        [0, 0, 1, 0, 0], 
        [1, 0, 0, 0, 0] 
    ]
print(get_minimum_connections(matrix)) # should print 1