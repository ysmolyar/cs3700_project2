def get_self_ip(addr):
    """
    Returns self IP given neighbor router IP by replacing last 8 bits with 1:
        'For the sake of simplicity, all of the neighboring routers will have IP addresses of the
        form *.*.*.2 and all of the IP addresses used by your router will be of the form *.*.*.1.'
    :param addr: address of neighboring router
    :return: address of port connected to neighboring router
    """
    return addr.rsplit('.', 1)[0] + '.1'


def addr_in_range(addr, prefix, mask):
    """
    Determines if the given addr is in the range spanned by the given prefix and subnet mask
    :param addr: IPv4 address
    :param prefix: address of network
    :param mask: subnet mask of network
    :return: True or False, if address is in network
    """
    addr_bin = addr_to_binary(addr)
    subnet_bin = get_subnet(prefix, mask)
    return addr_bin.startswith(subnet_bin) if subnet_bin != '' else False


def get_subnet(addr, mask):
    """
    Returns the binary string representation of the address subnet
    :param addr: IPv4 address
    :param mask: subnet mask
    :return: subnet bits of address
    """
    return addr_to_binary(addr)[:get_cidr_number(mask)]


def get_cidr_number(mask):
    """
    Returns CIDR address from subnet mask
    :param mask: subnet mask
    :return: CIDR number of mask
    """
    return addr_to_binary(mask).count('1')


def decrement_mask(mask):
    """
    Decrements mask by one bit. Used for coalescing forwarding table entries
    :param mask: subnet mask in X.X.X.X notation
    :return: decremented mask
    """
    idx = get_cidr_number(mask) - 1
    binary = addr_to_binary(mask)
    dec = binary[:idx] + '0' + binary[idx + 1:]

    return binary_to_addr(dec)


def addr_to_binary(addr):
    """
    Returns the binary string representation of the given IPv4 address
    :param addr: IPv4 address in X.X.X.X
    :return: binary representation of address
    """
    bins = addr.split('.')
    res = ""
    for b in bins:
        res += format(int(b), '08b')
    return res


def binary_to_addr(bin):
    """
    Converts binary string representation to decimal IPv4 address
    :param bin: binary string
    :return: IPv4 address in X.X.X.X notation
    """
    words = (bin[0 + i:8 + i] for i in range(0, len(bin), 8))
    res = ""
    for w in words:
        res += str(int(w, 2)) + '.'
    return res[:-1]
