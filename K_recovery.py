import time
from sys import path_importer_cache
from bs4 import BeautifulSoup
import requests
from utils import PC1, PC2
import K16_recovery


def replace_unknown_bits(partial_K, val):
    '''
    Replaces the unknown bits of K with the bits of val.

    Args:
        partial_K (string) : The 56 characters string representing K in binary, 
                             with the unknow bits represented as 'x'.
        val (int) : the value to extract the missing bits from.
    
    Returns:
        string : The string with the 'x' replaces with the bits extracted from val.
    '''
    val = bin(val)[2:].zfill(8)
    partial_K = list(partial_K)
    j = 0
    for i in [8, 17, 21, 24, 34, 37, 42, 53]:
        partial_K[i] = val[j]
        j += 1
    partial_K = "".join(partial_K)
    return partial_K


def add_parity_bits(partial_K):
    '''
    Adds the parity bits to our 56 bits key, to reach a 64 bits key.

    Args:
        partial_K (string) : The binary representation of the 56 bits key without 0b.

    Returns:
        string : The binay representation of the 64 bits key, without 0b.
    '''
    # Determination of the parity bits' values
    partial_K = list(partial_K)
    to_add = []
    sum_ = int(partial_K[0], 2)
    j = 1
    for i in range(1, 56):
        sum_ += int(partial_K[i], 2)
        j += 1
        if j == 7:
            j = 0
            if sum_ % 2 == 0:
                to_add.append('0')
            else:
                to_add.append('1')
            sum_ = 0
    
    
    # Adding the parity bits
    for i in [7, 15, 23, 31, 39, 47, 55, 63]:
        partial_K.insert(i, to_add[j])
        j += 1
    
    partial_K = "".join(partial_K)
    return partial_K


def rev_PC2(K16):
    '''
    Reverses the PC2 permutation applied to obtain K16.

    Args:
        K16 (string) : A string representing the binary value of K16 (without 0b).
    
    Returns:
        string : The binary string representing K16 after reversing PC2, with unknon bits marked with 'x'
        (and without 0b).
    '''
    K = ''
    pos_to_determine = [9, 18, 22, 25, 35, 38, 43, 54]  # The unknown bits posisitions after reversing PC2
    for i in range(56):
        if i + 1 not in pos_to_determine:
            K += K16[PC2.index(i + 1)]
        else:
            K+= 'x'
    return K


def rev_PC1(partial_K):
    '''
    Reverses the PC1 permutation.

    Args:
        partial_K (string) : The key value on 56 bits after PC1.
    
    Returns:
        string : the original key.
    '''
    K = ''
    for i in range(64):
        if (i + 1) % 8 != 0:                   # The parity bits are discarded in PC1
            K += partial_K[PC1.index(i + 1)]
    return K


def recover_K(K16):
    '''
    This function recovers the 64 bits master key value from the 48 bits of the 
    previously recovered K16.

    Args:
        K16 (string) : A string representing the binary value of K16 (without 0b).
    
    Returns:
        string : The binary representation of K (the master key) without the 0b.
    '''
    K = rev_PC2(K16)                                    # The master key we are reconstructing
    expected_output = 'E99D5D8CBF37F4DF'                # The correct plaintext
    
    # The parameters for the URL
    iv = '&iv=0000000000000000'
    input = '&input=B68222FAB437421A'                   # The correct ciphertext
    mode = '&mode=ecb'
    action = '&action=Decrypt'
    output = '&output='
    
    for i in range(256):
        key = replace_unknown_bits(K, i)
        key = rev_PC1(key)
        key = add_parity_bits(key)

        key = hex(int(key, 2))[2:].capitalize()
        url = "https://emvlab.org/descalc/?"      # The base URL to the DES calculator
        url += 'key=' + key + iv + input + mode + action + output   # The final request

        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        if expected_output == soup.find(id='output').getText():
            print("Key value retrieved : " + key)
            return
    
    print("No key value found")
        

begin = time.time()
recover_K(K16_recovery.K16_recovery())
end = time.time()
print(end - begin)