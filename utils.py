
# The message in plaintext
plaintext = hex(0xE99D5D8CBF37F4DF)

# The correct ciphertext
cipher_corr = hex(0xB68222FAB437421A)

# The faulted ciphertexts
cipher_fault = [ 
    hex(0xB49322BAB436421E), 
    hex(0xB69022FEB436421A),
    hex(0xB68220BAB436421A),
    hex(0xB79226B8A437421A), 
    hex(0xB79222BAA636421A),
    hex(0xB7C222FAA435421A),
    hex(0xB6C226FAA437401A),
    hex(0xB7C226FBA4334218),
    hex(0xBF8222FBA427421A),
    hex(0xB68A22FAF427421A),
    hex(0xB6822AFAF433421A),
    hex(0xB68232F2B463421B),
    hex(0xB68232FBFC77421A),
    hex(0xF68232FAB47F421A),
    hex(0xF68222FAB4374A1B),
    hex(0xF68232FAB0374253),
    hex(0x968222FAB077425B),
    hex(0xB6A222FAB037435A),
    hex(0xB68202FAB037525A),
    hex(0xA68263DAB037535A),
    hex(0xA68263FA9037525A),
    hex(0xA28223FAB417421A),
    hex(0xB28263FAB437621A),
    hex(0xB28262EAB537423A),
    hex(0x268263EAB537021A),
    hex(0xB60222EAB537061A),
    hex(0xB682A2EAB437021A),
    hex(0xB683227AB537020A),
    hex(0xB68322EA3537060E),
    hex(0xB68322FAB4B7421E),
    hex(0xB68722FAB437C21A),
    hex(0xB68222BEB436428E)
]

# DES Initial permutation table
IP = [
    58, 50, 42, 34, 26, 18, 10, 2,
    60, 52, 44, 36, 28, 20, 12, 4,
    62, 54, 46, 38, 30, 22, 14, 6,
    64, 56, 48, 40, 32, 24, 16, 8,
    57, 49, 41, 33, 25, 17, 9, 1,
    59, 51, 43, 35, 27, 19, 11, 3,
    61, 53, 45, 37, 29, 21, 13, 5,
    63, 55, 47, 39, 31, 23, 15, 7
]


# DES Expansion table
E = [
    32, 1, 2, 3, 4, 5,
    4, 5, 6, 7, 8, 9,
    8, 9, 10, 11, 12, 13,
    12, 13, 14, 15, 16, 17,
    16, 17, 18, 19, 20, 21,
    20, 21, 22, 23, 24, 25,
    24, 25, 26, 27, 28, 29,
    28, 29, 30, 31, 32, 1
]

# DES F function's permutation table
P = [
    16, 7, 20, 21,
    29, 12, 28, 17,
    1, 15, 23, 26,
    5, 18, 31, 10,
    2, 8, 24, 14,
    32, 27, 3, 9,
    19, 13, 30, 6,
    22, 11, 4, 25
]

# The reverse permutation of P
rev_P = [
    9, 17, 23, 31,
    13, 28, 2, 18,
    24, 16, 30, 6,
    26, 20, 10, 1,
    8, 14, 25, 3,
    4, 29, 11, 19,
    32, 12, 22, 7,
    5, 27, 15, 21
]

