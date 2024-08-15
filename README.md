# Vehicle Detection and Counting System

## Diri Saya
**Nama**: Bagas Dwi Santosa

**Email**: bagasdwisantosa87@gmail.com

**Asal Universitas**: Universitas Jenderal Achmad Yani Yogyakarta


## Deskripsi
Sistem ini adalah proyek dari **AI Engineer Intern Knowledge Test**. Sistem ini mendeteksi dan menghitung kendaraan dalam video menggunakan model YOLOv8. Sistem ini dapat mendeteksi dan melabeli kendaraan seperti mobil dan bus, serta memberikan ID unik untuk setiap kendaraan yang terdeteksi.

Kode ini dibuat berdasarkan berbagai referensi dari AI GPT, GitHub, dan sumber lainnya. Harap dicatat bahwa saya masih pemula dalam pengembangan sistem ini, sehingga beberapa aspek dari implementasi mungkin belum sepenuhnya optimal.

## Hasil & Problem
- **Berhasil Membaca File Video Input (`toll_gate.mp4`)**: Sistem dapat membuka dan membaca file video input dengan benar.
- **Berhasil Mendeteksi Kendaraan Mobil dan Bus**: Kendaraan yang terdeteksi diidentifikasi sebagai mobil dan bus sesuai dengan model YOLOv8.
- **Menampilkan Perhitungan Jumlah Kendaraan**: Sistem menampilkan perhitungan jumlah kendaraan pada setiap frame. Namun, perhitungan ini hanya dilakukan per frame, sehingga hasil total belum sesuai dengan jumlah kendaraan yang sebenarnya.
- **Berhasil Menampilkan ID Unik**: ID unik ditampilkan untuk setiap kendaraan, tetapi ID ini direset pada setiap frame, sehingga hasil total ID tidak akurat.
- **Berhasil Visualisasi Perhitungan Jumlah Kendaraan**: Jumlah kendaraan yang terdeteksi ditampilkan secara visual pada video output.
- **Berhasil Output Video**: Video output dengan anotasi yang benar-benar berhasil disimpan.


## Prasyarat
Sebelum menjalankan sistem, pastikan Anda memiliki perangkat lunak dan pustaka berikut:
- Python 3.x
- OpenCV
- Ultralytics YOLO

## Instalasi
1. **Kloning repositori ini:**
    ```bash
    git clone <URL_REPOSITORI>
    cd <NAMA_REPOSITORI>
    ```

2. **Buat dan aktifkan lingkungan virtual (opsional tetapi disarankan):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # Di Windows: venv\Scripts\activate
    ```

3. **Instal dependensi yang diperlukan:**
    ```bash
    pip install -r requirements.txt
    ```

4. **Unduh model YOLOv8:**
   Unduh model `yolov8n.pt` dari ([situs YOLOv8](https://github.com/ultralytics/ultralytics)) dan simpan di direktori yang sama dengan skrip.

## Cara Menjalankan Sistem
1. **Siapkan video input dan tentukan jalur output.**

2. **Edit jalur video input dan output di skrip Python (`vehicle_detection.py`):**
    Buka berkas `vehicle_detection.py` dan sesuaikan variabel `video_path` dan `output_path` dengan jalur file video Anda.

    ```python
    if __name__ == "__main__":
        video_path = 'path/to/your/video.mp4'  # Ganti dengan jalur video input Anda
        output_path = 'path/to/output/video.mp4'  # Ganti dengan jalur video output yang diinginkan
        detect_and_display_video(video_path, output_path)
    ```

3. **Jalankan skrip utama:**
    ```bash
    python vehicle_detection.py
    ```

## Struktur Repositori
- `vehicle_detection.py`: Skrip utama untuk mendeteksi dan menghitung kendaraan.
- `vehicle_detection.ipynb`: Skrip ipynb untuk mendeteksi dan menghitung kendaraan.
- `requirements.txt`: Daftar dependensi Python yang diperlukan.
- `README.md`: Berkas ini berisi dokumentasi dan petunjuk penggunaan.
- `toll_gate.mp4`: Berkas video input.
- `output_toll_gate.mp4`: Berkas video output.

## Informasi Tambahan
- **Model YOLOv8**: Menggunakan model YOLOv8 untuk deteksi kendaraan. Pastikan model yang Anda unduh sesuai dengan versi yang digunakan.
- **ID Unik**: Setiap kendaraan diberi ID unik untuk identifikasi. ID ini ditampilkan bersama label kendaraan di video.
