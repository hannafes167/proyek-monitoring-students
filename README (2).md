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

Setup environment:
```
- Python: pandas, scikit-learn, matplotlib, seaborn, joblib

- Google Colab: pemrosesan data & pelatihan model

- Streamlit: prototipe sistem prediksi

- Looker Studio: visualisasi dashboard interaktif


```

## Business Dashboard
Business dashboard dibuat untuk membantu tim akademik dan manajemen dalam memantau kondisi mahasiswa dan mempermudah deteksi dini risiko dropout.

**Fitur-fitur dashboard antara lain:**
- Jumlah total mahasiswa
- Jumlah mahasiswa berdasarkan status: Dropout, Enrolled, Graduate
- Persentase dropout
- Berdasarkan status pembayaran kuliah
- Berdasarkan nilai saat penerimaan (admission grade)
- Berdasarkan usia saat masuk
- Berdasarkan nilai kurikulum semester 1 dan 2
- Berdasarkan kualifikasi pendidikan sebelumnya
  
[Link Dashboard Looker Studio] https://lookerstudio.google.com/reporting/4b31e782-cb8d-41ef-8363-4cde65037501)

## Menjalankan Sistem Machine Learning
Sistem klasifikasi ini dibangun menggunakan algoritma Random Forest. Model dilatih menggunakan fitur terpilih seperti nilai akademik, latar belakang sosial, dan status keuangan mahasiswa untuk memprediksi risiko dropout.

1. Memastikan Python dan pustaka berikut sudah terpasang:

 ```
pip install pandas scikit-learn joblib
```
2. di environment Python lokal atau Colab.
   
3. Implementasikan ke Streamlit untuk pengujian berbasis web.
   
4. Gunakan output dashboard_data.csv sebagai sumber data untuk dashboard Looker Studio.

[Link Prototype (https://colab.research.google.com/drive/1XtH37fgp-T1WdC_feIlttKv-9G0n-Su3?usp=sharing)]

## Conclusion
Proyek ini berhasil membangun sistem prediksi mahasiswa dropout menggunakan machine learning serta mengembangkan dashboard interaktif untuk pemantauan kondisi mahasiswa. Hasil analisis menunjukkan bahwa nilai akademik dan kondisi keuangan merupakan faktor dominan dalam risiko dropout.

### Rekomendasi Action Items
1. Implementasi sistem deteksi dini berbasis data untuk memantau mahasiswa berisiko tinggi dropout, terutama berdasarkan nilai semester awal dan kondisi keluarga.
2. Pemberian intervensi dan bimbingan akademik secara berkala kepada mahasiswa yang teridentifikasi melalui dashboard dan model machine learning.
