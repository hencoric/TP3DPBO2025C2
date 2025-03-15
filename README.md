# JANJI

Saya Marco Henrik Abineno dengan NIM 2301093 mengerjakan Tugas Praktikum 3 dalam mata kuliah Desain dan Pemrograman Berorientasi Objek untuk keberkahanNya maka saya tidak melakukan kecurangan seperti yang telah dispesifikasikan. Aamiin.

# DESAIN PROGRAM

## Diagram

![TP3 drawio](https://github.com/user-attachments/assets/14ef6c9c-29f8-4a36-aacf-4cc2560fdbf0)

## Konsep OOP yang digunakan

### 1. Hierarchical Inheritance

Hierarchical Inheritance terjadi ketika satu kelas dasar (parent) memiliki banyak turunan (child). Dalam program saya class Komponen merupakan parent dari beberapa class  
a. Cpu mewarisi dari Komponen  
b. GPU mewarisi dari Komponen  
c. Harddrive mewarisi dari Komponen  
d. Ram mewarisi dari Komponen  

### 2. Multiple Inheritance

Multiple Inheritance terjadi ketika suatu kelas memiliki lebih dari satu kelas induk (parent). Dalam program saya class Ram mewarisi dari 2 class parent  
a. Komponen  
b. Overclocking  

### 3. Hybrid Inheritance

Hybrid Inheritance adalah kombinasi dari lebih dari satu jenis pewarisan. Dalam kode saya class Server Mewarisi dari class Cpu dan Gpu, yang keduanya mewarisi dari class Komponen  

### 4. Composition

a. Komputer memiliki CPU  
b. Komputer memiliki Ram (banyak, dalam bentuk vector<ram>)  
c. Komputer memiliki Harddrive  

# ALUR PROGRAM

### **Alur Program**  

1. **Membuat Objek Komponen**  
   - CPU 
   - Beberapa RAM 
   - Harddrive  

2. **Membuat Objek Komputer**
   - Menggunakan CPU, RAM, dan Harddrive  
   - Menambahkan RAM tambahan ke komputer  

3. **Menampilkan Informasi Komputer**  
   - Nama komputer  
   - Detail CPU  
   - Detail semua RAM yang digunakan  
   - Detail Harddrive  

4. **Membuat Objek Server** 
   - Menggunakan CPU dan GPU  
   - Memiliki jumlah rack tertentu  

5. **Menampilkan Informasi Server**  
   - Detail CPU  
   - Detail GPU  
   - Jumlah rack  

6. **Program selesai**

