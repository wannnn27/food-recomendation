# Food Recommendation System 

[![Hugging Face Spaces](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Spaces-blue)](https://huggingface.co/spaces/arwnsyh/food-recommendation-system)
[![Python](https://img.shields.io/badge/Python-3.9+-yellow)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

Sistem rekomendasi makanan berbasis AI yang membantu pengguna memilih makanan berdasarkan berat badan dan tujuan diet (Diet, Bulking, Muscle Gain, Maintain). Menggunakan algoritma **Random Forest Classifier** yang telah dilatih dengan dataset nutrisi untuk memberikan rekomendasi yang akurat.

## Fitur
- **Rekomendasi Personal**: Menghitung kebutuhan kalori harian berdasarkan berat badan.
- **Klasifikasi Cerdas**: Menggunakan Machine Learning untuk mengkategorikan makanan (High Protein, Low Calorie, dsb).
- **Antarmuka Intuitif**: Menggunakan Gradio untuk tampilan yang mudah digunakan.

## Live Demo
Coba aplikasi langsung di browser Anda:  
 **[Sistem Rekomendasi Makanan di Hugging Face](https://huggingface.co/spaces/arwnsyh/food-recommendation-system)**

## Instalasi Lokal

Jika Anda ingin menjalankan proyek ini di komputer Anda sendiri:

1.  **Clone repository**
    ```bash
    git clone https://github.com/USERNAME/food-recommendation-system.git
    cd food-recommendation-system
    ```

2.  **Install dependencies**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Jalankan aplikasi**
    ```bash
    python app.py
    ```
4.  Buka browser di `http://localhost:7860`

## Struktur File
- `app.py`: Kode utama aplikasi (Gradio Interface + Logika Rekomendasi).
- `train_improvement.py`: Script untuk melatih model Random Forest (opsional, jika ingin train ulang).
- `food_recommendation.ipynb`: Notebook Jupyter untuk analisis data & eksperimen.
- `rf_model.pkl`: Model AI yang sudah dilatih (disimpan dengan joblib).
- `labeled_nutrition_data.csv`: Dataset nutrisi yang sudah dilabeli.
- `requirements.txt`: Daftar pustaka Python yang dibutuhkan.
- `Dockerfile`: Konfigurasi untuk deployment dengan Docker.

## Teknologi
- **Python** (Core Logic)
- **Scikit-Learn** (Random Forest Model)
- **Pandas** (Data Processing)
- **Gradio** (Web UI)

## Lisensi
Project ini dilisensikan di bawah [MIT License](LICENSE).
