# ANSI color codes:
PINK = "\033[1;35m"
RESET = "\033[0m"

# 1)
import torch

# 2)
x1 = torch.tensor([3,7,2,9,1])
x2 = torch.tensor([[1,4,7],[2,5,8],[3,6,9]])
x3 = torch.tensor([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
x4 = torch.rand(4,4,4)
vectors =[x1, x2, x3, x4]

print(f"{PINK}Solutions for task 2: {RESET}")
for x in vectors:
    print(f"The vector is:\n{x}")
    print(f"and its shape is {x.shape}\n")


# 3)
print(f"{PINK}Solutions for task 3: {RESET}")
print(f"{PINK}a) {RESET}")

A = torch.tensor([[2, 4], [6, 8]])
B = torch.tensor([[1, 3], [5, 7]])
addition = A+B
multiplication = A*B
matrix_mult = torch.mm(A,B)
print(addition)
print(multiplication)
print(matrix_mult)

print(f"{PINK}b) {RESET}")
sum_col_A = A.sum(dim=0) # sum across columns
sum_row_A = A.sum(dim=1) # sum across rows
mean_col_A = A.float().mean(dim=0)
mean_row_A = A.float().mean(dim=1)
print(f"For Matrix A:\nsum across columns:\t{sum_col_A}\nsum across rows:\t{sum_row_A}\nmean across columns:\t{mean_col_A}\nmean across rows:\t{mean_row_A}\n")
sum_col_B = B.sum(dim=0) 
sum_row_B = B.sum(dim=1) 
mean_col_B = B.float().mean(dim=0)
mean_row_B = B.float().mean(dim=1)
print(f"For Matrix B:\nsum across columns:\t{sum_col_B}\nsum across rows:\t{sum_row_B}\nmean across columns:\t{mean_col_B}\nmean across rows:\t{mean_row_B}\n")

print(f"{PINK}c) {RESET}")
max_A = A.max()
min_A = A.min()
argmax_A = A.argmax()
argmin_A = A.argmin()
print(f"For Matrix A:\nMax val:\t{max_A}\nMin val:\t{min_A}\nArgmax val:\t{argmax_A}\nArgmin val:\t{argmin_A}\n")

max_B = B.max()
min_B = B.min()
argmax_B = B.argmax()
argmin_B = B.argmin()
print(f"For Matrix B:\nMax val:\t{max_B}\nMin val:\t{min_B}\nArgmax val:\t{argmax_B}\nArgmin val:\t{argmin_B}\n")

print(f"{PINK}Solutions for task 4: {RESET}")
T = torch.tensor([[10, 20, 30], [40, 50, 60], [70, 80, 90]])
sum_T = T.sum()
print(f"{PINK}a){RESET} Sum across columns and rows:\t{sum_T}\n")
mean_col_T = T.float().mean(dim=0)
mean_row_T = T.float().mean(dim=1)
print(f"{PINK}b){RESET}\nMean along columns:\t{mean_col_T}\nMean along rows:\t{mean_row_T}\n")

argmax_row_T = T.argmax(dim=1)
argmin_row_T = T.argmin(dim=1)
print(f"{PINK}c){RESET}\nIndices of max values along each row:\t{argmax_row_T}\nIndices of min values along each row:\t{argmin_row_T}\n")


print(f"{PINK}Solutions for task 5: {RESET}")

X = torch.tensor([0.1, 0.6, 0.8, 0.3, 0.9, 0.4])
mask = X > 0.5
print(f"{PINK}a){RESET} {X[mask]}\n")

Y = torch.tensor([2.0, 1.0, 0.1])
probs = torch.nn.functional.softmax(Y, dim=0)
print(f"{PINK}b){RESET} {probs}\n")

C = torch.tensor([1, 2, 3])
D = torch.tensor([4, 5, 6])
combined = torch.cat((C,D), dim=0)
print(f"{PINK}c){RESET} {combined}\n")

Z = torch.tensor([5, 1, 8, 3, 7])
sorted_Z, indices = torch.sort(Z)
print(f"{PINK}d){RESET}\nZ sorted:\t{sorted_Z}\nSorted Indices:\t{indices}\n")

iter_tensor = torch.tensor([[17, 18, 19], [14, 15, 16], [10, 11, 12]])
print(f"{PINK}e){RESET}")
flattened = iter_tensor.flatten()
for val in flattened:
    print(val.item())
print("\n")