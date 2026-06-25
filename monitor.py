import subprocess

def get_price():
    cmd = 'cast call 0xC6962004f452bE9203591991D15f6b388e09E8D0 "slot0()(uint160,int24,uint16,uint16,uint16,uint8,bool)" --rpc-url https://arb1.arbitrum.io/rpc'
    result = subprocess.check_output(cmd, shell=True).decode().strip()

    # Mengambil bagian angka mentah saja (sebelum ada spasi)
    # result.split() akan memecah teks berdasarkan spasi, lalu kita ambil item pertama
    raw_val = result.split()[0]
    sqrt_price = int(raw_val)

    # Kalkulasi harga
    price = ((sqrt_price / 2**96)**2) * 1e12
    return price

print(f"Harga WETH/USDC saat ini: ${get_price():,.2f}")
