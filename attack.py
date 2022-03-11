from utils import *

R16, L16 = get_R16_L16(cipher_corr)
R15 = L16
R16_fault, L16_fault = get_R16_L16(cipher_fault[0])

R16_xor_R16_fault = xor(R16, R16_fault)
revP_xor_R16_fault = rev_perm(R16_xor_R16_fault)

equations = []
for i in range(0, 32, 4):
    if revP_xor_R16_fault[i:i+4] != '0000':
        equations.append(revP_xor_R16_fault[i:i+4])