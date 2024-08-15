# Vehicle Detection and Counting System

## Deskripsi
Sistem ini mendeteksi dan menghitung kendaraan dalam video menggunakan model YOLOv8. Sistem ini dapat mendeteksi dan melabeli kendaraan seperti mobil dan bus, serta memberikan ID unik untuk setiap kendaraan yang terdeteksi.

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
   Unduh model `yolov8n.pt` dari [situs YOLOv8](https://github.com/ultralytics/yolov5) dan simpan di direktori yang sama dengan skrip.

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
- `requirements.txt`: Daftar dependensi Python yang diperlukan.
- `README.md`: Berkas ini berisi dokumentasi dan petunjuk penggunaan.

## Informasi Tambahan
- **Model YOLOv8**: Kami menggunakan model YOLOv8 untuk deteksi kendaraan. Pastikan model yang Anda unduh sesuai dengan versi yang digunakan.
- **ID Unik**: Setiap kendaraan diberi ID unik untuk identifikasi. ID ini ditampilkan bersama label kendaraan di video.

## Kontak
Jika Anda memiliki pertanyaan atau masalah, silakan hubungi [email@example.com].
