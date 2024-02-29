def hitung_total(menu, jumlah):
product = {
    'caffe americano': 37000,
    'caramel macchiato': 59000,
    'asian dolce latte': 55000,
    'caramel latte': 52000,
    'vanilla latte': 52000,
    'caffe latte': 48000,
    'cappuccino': 48000,
    'caffe mocha': 55000
}

def belanja():
    print("selamat datang, selamat berbelanja")
    print("Berikut adalah daftar barang yang tersedia:")
    for barang, harga in product.items():
        print(f"{barang}: Rp {harga} per unit")
      
    total_belanja = jumlah * product[menu]
    total_bayar = hitung_total(menu, jumlah)
    while True:
        barang_dipilih = input("Masukkan nama barang yang ingin anda beli(atau 'selesai' untuk selesai)")
        if barang_dipilih.lower() == 'selesai' :
            break
        if barang_dipilih not in product:
            print("Maaf, barang tersebut tidak tersedia")
            continue
        jumlah = float(input(f"berapa {barang_dipilih} yang anda inginkan?"))
        total_belanja += product[barang_dipilih] * jumlah
    print(f"total belanja anda adalah: Rp{total_belanja}")
    
    total_harga = jumlah * product[menu]
    
    total_harga = jumlah * product[menu]
    
    if total_harga > 350000:
        diskon = total_harga * 0.15
        total_harga -= diskon
    
    ppn = total_harga * 0.10
    total_bayar = total_harga + ppn
    
    return total_bayar
    print(f"Selamat anda mendapatkan diskon sebesar 15% karena telah melakukan transaksi diatas Rp350.000")
belanja() 