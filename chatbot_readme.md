# 🧠 AI Chatbot Streamlit

Sebuah aplikasi chatbot sederhana namun powerful yang dibangun dengan Streamlit dan menggunakan OpenRouter API untuk mengakses berbagai model AI terdepan.

## ✨ Fitur Utama

- **Multi-Model Support**: Akses ke berbagai model AI populer seperti Llama 3.3, Gemma 2, dan Mistral
- **User-Friendly Interface**: Antarmuka chat yang bersih dan intuitif dengan desain bubble style
- **Personalisasi**: Input nama pengguna untuk pengalaman yang lebih personal
- **API Key Fleksibel**: Gunakan API key pribadi atau fallback ke default key
- **Chat History**: Riwayat percakapan yang tersimpan selama sesi
- **Reset Functionality**: Tombol untuk membersihkan riwayat chat
- **Responsive Design**: Tampilan yang menarik dengan gradient background dan styling modern

## 🚀 Model yang Tersedia

- **meta-llama/llama-3.3-8b-instruct:free** - Model terbaru dari Meta dengan performa tinggi
- **meta-llama/llama-3.1-8b-instruct:free** - Versi stabil Llama dengan kemampuan instruksi yang baik
- **google/gemma-2-9b-it:free** - Model Google Gemma dengan optimisasi untuk percakapan
- **mistralai/mistral-7b-instruct:free** - Model Mistral yang ringan namun powerful

## 📋 Persyaratan

```
streamlit
requests
```

## 🛠️ Instalasi

1. Clone repository ini:
```bash
git clone <repository-url>
cd ai-chatbot-streamlit
```

2. Install dependencies:
```bash
pip install streamlit requests
```

3. Jalankan aplikasi:
```bash
streamlit run chatbot.py
```

## 🔧 Konfigurasi

### API Key
- **Pribadi**: Masukkan OpenRouter API key Anda di sidebar untuk penggunaan personal
- **Default**: Aplikasi menyediakan fallback API key untuk testing (dengan batasan tertentu)

### Penggunaan
1. Buka aplikasi di browser (biasanya `http://localhost:8501`)
2. Masukkan nama Anda di sidebar (opsional)
3. Pilih model AI yang diinginkan
4. Mulai berinteraksi dengan chatbot!

## 🎨 Tampilan

Aplikasi menampilkan:

- **Background Gradient**: Kombinasi warna biru dan putih yang menenangkan
- **Sidebar Konfigurasi**: Panel samping untuk pengaturan dan informasi
- **Chat Interface**: Area chat dengan bubble styling untuk pesan
- **Responsive Layout**: Tampilan yang optimal di berbagai ukuran layar

## 🔍 Struktur Kode

```
chatbot.py
├── CSS Styling - Background dan tema visual
├── Sidebar Configuration - Pengaturan user dan model
├── API Configuration - Setup OpenRouter API
├── Chat Interface - Logic percakapan
└── Error Handling - Penanganan kesalahan
```

## 🌟 Keunggulan

- **Sederhana namun Fungsional**: Interface yang mudah dipahami dengan fitur lengkap
- **Multi-Model**: Fleksibilitas memilih model sesuai kebutuhan
- **Real-time Chat**: Respons langsung dari AI
- **Customizable**: Mudah dimodifikasi dan dikembangkan
- **Error Handling**: Penanganan error yang baik untuk user experience yang smooth

## 🚨 Catatan Penting

- API key default memiliki batasan penggunaan
- Untuk penggunaan intensif, disarankan menggunakan API key pribadi
- Pastikan koneksi internet stabil untuk performa optimal

## 👨‍💻 Dibuat oleh Rico

Chatbot ini dikembangkan sebagai demonstrasi integrasi Streamlit dengan OpenRouter API, menggabungkan kemudahan penggunaan dengan kekuatan model AI modern.

---

**Happy Chatting! 🎉**