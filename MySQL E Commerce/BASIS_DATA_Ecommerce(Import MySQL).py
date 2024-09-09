import mysql.connector
from mysql.connector import Error

try:
    conn = mysql.connector.connect(
        host="localhost",
        user="root",  
        password="1234"  
    )

    cursor = conn.cursor()
    cursor.execute("CREATE DATABASE IF NOT EXISTS ecommerce_db")
    conn.commit()
    print("Database 'ecommerce_db' created successfully!")

finally:
    if conn.is_connected():
        cursor.close()
        conn.close()
        print("MySQL connection is closed.")

try:
    conn = mysql.connector.connect(
        host="localhost",
        user="root",  
        password="1234", 
        database="ecommerce_db"  
    )
    
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Pengguna (
        id_pengguna INT AUTO_INCREMENT PRIMARY KEY,
        nama VARCHAR(255),
        email VARCHAR(255) UNIQUE,
        kata_sandi VARCHAR(255),
        alamat VARCHAR(255),
        nomor_telepon VARCHAR(15),
        tanggal_bergabung DATE
    )
    ''')
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Penjual (
        id_penjual INT AUTO_INCREMENT PRIMARY KEY,
        id_pengguna INT UNIQUE,
        nama_toko VARCHAR(255),
        alamat_toko VARCHAR(255),
        tanggal_bergabung DATE,
        FOREIGN KEY (id_pengguna) REFERENCES Pengguna(id_pengguna) ON DELETE CASCADE
    )
    ''')
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Produk (
        id_produk INT AUTO_INCREMENT PRIMARY KEY,
        nama_produk VARCHAR(255),
        deskripsi_produk TEXT,
        harga DECIMAL(10, 2),
        stok INT,
        kategori VARCHAR(255),
        id_penjual INT,
        FOREIGN KEY (id_penjual) REFERENCES Penjual(id_penjual) ON DELETE CASCADE
    )
    ''')
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Transaksi (
        id_transaksi INT AUTO_INCREMENT PRIMARY KEY,
        id_pengguna INT,
        total_harga DECIMAL(10, 2),
        status_transaksi VARCHAR(50),
        tanggal_transaksi DATE,
        FOREIGN KEY (id_pengguna) REFERENCES Pengguna(id_pengguna) ON DELETE CASCADE
    )
    ''')
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Pembayaran (
        id_pembayaran INT AUTO_INCREMENT PRIMARY KEY,
        id_transaksi INT UNIQUE,
        metode_pembayaran VARCHAR(255),
        status_pembayaran VARCHAR(50),
        tanggal_pembayaran DATE,
        FOREIGN KEY (id_transaksi) REFERENCES Transaksi(id_transaksi) ON DELETE CASCADE
    )
    ''')
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS DetailTransaksi (
        id_detail_transaksi INT AUTO_INCREMENT PRIMARY KEY,
        id_transaksi INT,
        id_produk INT,
        kuantitas INT,
        harga_satuan DECIMAL(10, 2),
        subtotal DECIMAL(10, 2),
        FOREIGN KEY (id_transaksi) REFERENCES Transaksi(id_transaksi) ON DELETE CASCADE,
        FOREIGN KEY (id_produk) REFERENCES Produk(id_produk) ON DELETE CASCADE
    )
    ''')
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS UlasanProduk (
        id_ulasan INT AUTO_INCREMENT PRIMARY KEY,
        id_pengguna INT,
        id_produk INT,
        rating INT,
        komentar TEXT,
        tanggal_ulasan DATE,
        FOREIGN KEY (id_pengguna) REFERENCES Pengguna(id_pengguna) ON DELETE CASCADE,
        FOREIGN KEY (id_produk) REFERENCES Produk(id_produk) ON DELETE CASCADE
    )
    ''')
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Keranjang (
        id_keranjang INT AUTO_INCREMENT PRIMARY KEY,
        id_pengguna INT UNIQUE,
        total_item INT,
        total_harga DECIMAL(10, 2),
        FOREIGN KEY (id_pengguna) REFERENCES Pengguna(id_pengguna) ON DELETE CASCADE
    )
    ''')
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS ItemKeranjang (
        id_item_keranjang INT AUTO_INCREMENT PRIMARY KEY,
        id_keranjang INT,
        id_produk INT,
        kuantitas INT,
        FOREIGN KEY (id_keranjang) REFERENCES Keranjang(id_keranjang) ON DELETE CASCADE,
        FOREIGN KEY (id_produk) REFERENCES Produk(id_produk) ON DELETE CASCADE
    )
    ''')
    conn.commit()

    print("Tables created successfully in 'ecommerce_db'!")

except mysql.connector.Error as err:
    print(f"Error: {err}")

finally:
    if conn.is_connected():
        cursor.close()
        conn.close()
        print("MySQL connection is closed.")
