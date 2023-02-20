def number_cutter(xp_received):
    max_numer = 100
    current = 0
    current += xp_received
    if current >= max_numer:
        excessive = current - max_numer
        # Level up here
        current = excessive
        print(current)

number_cutter(10)