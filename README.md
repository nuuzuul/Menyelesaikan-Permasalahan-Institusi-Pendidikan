# Proyek Akhir: Menyelesaikan Permasalahan Perusahaan Edutech

## Business Understanding
Jaya Jaya Institut merupakan lembaga pendidikan tinggi yang telah berdiri sejak tahun 2000 dan dikenal sukses meluluskan banyak mahasiswa berprestasi di berbagai bidang. Meskipun demikian, institusi ini tengah menghadapi masalah signifikan berupa tingginya angka mahasiswa yang tidak menyelesaikan studi atau mengalami dropout.

### Permasalahan Bisnis
Permasalahan bisnis yang akan diselesaikan yaitu:
1. Persentase mahasiswa yang tidak menyelesaikan studi cukup tinggi, yakni mencapai 32,1% dari seluruh mahasiswa yang terdaftar.
2. Sulit untuk mengenali faktor-faktor kunci yang berkontribusi terhadap terjadinya dropout terhadap mahasiswa.
3. Belum tersedia sistem deteksi dini yang dapat mengidentifikasi mahasiswa dengan potensi risiko dropout.
4. Tantangan dalam memantau kinerja akademik mahasiswa secara efisien dan menyeluruh.

### Cakupan Proyek
Cakupan proyek yang akan dikerjakan yaitu:
1. Melakukan analisis data mahasiswa guna mengidentifikasi penyebab utama terjadinya dropout.
2. Merancang model pembelajaran mesin untuk memperkirakan mahasiswa yang berpotensi tidak menyelesaikan studi.
3. Membangun dashboard guna memantau perkembangan akademik mahasiswa.
4. Menerapkan sistem prediksi melalui sebuah aplikasi berbasis web.
5. Merumuskan rekomendasi langkah-langkah strategis untuk menekan angka mahasiswa dropout.
### Persiapan

Sumber data: https://github.com/dicodingacademy/dicoding_dataset/blob/main/students_performance/data.csv

Setup environment:
```
pip install -r requirements.txt
```

## Business Dashboard
Guna mendukung Jaya Jaya Institut dalam memantau kinerja akademik mahasiswa, telah dikembangkan sebuah dashboard interaktif berbasis Metabase. Dashboard ini menyajikan visualisasi menyeluruh terkait distribusi status mahasiswa, faktor-faktor yang berkontribusi terhadap dropout, serta capaian akademik mereka.

Dashboard Metabase dapat diakses seperti berikut:
##### Setup metabase:
```
docker pull metabase/metabase:v0.46.4
docker run -p 3000:3000 --name metabase metabase/metabase
```
- Email: root@mail.com
- Password: root123
Hasil dapat dilihat pada gambar nuuzuul-dashboard

## Menjalankan Sistem Machine Learning
Model random forest yang dibuat telah dikembangkan untuk memprediksi mahasiswa yang akan dropout dengan menggunakan aplikasi web streamlit cloud dengan mengakses link berikut: https://menyelesaikan-permasalahan-institusi-pendidikan-hptm4vgfkz5bsu.streamlit.app/
```
pip install -r requirements.txt

```
```
streamlit run app.py
```

## Conclusion
Dapat disimpulkan bahwa:
1. Performa akademik mahasiswa pada semester pertama dan kedua menjadi faktor utama yang mempengaruhi risiko mahasiswa mengalami dropout.
2. Aspek ekonomi yang dialami mahasiswa juga memiliki pengaruh besar terhadap keputusan dropout.
3. Model  yang dikembangkan berhasil memprediksi risiko dropout mahasiswa.
4. Mengidentifikasi awal mahasiswa agar institusi pendidikan dapat menggurangi potensi dropout yang meningkat

### Rekomendasi Action Items
Beberapa rekomendasi action items yang harus dilakukan perusahaan guna menyelesaikan permasalahan:
- Dukungan Finansial dengan Menyediakan program bantuan keuangan dan beasiswa yang lebih terorganisir untuk mahasiswa dengan masalah ekonomi.
- Penerapan Sistem model prediksi dropout ke dalam sistem akademik untuk secara otomatis mendeteksi mahasiswa berisiko pada awal-awal semester.
- Membentuk program pembimbingan akademik khusus untuk mahasiswa yang teridentifikasi berisiko tinggi mengalami dropout, dengan penekanan pada mata kuliah yang sering menjadi hambatan pada mahasiswa.
