from ipaddress import ip_address


def int32_to_ip(int32):
    ip = ip_address(int32)
    return ip


print(int32_to_ip(2149583361))
print(int32_to_ip(32))
print(int32_to_ip(0))
print(int32_to_ip(2154959208))
