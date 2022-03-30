from utils import *

def K16_recovery():
    '''
    Recovers the K16 subkey.

    @Returns:
        (string) : The K16 binary string (without 0b)
    '''
    # The possible key_parts found for each Sbox input
    possible_keys_part = {
        "S1" : [],
        "S2" : [],
        "S3" : [],
        "S4" : [],
        "S5" : [],
        "S6" : [],
        "S7" : [],
        "S8" : []
    }


    R16, L16 = get_R16_L16(cipher_corr) # R16 and L16 registers from correct ciphertext
    R15 = L16                           # According to equations R15 = L16
    R15_expanded = expand(R15)          # Expansion of R15 to 48 bits

    for faulted_cipher in cipher_fault:
        R16_err, L16_err = get_R16_L16(faulted_cipher)  # R16 and L16 registers from faulted ciphertext
        R15_err = L16_err
        R15_err_expanded = expand(R15_err)

        R16_xor_R16err = xor(R16, R16_err)              # R16 xor R16_err
        revP_R16_xor_R16err = rev_perm(R16_xor_R16err)  # P^-1(R16 xor R16_err)

        equations = []      # The equations we must solve
        for i in range(0, 32, 4):
            equations.append(revP_R16_xor_R16err[i:i+4])

        for i in range(8):  # Exhaustive search on K16 subparts possible values
            if equations[i] == '0000':
                continue
            sbox_name = 'S' + str(i + 1)
            result = exhaustive_attack_sbox(sbox_name, R15_expanded[i*6:(i+1)*6], R15_err_expanded[i*6:(i+1)*6], equations[i])
            if result != []:
                possible_keys_part[sbox_name].append(result)
        
    for key in list(possible_keys_part.keys()):
        possible_keys_part[key] = intersect(possible_keys_part[key])

    # Recovery of K16
    K16 = ''
    for part in possible_keys_part.values():
        K16 += part[0]
    return K16

#print(K16_recovery())
