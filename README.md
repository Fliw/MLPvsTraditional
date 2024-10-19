
# Introduction to Neural Network of MLP
![image](https://github.com/user-attachments/assets/6ef61f26-5f9d-4e1a-9cbb-b15a73f24726)

## Deskripsi
Dokumen ini menjelaskan cara membuat dan menjalankan model Multi-Layer Perceptron (MLP) menggunakan TensorFlow untuk memprediksi angka berdasarkan rumus matematis sederhana.

## Rumus
Model ini menggunakan rumus matematis sederhana untuk membandingkan antara AI dalam menentukan rumus dengan traditional programming yang sudah mempunyai rule, berikut rumusnya:
``
y = 2 * x
``
di mana:
- \( x \) adalah input dari pengguna
- \( y \) adalah output yang diprediksi

## Cara Kerja
1. **Menyiapkan Data**: 
   - Data input adalah deretan angka dari 1 hingga 10.
   - Output dihasilkan dengan mengalikan input dengan 2.

2. **Membangun Model**:
   - Model MLP dibangun menggunakan Keras dengan satu lapisan tersembunyi yang memiliki 64 neuron dan fungsi aktivasi ReLU.
   - Lapisan output memiliki satu neuron untuk memprediksi output.

3. **Melatih Model**:
   - Model dilatih menggunakan optimasi Adam dan fungsi loss mean squared error (MSE) selama 250 epoch.
   - Validasi dilakukan dengan membagi data pelatihan menjadi 80% untuk pelatihan dan 20% untuk validasi.

4. **Prediksi**:
   - Setelah pelatihan, pengguna dapat memasukkan angka untuk mendapatkan prediksi dari model MLP.
   - Program juga menyediakan metode tradisional untuk membandingkan hasil.
   - Selain Metode Tradisional, Program juga membuat nilai selisih antara MLP vs Traditional

## Cara Setup Lingkungan

### 1. Instalasi Python dan Virtual Environment
Pastikan Python telah terinstal. Buat virtual environment dengan perintah:
```bash
python -m venv venv
```

### 2. Aktivasi Virtual Environment
- Di Windows:
    ```bash
    venv\Scripts\activate
    ```
- Di macOS/Linux:
    ```bash
    source venv/bin/activate
    ```

### 3. Instalasi TensorFlow
Instal TensorFlow menggunakan pip:
```bash
pip install tensorflow
```

### 4. Menjalankan Kode
jalankan program dengan perintah berikut:
```bash
python mlp.py
```

## Hasil
Program akan meminta input dari pengguna dan memberikan output berdasarkan prediksi model MLP serta perhitungan tradisional. Pengguna dapat mengetik 'exit' untuk keluar dari program.

## Kesimpulan
Model ini belajar dari data yang kita berikan, sehingga dapat memberikan prediksi yang lebih akurat untuk data baru. Dengan membandingkan hasil prediksi dari model dengan hasil yang dihitung menggunakan rumus sederhana, kita bisa memahami seberapa baik model bekerja. Ini penting untuk belajar AI karena memberikan dasar pembelajaran mesin yang praktis dan mudah, serta memungkinkan kita untuk bereksperimen dengan pengaturan yang berbeda guna memahami cara kerja jaringan saraf, sambil menghindari kesalahan dengan memisahkan data latih dan data uji.

## Catatan
- Disarankan untuk menggunakan virtual environment agar proyek Anda terisolasi dari instalasi Python lainnya.
- Selalu pastikan untuk menangani input pengguna agar tidak terjadi kesalahan.

Dengan mengikuti panduan ini, Anda dapat berhasil mengatur dan menjalankan model MLP dalam lingkungan lokal Python Anda.
