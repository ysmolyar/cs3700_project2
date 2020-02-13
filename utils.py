def get_self_ip(addr):
    """
    Returns self IP given neighbor router IP by replacing last 8 bits with 1:
        'For the sake of simplicity, all of the neighboring routers will have IP addresses of the
        form *.*.*.2 and all of the IP addresses used by your router will be of the form *.*.*.1.'
    """
    return addr.rsplit('.', 1)[0] + '.1'


def addr_in_range(addr, prefix, mask):
    """Determines if the given addr is in the range spanned by the given prefix and subnet mask"""
    addr_bin = addr_to_binary(addr)
    cidr_bin = addr_to_binary(prefix)[:calculate_cidr_number(prefix, mask)]
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
