# E-COMMERCE ELECTRONICS INVENTORY ANALYSIS

## Repository Outline

Project ini terdiri dari file:
```
1. description.md - Penjelasan gambaran umum project.
2. DAG.py - File DAG untuk workflow menggunakan Apache Airflow.
3. DAG_graph.jpg - Visualisasi DAG workflow dari Airflow.
4. GX.ipynb - Notebook untuk melakukan validasi data dengan Great Expectations.
5. data_raw.csv - Dataset asli yang digunakan pada project ini.
6. data_clean.csv - Dataset hasil preprocessing.
7. ddl.txt - Query atau struktur basis data NoSQL
8. conceptual.txt - Peertanyaan dan jawaban sebagai penjelasan materi
9. gx/ - Folder konfigurasi validasi dari Great Expectations
10. images/ - Berisi 8 screenshot visualisasi data dengan Kibana (introduction, insights, conclusion)

```

## Problem Background

Saat ini banyak konsumen barang elektronik membeli barang via online. Tetapi kebutuhan akan barang elektronik juga terbatas dan proses pembelian / penjualan tidak dapat dilakukan dalam waktu cepat, sehingga kebanyakan barang harus disimpan di gudang / menjadi stock.

Anda adalah seorang data analyst di sebuah perusahaan e-commerce yang usahanya salah satunya menjadi retailer barang elektronik. Report ini berisi hasil analisis performa penjualan barang dari jenis kategori, harga, rating, serta ketersediaan stocknya, di mana hasil reportnya akan dapat dimanfaatkan pengguna untuk melakukan strategi promosi penjualan produk serta mengurangi potensi deadstock.

## Project Output

Output dari project ini adalah:

1. Membuat workflow otomatis data pipeline menggunakan Apache Airflow
2. Melakukan validasi data otomatis menggunakan Great Expectations
3. Menghasilkan dataset yang sudah dibersihkan dan siap dimasukkan ke Elasticsearch.
4. Melampirkan hasil visualisasi performa produk dalam dashboard Kibana.
5. Memberikan rekomendasi kepada bagian dalam perusahaan yang bertanggung jawab langsung atas marketing dan inventory perusahaan.

## Data

Dataset yang digunakan memiliki ketentuan sebagai berikut:
1. URL dataset adalah https://www.kaggle.com/datasets/keyushnisar/global-product-inventory-dataset-2025. Dataset ini disimpan secara lokal dengan nama file `P2M3_nathanael_data_raw.csv`. Dataset ini berisi data performa dan spesifikasi produk elektronik dari sebuah perusahaan e-commerce.

2. Dataset terdiri dari 10.000 baris data produk dan 14 kolom, yaitu:
    `Product ID`, `Product Name`, `Product Category`, `Product Description`,` Price`,
    `Stock Quantity`, `Warranty Period`, `Product Dimensions`, `Manufacturing Date`,
    `Expiration Date`, `SKU`, `Product Tags`, `Color/Size Variations`, `Product Ratings`

3. Terdapat missing values, outlier, dan inkonsistensi format data (seperti format tanggal dan dimensi produk) yang mengharuskan Anda untuk melakukan handling      yang tepat seperti imputasi, normalisasi, dan transformasi data. Anda disarankan mengubah nama kolom ke format yang lebih ringkas atau konsisten (misalnya dalam bahasa Inggris tanpa spasi) untuk memudahkan proses transformasi dan integrasi ke `Elasticsearch`.

4. Data pada nomor 3 dihasilkan melalui pembuatan pipeline dengan `Airflow`.

5. Data yang telah dibersihkan dan siap digunakan akan tersimpan dalam file `P2M3_nathanael_data_clean.csv`. Data inilah yang digunakan untuk visualisasi data di `Kibana`

## Method

Metode/Tools yang digunakan adalah:

1. `Apache Airflow`, digunakan untuk mengorkestrasi pipeline ETL dalam bentuk DAG yang mencakup ekstraksi data mentah, validasi, pembersihan, dan penyimpanan akhir.

2. `Great Expectations`, digunakan untuk memvalidasi kualitas data melalui pengecekan null, domain, dan uniqueness, serta menghasilkan dokumentasi otomatis.

3. `Data Preprocessing`, dilakukan di notebook P2M3_nathanael_GX.ipynb untuk membersihkan data dari nilai kosong, menormalisasi kolom numerik, dan menangani outlier.

4. `Elasticsearch`, digunakan untuk menyimpan data hasil preprocessing dengan struktur dan pemetaan konsep.

5. `Kibana`, digunakan untuk menampilkan dashboard visualisasi berbasis data Elasticsearch yang mencakup performa produk, korelasi harga-rating, analisis stok, dan insight.

## Stacks

Daftar library / bahasa pemrograman yang digunakan adalah:

- `Apache Airflow`, yaitu platform orkestrasi data pipeline berbasis DAG (Directed Acyclic Graph) yang digunakan untuk mengatur dan menjadwalkan alur proses ETL secara otomatis. Tujuan dari penggunaan Airflow adalah untuk memastikan proses pengolahan data berjalan terstruktur, modular, dan dapat dimonitor dengan baik.

- `Logging`, yaitu sistem pencatatan otomatis aktivitas dan error yang terjadi selama proses pipeline berjalan. Digunakan di dalam script Airflow maupun notebook untuk memantau keberhasilan dan kegagalan proses.

- `Great Expectations`, yaitu framework validasi data yang memungkinkan pengguna membuat serangkaian “expectations” terhadap dataset, seperti pengecekan nilai null, batas domain nilai, hingga keunikan data. Tujuan dari metode ini adalah untuk menjamin kualitas dan konsistensi data sebelum diproses lebih lanjut.

- `Pandas`, yaitu library Python untuk manipulasi dan analisis data berbentuk tabel (DataFrame). Digunakan untuk proses pembersihan data, transformasi kolom, serta pengolahan data awal sebelum validasi atau loading ke database. Tujuan dari library ini adalah untuk memudahkan eksplorasi dan preprocessing data.

- `NumPy`, yaitu library Python untuk komputasi numerik, digunakan sebagai pendukung perhitungan matematis dalam proses normalisasi data, pembuatan metrik, dan pengolahan data numerik lainnya. Tujuan penggunaannya adalah untuk meningkatkan efisiensi perhitungan dalam skala besar.

- `Elasticsearch`, yaitu sistem database NoSQL berbasis dokumen yang memiliki kemampuan pencarian dan analisis data dalam jumlah besar secara real-time. Digunakan untuk menyimpan data hasil preprocessing agar bisa diakses dan divisualisasikan. Tujuan dari penggunaan Elasticsearch adalah untuk mendukung visualisasi dan analitik performa produk.

- `Kibana`, yaitu tool visualisasi data yang terintegrasi dengan Elasticsearch dan digunakan untuk membuat dashboard interaktif dari data yang disimpan di database. Tujuannya adalah untuk menyajikan insight berupa grafik dan visual analitik secara intuitif kepada user atau stakeholder.


## Reference

Dataset URL : https://www.kaggle.com/datasets/keyushnisar/global-product-inventory-dataset-2025

https://www.slimstock.com/blog/how-e-commerce-is-impacting-inventory-management/

https://www.businessinsider.com/walmart-target-use-ai-to-prevent-inventory-shortages-2025-6

---