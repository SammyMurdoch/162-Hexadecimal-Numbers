def get_hex_count(d) -> int:
    return 15 * 16**(d-1) - 43 * 15**(d-1) + 41 * 14**(d-1) - 13 ** d

total = 0
max_digits = 16

for d in range(1, max_digits + 1):
    hex_count = get_hex_count(d)
    total += hex_count

hex_total = hex(total)

formatted_hex_total = "".join([c.upper() if not c.isdigit() else c for c in str(hex_total)[2:]])

print(f"Total in hex is: {formatted_hex_total}")
