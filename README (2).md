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

4. Memberikan insight dan rekomendasi berdasarkan hasil analisis data dan prediksi.

### Persiapan

Sumber data: Dataset berasal dari sumber terbuka dengan judul "Students Performance" Dataset ini memuat berbagai informasi akademik dan demografis mahasiswa.

Setup environment:
```
- Python (Pandas, Scikit-learn, Matplotlib, Seaborn)

- Google Looker Studio untuk pembuatan dashboard

- Google Colab untuk pemrosesan data dan pengembangan model machine learning


```

## Business Dashboard
Business dashboard dibuat untuk membantu tim akademik dan manajemen dalam memantau kondisi mahasiswa dan mempermudah deteksi dini risiko dropout.

**Fitur-fitur dashboard antara lain:**
- Jumlah total mahasiswa
- Jumlah mahasiswa berdasarkan status: Dropout, Enrolled, Graduate
- Persentase dropout
- Dropout berdasarkan usia
- Hubungan antara status mahasiswa dengan faktor-faktor seperti:
- Grade saat admission
- Pekerjaan orang tua (ayah)
- Nilai kurikulum semester 1
- Tingkat pengangguran dan GDP
  
[Link Dashboard Looker Studio] https://lookerstudio.google.com/reporting/5d6d63d5-3e32-4efd-91fe-b9405c702d85)

## Menjalankan Sistem Machine Learning
Sistem machine learning dibangun menggunakan algoritma klasifikasi (contohnya: Random Forest). Model dilatih untuk memprediksi kemungkinan mahasiswa dropout berdasarkan beberapa fitur terpilih, seperti nilai akademik, latar belakang keluarga, dan kondisi ekonomi makro.

1. Memastikan Python dan pustaka berikut sudah terpasang:

 ```
pip install pandas scikit-learn joblib
```
2. Menjalankan predict.py

3. Output dashboard_data

[Link Prototype (https://colab.research.google.com/drive/1XtH37fgp-T1WdC_feIlttKv-9G0n-Su3?usp=sharing)]

## Conclusion
Proyek ini berhasil mengidentifikasi fitur-fitur penting yang berkontribusi terhadap risiko dropout mahasiswa, serta membangun sistem prediksi menggunakan machine learning. Selain itu, dashboard interaktif juga telah dibuat untuk memudahkan pemantauan dan pengambilan keputusan.

Model yang dibangun dapat dijadikan alat bantu untuk mendeteksi mahasiswa yang memerlukan perhatian lebih, sehingga pihak institusi dapat melakukan tindakan pencegahan sedini mungkin.

### Rekomendasi Action Items
1. Implementasi sistem deteksi dini berbasis data untuk memantau mahasiswa berisiko tinggi dropout, terutama berdasarkan nilai semester awal dan kondisi keluarga.
2. Pemberian intervensi dan bimbingan akademik secara berkala kepada mahasiswa yang teridentifikasi melalui dashboard dan model machine learning.
