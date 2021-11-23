def Inverse_Matrix():
    R = int(input("Enter the number of rows:"))
    C = int(input("Enter the number of columns:"))

    # Initialize M
    M = []
    print("Enter the entries rowwise:")

    # For user input
    for i in range(R):          # A for loop for row entries
        a = []
        for j in range(C):      # A for loop for column entries
            a.append(float(input()))
        M.append(a)

    n = len(M)
    # row multiplication by a number 's'
    def r_multiply(r, s): return [s*i for i in r]

    def r_subtract(r1, r2): return [(r1[i]-r2[i])
                                    for i in range(len(r1))]  # Subtraction of rows
    for k in range(n):  # interchanging row having diagonal element = 0
        if M[k][k] == 0:
            m = k+1
            while m != k:
                if m == n:
                    m = 0
                if M[m][k] != 0:
                    M[k], M[m] = M[m], M[k]
                    break
                m += 1
    for j in range(n):
        for i in range(n):
            if i != j:        # for making all elements '0' except for diagonal elements
                M[i] = r_subtract(M[i], r_multiply(
                    M[j], (float(M[i][j])/float(M[j][j]))))
            else:           # for making all diagonal elements '1'
                M[i] = r_multiply(
                    M[i], (1/float(M[i][j])))
    print(M)


Inverse_Matrix()
