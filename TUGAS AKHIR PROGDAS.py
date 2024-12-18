import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

#Kelas Apikasi

class AplikasiNilaiMahasiswa:
    def __init__(self, root): #Konstruktor ini bertanggung jawab untuk menginisialisasi atribut objek, seperti pengaturan jendela
        self.root = root
        self.root.title("Aplikasi Perhitungan Nilai Mahasiswa")
        
        # Mengatur ukuran jendela dan memungkinkan perubahan ukuran
        self.root.geometry("700x600")  # Ukuran awal, lebih tinggi untuk menampung lebih banyak field
        self.root.state("normal")  # Memungkinkan jendela untuk diubah ukurannya
        self.root.configure(bg="#AFCBFF")
        
        # Memungkinkan jendela untuk diubah ukurannya di kedua arah (lebar dan tinggi)
        self.root.resizable(True, True)

        # Menyimpan daftar data mahasiswa
        self.data_mahasiswa_list = []

        self.input_page()

    #Fungsi untuk menampilkan halaman pertama, yaitu form untuk mengisi data mahasiswa (Nama, NIM, Mata Kuliah, dan nilai Tugas, UTS, UAS).

    def input_page(self): 
        """Halaman pertama untuk input nilai mahasiswa."""
        # Menghapus widget yang ada sebelumnya untuk menghindari tumpang tindih
        for widget in self.root.winfo_children():
            widget.destroy()

        # Label judul (di tengah)
        self.title_label = tk.Label(self.root, text="Aplikasi Perhitungan Nilai Mahasiswa", font=("Helvetica", 16), bg="lightblue")
        self.title_label.grid(row=0, column=0, columnspan=2, pady=10, sticky="n", padx=50)

        # Menetapkan ukuran kolom untuk semua Entry
        entry_width = 30  # Lebar kolom yang sama untuk semua entry fields

        # Label dan entry untuk Nama
        self.nama_label = tk.Label(self.root, text="Nama:", font=("Helvetica", 12), anchor="w", bg="lightblue")
        self.nama_label.grid(row=1, column=0, sticky="w", padx=(30, 10), pady=5)  # Menyesuaikan padding
        self.nama_entry = tk.Entry(self.root, font=("Helvetica", 12), bg="white", width=entry_width)
        self.nama_entry.grid(row=1, column=1, pady=5, padx=10)

        # Label dan entry untuk NIM
        self.nim_label = tk.Label(self.root, text="NIM:", font=("Helvetica", 12), anchor="w", bg="lightblue")
        self.nim_label.grid(row=2, column=0, sticky="w", padx=(30, 10), pady=5)  # Menyesuaikan padding
        self.nim_entry = tk.Entry(self.root, font=("Helvetica", 12), bg="white", width=entry_width)
        self.nim_entry.grid(row=2, column=1, pady=5, padx=10)

        # Label dan entry untuk Mata Kuliah
        self.prodi_label = tk.Label(self.root, text="Mata Kuliah:", font=("Helvetica", 12), anchor="w", bg="lightblue")
        self.prodi_label.grid(row=3, column=0, sticky="w", padx=(30, 10), pady=5)
        self.prodi_entry = tk.Entry(self.root, font=("Helvetica", 12), bg="white", width=entry_width)
        self.prodi_entry.grid(row=3, column=1, pady=5, padx=10)

        # Label dan entry untuk Nilai Tugas 1
        self.tugas1_label = tk.Label(self.root, text="Nilai Tugas 1:", font=("Helvetica", 12), anchor="w", bg="lightblue")
        self.tugas1_label.grid(row=4, column=0, sticky="w", padx=(30, 10), pady=5)
        self.tugas1_entry = tk.Entry(self.root, font=("Helvetica", 12), bg="white", width=entry_width)
        self.tugas1_entry.grid(row=4, column=1, pady=5, padx=10)

        # Label dan entry untuk Nilai Tugas 2
        self.tugas2_label = tk.Label(self.root, text="Nilai Tugas 2:", font=("Helvetica", 12), anchor="w", bg="lightblue")
        self.tugas2_label.grid(row=5, column=0, sticky="w", padx=(30, 10), pady=5)
        self.tugas2_entry = tk.Entry(self.root, font=("Helvetica", 12), bg="white", width=entry_width)
        self.tugas2_entry.grid(row=5, column=1, pady=5, padx=10)

        # Label dan entry untuk Nilai UTS
        self.uts_label = tk.Label(self.root, text="Nilai UTS:", font=("Helvetica", 12), anchor="w", bg="lightblue")
        self.uts_label.grid(row=6, column=0, sticky="w", padx=(30, 10), pady=5)
        self.uts_entry = tk.Entry(self.root, font=("Helvetica", 12), bg="white", width=entry_width)
        self.uts_entry.grid(row=6, column=1, pady=5, padx=10)

        # Label dan entry untuk Nilai UAS
        self.uas_label = tk.Label(self.root, text="Nilai UAS:", font=("Helvetica", 12), anchor="w", bg="lightblue")
        self.uas_label.grid(row=7, column=0, sticky="w", padx=(30, 10), pady=5)
        self.uas_entry = tk.Entry(self.root, font=("Helvetica", 12), bg="white", width=entry_width)
        self.uas_entry.grid(row=7, column=1, pady=5, padx=10)

        # Tombol untuk submit
        self.submit_button = tk.Button(self.root, text="Submit", font=("Helvetica", 12), bg="green", fg="white", command=self.submit_nilai)
        self.submit_button.grid(row=8, column=0, columnspan=2, pady=10, padx=50)

        # Tombol Next untuk pindah ke halaman hasil
        self.next_button = tk.Button(self.root, text="Next", font=("Helvetica", 12), bg="blue", fg="white", command=self.result_page)
        self.next_button.grid(row=9, column=0, columnspan=2, pady=10, padx=50)

        # Mengatur agar kolom dapat mengisi lebar yang tersedia
        self.root.grid_columnconfigure(0, weight=1)
        self.root.grid_columnconfigure(1, weight=3)  # Memperlebar kolom kedua untuk entri

        # Menyesuaikan tinggi baris
        for i in range(10):
            self.root.grid_rowconfigure(i, weight=0)

