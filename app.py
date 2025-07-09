'''
How to run this locally?

In your terminal, use the command:
python -m streamlit run app.py
'''

import joblib
import streamlit as st
import pandas as pd

# Load model dan scaler
model_load = joblib.load('diabetes_model.pkl')
scaler = joblib.load('scaler.pkl')

# Kolom yang digunakan
kolom_data = [
    "Pregnancies",
    "Glucose",
    "BMI",
    "DiabetesPedigreeFunction",
    "Age"
]

if __name__ == "__main__":

    # Judul web
    st.title('Prediksi Diabetes Berdasarkan Data Medis')

    st.subheader('Tentang Diabetes', divider='grey')
    st.markdown('''
    Diabetes adalah kondisi kesehatan kronis yang ditandai dengan kadar gula darah yang tinggi dalam jangka waktu lama. Penyebab utama meningkatnya gula darah bisa berasal dari gaya hidup, faktor genetik, atau kondisi metabolik tertentu.

    Dalam aplikasi ini, prediksi diabetes didasarkan pada beberapa faktor berikut:

    - **Jumlah Kehamilan (Pregnancies)**: Riwayat kehamilan, terutama pada wanita, dapat memengaruhi risiko diabetes gestasional yang bisa berkembang menjadi diabetes tipe 2.
    - **Kadar Glukosa (Glucose)**: Merupakan kadar gula dalam darah. Glukosa tinggi adalah indikator penting dalam mendeteksi risiko diabetes.
    - **BMI (Body Mass Index)**: Menggambarkan keseimbangan antara berat badan dan tinggi badan. Nilai BMI yang tinggi dapat meningkatkan risiko resistensi terhadap gula darah.
    - **Diabetes Pedigree Function (DPF)**: Mengukur seberapa besar riwayat keluarga memengaruhi risiko diabetes. Semakin tinggi nilainya, semakin besar kemungkinan seseorang mewarisi risiko tersebut.
    - **Usia (Age)**: Risiko diabetes meningkat seiring bertambahnya usia, terutama setelah usia 25 tahun.

    Dengan mempertimbangkan kelima faktor ini, aplikasi ini dapat memberikan estimasi awal apakah seseorang berpotensi mengalami diabetes atau tidak. Prediksi ini bukan diagnosis medis, namun bisa menjadi langkah awal untuk memeriksakan diri lebih lanjut.
    ''')

    st.subheader('Apa itu Predict Machine?', divider='grey')
    st.markdown('''
    Predict Machine adalah mesin prediksi berbasis machine learning yang telah dilatih menggunakan data medis. Mesin ini dirancang untuk membantu memprediksi kemungkinan seseorang mengidap diabetes berdasarkan parameter tertentu.
    ''')

    st.subheader('Cara Menggunakan?', divider='grey')
    st.markdown('''
    Silakan isi data pada sidebar berikut dengan benar. Klik tombol "Predict" untuk mengetahui hasil prediksi kondisi diabetes Anda berdasarkan model yang sudah dilatih.
    ''')

    with st.sidebar:
        st.header('Input Data', divider='rainbow')

        pregnancies = int(st.number_input('Berapa kali kehamilan?', min_value=0, max_value=13, step=1))
        glucose = int(st.number_input('Kadar Glukosa (37 -200)', min_value=37, max_value=200, step=1))
        bmi = st.number_input('BMI Anda (14.0 - 50.0)', min_value=14.0, max_value=50.0, step=0.1)
        dpf = st.number_input('Diabetes Pedigree Function (0.0 - 1)', min_value=0.0, max_value=1.0, step=0.01)
        age = int(st.number_input('Usia Anda (0 - 66)', min_value=0, max_value=66, step=1))

        # Data input mentah
        input_data = [[pregnancies, glucose, bmi, dpf, age]]

        if st.button('Predict'):
            input_df = pd.DataFrame(input_data, columns=kolom_data)

            # Lakukan scaling
            input_scaled = scaler.transform(input_df)

            # Prediksi dengan data yang sudah discale
            result = model_load.predict(input_scaled)

            if result[0] == 1:
                st.error('Pasien terprediksi **MENGIDAP DIABETES** ⚠️')
            else:
                st.success('Pasien **TIDAK TERINDIKASI DIABETES** ✅')
