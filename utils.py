def addr_in_range(addr, prefix, mask):
    """Determines if the given addr is in the range spanned by the given prefix and subnet mask"""
    addr_bin = addr_to_binary(addr)
    cidr_bin = addr_to_binary(calculate_cidr(prefix, mask))
    return addr_bin.startswith(cidr_bin)


def calculate_cidr(addr, mask):
    """Returns CIDR address from IPv4 address and subnet mask"""
    return addr + '/' + str(addr_to_binary(mask).count('1'))


def addr_to_binary(addr):
    """Returns the binary string representation of the given IPv4 address, or prefix bits if CIDR address"""
    binary = '{0:08b}{1:08b}{2:08b}{3:08b}'.format(*addr.split('.'))
    subnet = int(addr.split('/')[1]) if '/' in addr else None
    return binary[:subnet] if subnet else binary
