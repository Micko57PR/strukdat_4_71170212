import json

brngbaru = int(input("Masukkan jumlah barang : "))

daftarbarang = []

total = 0

for i in range(brngbaru):
    n = i+1
    nm = str(input(f'Nama Barang {n} = '))
    hrg = int(input(f'Harga Barang {n} = '))

    daftarbarang.append({
        "nama": nm,
        "harga": hrg
    })

    total = total + hrg

    print("\n")

struk = dict({
    "total": total,
    "barang": daftarbarang
})

with open('barangbelanja.json', 'w') as datafile:
    json.dump(struk, datafile)

print('data sudah diisi')
