def addr_in_range(addr, prefix, mask):
    """Determines if the given addr is in the range spanned by the given prefix and subnet mask"""
    addr_bin = addr_to_binary(addr)
    print("ADDR_BIN: " + str(addr_bin) + "\n")
    cidr_bin = addr_to_binary(prefix)[:calculate_cidr_number(prefix, mask)]
    print("CIDR_BIN: " + str(cidr_bin) + "\n")
    return addr_bin.startswith(cidr_bin)


def calculate_cidr_number(addr, mask):
    """Returns CIDR address from IPv4 address and subnet mask"""
    return addr_to_binary(mask).count('1')


def addr_to_binary(addr):
    """Returns the binary string representation of the given IPv4 address, or prefix bits if CIDR address"""
    bins = addr.split('.')
    res = ""
    for b in bins:
        res += format(int(b), '08b')
    return res
