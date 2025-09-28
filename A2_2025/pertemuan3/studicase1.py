print("=" * 55)
print("         Wahana Roller Coaster Tornado Dufan")
print("=" * 55)

print("\nKamu harus mengisi data tinggi badan nantinya:")
print("-" * 45)

tinggi_badan = int(input("Masukkan tinggi badanmu: "))

if tinggi_badan >= 145:
    print("Kamu boleh naik Wahana Roller Coaster")

else:
    print("Kamu tidak boleh naik")

status = "Kamu boleh naik Wahana Roller Coaster" if tinggi_badan >= 145 else "Kamu tidak boleh naik"

print(status)