#Fungsi ini digunakan untuk mengambil data dari form input dan melakukan validasi.
    def submit_nilai(self):
        """Menyimpan nilai mata kuliah dan menghitung nilai."""
        try:
            # Mengambil data dari form input
            nama = self.nama_entry.get()
            nim = self.nim_entry.get()
            mata_kuliah = self.prodi_entry.get()
            tugas1 = self.tugas1_entry.get()
            tugas2 = self.tugas2_entry.get()
            uts = self.uts_entry.get()
            uas = self.uas_entry.get()

#Modul 2 pengkondisian IF
            # Mengecek jika ada input yang kosong
            if not nama or not nim or not mata_kuliah or not tugas1 or not tugas2 or not uts or not uas:
                messagebox.showerror("Input Error", "Semua data harus diisi!")
                return

            # Mengecek jika NIM bukan angka
            if not nim.isdigit():
                messagebox.showerror("Input Error", "NIM harus berupa angka!")
                return

            # Mengonversi nilai tugas, uts, dan uas menjadi angka
            try:
                tugas1 = float(tugas1)
                tugas2 = float(tugas2)
                uts = float(uts)
                uas = float(uas)
                
                # Memastikan nilai berada dalam rentang 0-100
                if not (0 <= tugas1 <= 100 and 0 <= tugas2 <= 100 and 0 <= uts <= 100 and 0 <= uas <= 100):
                    messagebox.showerror("Input Error", "Masukkan nilai yang valid (0-100)!")
                    return
            except ValueError:
                messagebox.showerror("Input Error", "Masukkan nilai yang valid (0-100)!")
                return

            # Menghitung rata-rata nilai
            rata_rata = (tugas1 + tugas2 + uts + uas) / 4

#Pengkondisian if else
            # Menentukan predikat berdasarkan rata-rata
            if rata_rata >= 85:
                predikat = "A"
            elif rata_rata >= 70:
                predikat = "B"
            elif rata_rata >= 55:
                predikat = "C"
            elif rata_rata >= 40:
                predikat = "D"
            else:
                predikat = "E"

            # Menyimpan data mahasiswa
            mahasiswa_data = (nama, nim, mata_kuliah, tugas1, tugas2, uts, uas, rata_rata, predikat)
            self.data_mahasiswa_list.append(mahasiswa_data)

            messagebox.showinfo("Success", "Data berhasil disubmit!")

            # Mengosongkan entry fields
            self.clear_entries()

        except Exception as e:
            messagebox.showerror("Error", str(e))

#Fungsi ini digunakan untuk menampilkan halaman kedua yang berisi tabel hasil (data mahasiswa yang sudah diinput).

    def result_page(self):
        """Halaman kedua untuk menampilkan hasil."""
        # Menghapus widget sebelumnya
        for widget in self.root.winfo_children():
            widget.destroy() #Menghapus semua widget dari jendela utama (root) sebelum menampilkan halaman baru. 

        self.title_label = tk.Label(self.root, text="Data Mahasiswa", font=("Helvetica", 16), bg="lightblue")
        self.title_label.grid(row=0, column=0, columnspan=2, pady=10)

        # Menampilkan tabel hasil
        self.tree = ttk.Treeview(self.root, columns=("Nama", "NIM", "Mata Kuliah", "Tugas 1", "Tugas 2", "UTS", "UAS", "Rata-rata", "Predikat"), show="headings")

        for col in self.tree["columns"]:
            self.tree.heading(col, text=col)

        for data in self.data_mahasiswa_list:
            self.tree.insert("", "end", values=data)

        self.tree.grid(row=1, column=0, columnspan=2, pady=10, padx=20)

        # Tombol kembali ke input form
        self.back_button = tk.Button(self.root, text="Back", font=("Helvetica", 12), bg="blue", fg="white", command=self.input_page)
        self.back_button.grid(row=2, column=0, columnspan=2, pady=10)

        # Tombol reset untuk menghapus history
        self.reset_button = tk.Button(self.root, text="Reset", font=("Helvetica", 12), bg="red", fg="white", command=self.reset_data)
        self.reset_button.grid(row=3, column=0, columnspan=2, pady=10)

#Fungsi ini digunakan untuk menghapus seluruh data mahasiswa yang tersimpan di dalam data_mahasiswa_list dan mengosongkan tabel pada halaman hasil.
    def reset_data(self):
        """Menghapus semua data mahasiswa dan menyegarkan tabel."""
        self.data_mahasiswa_list.clear()  # Menghapus data mahasiswa
        self.tree.delete(*self.tree.get_children())  # Menghapus semua baris dalam tabel
        messagebox.showinfo("Reset", "History data telah dihapus!") #Memanggi untuk memberikan informasi bahwa data telah direset.

    def clear_entries(self):
        """Mengosongkan semua field input."""
        self.nama_entry.delete(0, tk.END)
        self.nim_entry.delete(0, tk.END)
        self.prodi_entry.delete(0, tk.END)
        self.tugas1_entry.delete(0, tk.END)
        self.tugas2_entry.delete(0, tk.END)
        self.uts_entry.delete(0, tk.END)
        self.uas_entry.delete(0, tk.END)

# Menjalankan aplikasi
if __name__ == "__main__":
    root = tk.Tk()
    app = AplikasiNilaiMahasiswa(root)
    root.mainloop()
