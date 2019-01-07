# Teori Pertemuan Ke-5
DAG menggambarkan cara menjalankan pipa data, operator menggambarkan apa yang harus dilakukan dalam pipa data. Biasanya, ada tiga kategori besar operator

* Sensor: menunggu waktu tertentu, file eksternal, atau sumber data hulu

* Operator: memicu tindakan tertentu (mis. Jalankan perintah bash, jalankan fungsi python, atau jalankan query Hive, dll)

* Transfer: memindahkan data dari satu lokasi ke lokasi lain

Sensor membuka blokir aliran data setelah waktu tertentu berlalu atau ketika data dari sumber data hulu tersedia. Di Airbnb, mengingat sebagian besar pekerjaan ETL kami melibatkan kueri Hive, kami sering NamedHivePartitionSensorsmemeriksa apakah partisi terbaru dari tabel Hive tersedia untuk pemrosesan hilir.

Operator memicu transformasi data, yang sesuai dengan langkah ransform T. Karena Airflow adalah open-source, kontributor dapat memperluas BaseOperator kelas untuk membuat operator kustom sesuai keinginan mereka. Di Airbnb, operator paling umum yang kami gunakan adalah HiveOperator(untuk menjalankan permintaan sarang), tetapi kami juga menggunakan PythonOperator(misalnya untuk menjalankan skrip Python) dan BashOperator(misalnya untuk menjalankan skrip bash, atau bahkan pekerjaan percikan mewah) cukup sering. Kemungkinannya tidak terbatas di sini

Akhirnya, kami juga memiliki operator khusus yang Mentransfer data dari satu tempat ke tempat lain, yang sering memetakan langkah L oad di ETL. Di Airbnb, kami menggunakan MySqlToHiveTransferatau S3ToHiveTransfercukup sering, tetapi ini sangat tergantung pada infrastruktur data seseorang dan di mana data warehouse tinggal.