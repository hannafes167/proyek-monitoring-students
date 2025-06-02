# Proyek Akhir: Menyelesaikan Permasalahan Perusahaan Edutech

## Business Understanding
Jaya Jaya Institut merupakan salah satu institusi pendidikan perguruan yang telah berdiri sejak tahun 2000. Hingga saat ini ia telah mencetak banyak lulusan dengan reputasi yang sangat baik. Akan tetapi, terdapat banyak juga siswa yang tidak menyelesaikan pendidikannya alias dropout.

Jumlah dropout yang tinggi ini tentunya menjadi salah satu masalah yang besar untuk sebuah institusi pendidikan. Oleh karena itu, Jaya Jaya Institut ingin mendeteksi secepat mungkin siswa yang mungkin akan melakukan dropout sehingga dapat diberi bimbingan khusus.

### Permasalahan Bisnis
1. Tingginya tingkat mahasiswa yang tidak menyelesaikan studi (dropout) berdampak pada reputasi institusi.

2. Tidak adanya sistem deteksi dini yang dapat membantu mengidentifikasi mahasiswa yang berisiko dropout.

3. Tidak diketahui secara pasti faktor-faktor mana yang paling berpengaruh terhadap kemungkinan mahasiswa dropout.

4. Tidak tersedianya visualisasi yang memudahkan pihak institusi untuk memantau kondisi mahasiswa secara real-time.

### Cakupan Proyek
1. Melakukan eksplorasi data mahasiswa untuk memahami karakteristik dan pola dropout.

2. Melakukan seleksi fitur yang relevan dan membangun model machine learning untuk memprediksi kemungkinan dropout.

3. Mengembangkan prototype visualisasi dalam bentuk business dashboard menggunakan Looker Studio.

4. Memberikan insight dan rekomendasi berdasarkan hasil analisis dan prediksi model.

### Persiapan

Sumber data: Dataset berasal dari sumber terbuka dengan judul "Students Performance" Dataset ini memuat berbagai informasi akademik dan demografis mahasiswa.

Link dataset: https://github.com/dicodingacademy/dicoding_dataset/blob/main/students_performance/README.md 

Setup environment:
```
conda create --name main-ds python=3.11.5
conda activate main-ds
pip install -r requirements.txt

```

## Business Dashboard
Business dashboard dibuat untuk membantu tim akademik dan manajemen dalam memantau kondisi mahasiswa dan mempermudah deteksi dini risiko dropout.

**Fitur-fitur dashboard antara lain:**
- Komposisi status mahasiswa (Enrolled, Graduate, Dropout)
- Distribusi usia dan nilai terhadap status mahasiswa
- Korelasi antara faktor keuangan, nilai semester awal, dan risiko dropout
- Visualisasi multivariat: perbandingan antar fitur terhadap target status
[Link Dashboard Looker Studio (https://lookerstudio.google.com/reporting/4b31e782-cb8d-41ef-8363-4cde65037501)]

## Menjalankan Sistem Machine Learning
Sistem klasifikasi ini dibangun menggunakan algoritma Random Forest. Model dilatih menggunakan fitur terpilih seperti nilai akademik, latar belakang sosial, dan status keuangan mahasiswa untuk memprediksi risiko dropout.

1. Membuka terminal anaconda

2. Menjalankan perintah berikut:
   ```
   streamlit run predict.py
   ```
   Aplikasi streamlit sudah dideploy dan bisa diakses melalui:
   (https://proyek-monitoring-students-7qcnfjyxcus2wd5csaxy7u.streamlit.app/)
   
   Notebook colab uktuk eksplorasi
   (https://colab.research.google.com/drive/1XtH37fgp-T1WdC_feIlttKv-9G0n-Su3?usp=sharing)

## Conclusion
Sistem berhasil mengidentifikasi mahasiswa yang berisiko dropout berdasarkan fitur-fitur utama seperti nilai semester awal, usia saat masuk, dan kondisi keuangan. Aplikasi prototipe berbasis Streamlit dan Looker Studio telah dibangun untuk membantu manajemen institusi dalam proses monitoring dan pengambilan keputusan berbasis data.

### Rekomendasi Action Items
1. Terapkan sistem pemantauan berbasis data untuk mendeteksi risiko dropout sejak dini.
2. Fokus pada mahasiswa dengan nilai semester awal rendah dan kondisi finansial kurang mendukung.
3. Sediakan bimbingan akademik rutin dan pendampingan psikologis pada kelompok mahasiswa yang teridentifikasi berisiko.
