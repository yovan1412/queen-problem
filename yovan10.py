import random
import time

# Mengecek apakah posisi aman untuk ratu
def is_safe(board, row, col, n):
    # Mengecek kolom
    for i in range(row):
        if board[i] == col:
            return False
    
    # Mengecek diagonal kiri atas
    for i, j in zip(range(row-1, -1, -1), range(col-1, -1, -1)):
        if board[i] == j:
            return False
    
    # Mengecek diagonal kanan atas
    for i, j in zip(range(row-1, -1, -1), range(col+1, n)):
        if board[i] == j:
            return False
    
    return True

# Fungsi untuk menampilkan papan
def print_board(board, n):
    for row in range(n):
        line = ['Q' if col == board[row] else '.' for col in range(n)]
        print(" ".join(line))
    print("\n" + "-"*20)

# Fungsi untuk game interaktif N-Queens
def play_n_queens(n, time_limit):
    board = [-1] * n  # Papan berukuran N, dengan -1 berarti belum ada ratu
    start_time = time.time()  # Mulai pengukuran waktu
    
    print("Permainan N-Queens dimulai!\n")
    print(f"Ukuran papan: {n}x{n}")
    
    # Menjalankan permainan selama belum menemukan solusi dan waktu belum habis
    for row in range(n):
        print(f"\nBaris {row + 1}: Pilih kolom untuk menempatkan ratu.")
        
        # Waktu yang tersisa
        remaining_time = time_limit - (time.time() - start_time)
        if remaining_time <= 0:
            print(f"\nWaktu habis! Anda gagal menyelesaikan permainan.")
            return
        
        print(f"Waktu tersisa: {remaining_time:.2f} detik.")
        
        # Menampilkan papan saat ini
        print_board(board, n)
        
        # Meminta input pemain untuk menempatkan ratu pada kolom yang valid
        while True:
            try:
                col = int(input(f"Masukkan kolom (0-{n-1}) untuk ratu di baris {row + 1}: "))
                if col < 0 or col >= n:
                    print(f"Kolom harus antara 0 dan {n-1}. Coba lagi.")
                elif not is_safe(board, row, col, n):
                    print("Posisi tidak aman, coba kolom lain!")
                else:
                    break  # Kolom valid dan aman, keluar dari loop
            except ValueError:
                print("Masukkan angka yang valid!")
        
        # Tempatkan ratu pada posisi yang aman
        board[row] = col
        
        # Cek jika sudah selesai (semua ratu telah ditempatkan)
        if row == n - 1:
            print("\nSelamat! Anda berhasil menyelesaikan N-Queens.")
            print_board(board, n)
            return

    # Jika pemain selesai tetapi waktu habis
    print("Permainan berakhir karena batas waktu tercapai.")
    print(f"Solusi sementara (bukan solusi optimal):")
    print_board(board, n)

def main():
    n = int(input("Masukkan ukuran papan (N): "))
    time_limit = float(input("Masukkan batas waktu (dalam detik): "))
    
    # Mulai permainan
    play_n_queens(n, time_limit)

if __name__ == "__main__":
    main()
