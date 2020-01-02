deg = float(input())

k_minutes = deg % 30 * 2
deg_per_minute = 360 / 60

print(k_minutes * deg_per_minute)