stadium_capacity = int(input())
fans_count = int(input())

sector_a_fans = 0
sector_b_fans = 0
sector_v_fans = 0
sector_g_fans = 0

for i in range(fans_count):
    sector = str(input())

    if sector == 'A':
        sector_a_fans += 1
    elif sector == 'B':
        sector_b_fans += 1
    elif sector == 'V':
        sector_v_fans += 1
    elif sector == 'G':
        sector_g_fans += 1

p1 = (sector_a_fans / fans_count) * 100
p2 = (sector_b_fans / fans_count) * 100
p3 = (sector_v_fans / fans_count) * 100
p4 = (sector_g_fans / fans_count) * 100
p5 = (fans_count / stadium_capacity) * 100

print(f"""{p1:.2f}%
{p2:.2f}%
{p3:.2f}%
{p4:.2f}%
{p5:.2f}%""")