# DES Sbox S1
S1 = [
    [14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
    [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
    [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
    [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13]
]

# DES Sbox S2
S2 = [
    [15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
    [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
    [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
    [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9]
]

# DES Sbox S3
S3 = [
    [10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],
    [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
    [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],
    [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12]
]

# DES Sbox S4
S4 = [
    [7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
    [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
    [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],
    [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14]
]

# DES Sbox S5
S5 = [
    [2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
    [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
    [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
    [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3]
]

# DES Sbox S6
S6 = [
    [12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],
    [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],
    [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],
    [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13]
]

# DES Sbox S7
S7 = [
    [4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
    [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
    [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],
    [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12]
]

# DES Sbox S8
S8 = [
    [13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],
    [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
    [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],
    [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11]
]



def expand(r):
    '''
    DES expansion function contained in F function.

    Args:
        r (hex) : The hexadecimal value of the right register.
    
    Raises:
        Exception : If the hexadecimal value given in parameter is not a 32 bits value.

    Returns:
        string : A string representing the expanded value of r in binary (without the 0b).
    '''
    if len(r) != 10:
        raise Exception('The parameter value must be a 32 bits integer. Given one was a ' + str((len(r) - 2) * 4) + ' bits parameter.')

    tmp = bin(int(r, 16))[2:].zfill(32) # Converts the hexadecimal parameter r in a string representing its binary value
    res = ''
    for bit in E:
        res += tmp[bit - 1]
    return res


def xor(a, b):
    '''
    Make the xor operation between two same length integer.

    Args:
        a (string) : A string representing an integer in binary (without the 0b).
        b (string) : A string representing an integer in binary (without the 0b).

    Raises:
        Exception : If the parameters have different sizes.

    Returns:
        string : A string representing the xor value of the two arguments in binary (without the 0b).
    '''
    if len(a) != len(b):
        raise Exception('The two parameters must have the same bit size. First was : ' + str(len(a)) + ' bits. Second was : ' + str(len(b)) + ' bits.')

    res = bin(int(a, 2) ^ int(b, 2))[2:].zfill(len(a))
    return res


def initial_permutation(cipher):
    '''
    Applies the initial permutation IP function to the ciphertext.

    Args:
        cipher (hex) : The ciphertext in hexadecimal.

    Raises:
        Exception : If the cipher parameter is not a 64 bits integer.

    Returns:
        string : A string representing the result of the permutation in binary.
    '''
    if len(cipher) != 18:
        raise Exception('The ciphertext must be a 64 bits integer. Provided was a ' + str((len(cipher) - 2) * 4) + ' bits integer.')

    res = ''
    bin_cipher = bin(int(cipher, 16))[2:].zfill(48)
    for bit in IP:
        res += bin_cipher[bit - 1]
    return res


def perm(val):
    '''
    Permutates the bits of the integer in parameter according to P table (in DES F function).

    Args:
        val (string) : A string representing the binary value of an 32 bits integer (without the 0b).

    Raises:
        Exception : If the parameter is not a 32 bits integer.
    
    Returns:
        string : The result of the operation in the binary form (without 0b).
    '''
    if len(val) != 32:
        raise Exception('The parameter must represent a 32 bits integer. Provided represented a ' + str(len(val)) + ' bits integer.')

    res = ''
    for bit in P:
        res += val[bit - 1]
    return res


def rev_perm(val):
    '''
    Reverse the permutation P in DES F function.

    Args:
        val (string) : A string representing the binary value of an 32 bits integer (without the 0b).
    
    Raises:
        Exception : If the parameter is not a 32 bits integer.
    
    Returns:
        string : The result of the operation in the binary form (without 0b).
    '''
    if len(val) != 32:
        raise Exception('The parameter must represent a 32 bits integer. Provided represented a ' + str(len(val)) + ' bits integer.')
    
    res = ''
    for bit in rev_P:
        res += val[bit - 1]
    return res


def initial_perm(cipher):
    '''
    Calculates the initial permutation with the IP table.

    Args:
        cipher (string) : A string representing a 64 bits integer value in binary (without 0b).
    
    Raises:
        Exception : If the parameter is not a 64 bits value.

    Returns:
        string : The permuted provided string.
    '''
    if len(cipher) != 64:
        raise Exception('The parameter must be a 64 bits value. Provided was a ' + str(len(cipher) - 2) * 4 + ' bits value.')
    
    res = ''
    for bit in IP:
        res += cipher[bit - 1]
    return res


def get_R16_L16(cipher):
    '''
    Returns the content of the R16 and L16 registers.

    Args:
        cipher (hex) : The final ciphertext in hexadecimal.

    Raises:
        Exception : If the parameter is not a 64 bits integer.

    Returns:
        string, string : Strings representing the binary content of the R16 and L16 registers.
    '''
    if (len(cipher) - 2) * 4 != 64:
        raise Exception('The parameter must be a 64 bits hexadecimal value. Provided was a ' + str(len(cipher) - 2) * 4 + ' bits value.')

    bin_cipher = bin(int(cipher, 16))[2:].zfill(32)

    rev = initial_perm(bin_cipher)
    R16 = rev[:32]
    L16 = rev[32:64]
    return R16, L16


def calculate_S(SBox, input):
    '''
    Calculates the output of an Sbox.

    Args:
        Sbox (int[]) : The DES Sbox table to use.
        input (string) : A string representing a 6 bits integer in binary (without the 0b).

    Raises:
        Exception : If the input does not represent a 6 bits integer.

    Returns:
        string : A string representing the binary value obtained when applying the input to the Sbox.
    '''
    if len(input) != 6:
        raise Exception('The parameter must be a 6 bits integer. Provided was a ' + str(len(input)) + ' bits value.')
    
    row = 2 * int(input[0], 2) + int(input[5], 2)
    col = int(input[1:5], 2)
    return bin(SBox[row][col])[2:].zfill(4)


def exhaustive_attack_sbox(Sbox, input, expected):
    '''
    Performs an exhaustive search of the possible K16 bits associated to the Sbox.

    Args:
        Sbox(int[]) : The Sbox we are attacking.
        input (string) : The 6 bits input of the Sbox (must correspond to E(R15))
        expected (string) : The expected output of the Sbox.
    
    Raises:
        Exception : If input is not a 6 bits integer or expected is not a 4 bits integer.

    Returns:
        string[] : The list of possible K16 portions.
    '''
    if len(input) != 6:
        raise Exception('The parameter must be a 6 bits integer. Provided was a ' + str(len(input)) + ' bits value.')
    if len(expected) != 4:
        raise Exception('The parameter must be a 4 bits integer. Provided was a ' + str(len(input)) + ' bits value.')
    
    res = []
    for i in range(16):
        bin_i = bin(i)[2:].zfill(6)
        out = calculate_S(Sbox, xor(input, bin_i))
        if out == expected:
            res.append(bin_i)
    
    return res