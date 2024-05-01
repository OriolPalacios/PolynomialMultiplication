def horner_evaluation(A):
    n = len(A) + 1
    x = [i for i in range(n)]
    res = [A[-1] for _ in range(n)]
    for k in range(n):
        for i in reversed(range(1, len(A))):
            res[k] = x[k] * res[k] + A[i-1]
    return res

def convolution(A, B):
    coefficients = [0 for _ in range(len(A) + len(B) - 1)]
    for i in range(len(A)):
        for j in range(len(B)):
            coefficients[i + j] += A[i] * B[j]
    return coefficients

def lagrange_interpolation(x, y):
    coefficients = []
    partial_polynomials = []
    n = len(x)
    for i in range(n):
        denominator, numerator = 1, [1, 0]
        for j in range(n):
            if i != j:
                denominator *= x[i] - x[j]
                numerator = convolution(numerator, [-x[j], 1])
        numerator = [k/denominator*y[i] for k in numerator]
        partial_polynomials.append(numerator)
    for i in range(n):
        coefficients.append(sum([partial_polynomials[j][i] for j in range(n)]))
    return coefficients

def poly_mul_lagrange(A, B):
    if len(A) < len(B):
        A += [0] * (len(B) - len(A)) 
    if len(A) > len(B):
        B += [0] * (len(A) - len(B)) 
    # Horner's Evaluation
    evaluation_A = horner_evaluation(A)
    evaluation_B = horner_evaluation(B)
    # Pointwise Multiplication
    pointwise_mul = [evaluation_A[x] * evaluation_B[x] for x in range(len(A)+1)]
    # Interpolation
    coefficients = lagrange_interpolation([i for i in range(len(A) + 1)], pointwise_mul)
    return coefficients

