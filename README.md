# realtime-test-farrel

Sistem ini menerima input berupa kalimat berbahasa Inggris yang kemudian akan dianalisis kesalahan grammarnya, 
dijelaskan mengapa salah, dan akan dikoreksi menjadi kalimat yang benar. Model ini memanfaatkan Google Gemini API 
untuk menganalisis grammar kalimat dan Deepgram AI untuk menerjemahkan respons teks dari model Gemini API menjadi 
speech berbahasa Inggris.

Cara instalasi: 
1. pip install -r requirements.txt
2. Pilih IDE kesukaan Anda dan run kode main.py
3. Input kalimat bahasa Inggris berupa teks yang ingin dianalisis.
4. Akan keluar file answer.mp3 di direktori Anda.