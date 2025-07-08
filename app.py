'''
How to run in local?

Run this script using the following command in terminal:
python -m streamlit run app.py

'''

import joblib
import streamlit as st
import pandas as pd

model_load = joblib.load('diabetes_model.pkl')

kolom_data = [
    "Pregnancies",
    "Glucose",
    "BloodPressure",
    "SkinThickness",
    "Insulin",
    "BMI",
    "DiabetesPedigreeFunction",
    "Age"
]

# <--------------- MAIN --------------->

if __name__=="__main__":

    # Judul web
    st.title('Jaya Jaya Institut')
    
    st.subheader('Pengenalan Jaya Jaya Institut',  divider='grey')
    st.markdown('''Jaya Jaya Institut merupakan salah satu institusi pendidikan perguruan internasional yang telah berdiri sejak tahun 2000. Hingga saat ini ia telah mencetak banyak lulusan dengan reputasi yang sangat baik dalam bidang pendidikan. Selain itu merupakan pendidikan perguruan internasional yang sudah menarik perhatian berbagai kalangan siswa, bahkan dari mancanegara.''')
    
    st.subheader('Apa fungsi Predict Machine di bawah ini?',  divider='grey')
    st.markdown('''Predict Machine adalah sebuah mesin model yang dibuat untuk
                prediksi. Mesin ini dibuat dan di _train_ berdasarkan data yang ada pada
                Jaya Jaya Institute.''')
    
    st.subheader('Bagaimana cara menggunakannya?',  divider='grey')
    st.markdown(' Dari data yang dimiliki, anda tinggal memasukkannya sesuai dengan format data yang ada, dan berikut ini merupakan beberapa inputan yang harus diisi, yaitu:')

    st.write('**Marital Status**: Status pernikahan (Single = Belum menikah, Married = Menikah, Widower = Janda/Duda, Divorced = Cerai, Facto Union = Pernikahan tidak resmi, Legally Separated = Perceraian resmi)')
    st.write('**Nacionality**: Negara asal (Portugal, Jerman, Spanyol, Italia, Belanda, Inggris, Lituania, Angola, Kap Verde, Guinea, Mozambik, Sao Tomean, Turki, Brasil, Rumania, Moldova-Republik, Meksiko, Ukraina, Rusia, Kuba, Kolombia)') 
    st.write('**Admission Grade**: Nilai masuk (0-200)')
    st.write('**Displaced**: Apakah siswa berasal dari keluarga kurang mampu?')
    st.write('**Educational Special Needs**: Apakah siswa memiliki kebutuhan khusus pendidikan?')
    st.write('**Debtor**: Apakah siswa memiliki tanggungan hutang?')
    st.write('**Tuition Fees**: Apakah siswa sudah melunasi pembayaran terkini?')
    st.write('**Scholarship Holder**: Apakah siswa mendapatkan beasiswa?')
    st.write('**Gender**: Jenis kelamin (Man = Laki-laki, Woman = Perempuan)')
    st.write('**Age At Enrollment**: Usia siswa saat melakukan enrollment')
    st.write('**International**: Apakah siswa berasal dari luar negeri?')
    st.write('**Unemployment Rate**: Tingkat pengangguran di daerah mahasiswa')
    st.write('**Inflation Rate**: Tingkat inflasi di daerah mahasiswa')
    st.write('**GDP (Gross Domestic Product**): Tingkat GDP di daerah mahasiswa')
    st.write('**Curriculum Unit**: Jumlah Curriculum yang dikreditkan, dienrollment, disetujui, dan nilainya. Baik pada semester 1 maupun semester 2')

    
    # <--------- SIDEBAR --------->
    
    with st.sidebar:
        
        st.header('Predict Machine', divider='rainbow')

        # Pregnancies
        st.subheader('How many pregnancies?')
        pregnancies = int(st.number_input('Total kehamilan selama hidup', min_value=0, max_value=17, step=1))

        # Glucose
        st.subheader('How much your glucose?')
        glucose = int(st.number_input('Banyak Glukosa', min_value=20, max_value=200, step=1))
        
        # BloodPressure
        st.subheader('How much your Blood Pressure?')
        blood_pressure = int(st.number_input('Tekanan Darah', min_value=10, max_value=130, step=1))

        # SkinThickness
        st.subheader('How Thick your Skin?')
        skin_thickness = int(st.number_input('Tebal Kulit', min_value=9, max_value=100, step=1))
        
        # Insulin
        st.subheader('Put much your insulin?')
        insulin = int(st.number_input('Banyak Insulin', min_value=0, max_value=850, step=1))

        # BMI
        st.subheader('How much your BMI?')
        bmi = st.number_input('Indeks Massa Tubuh anda',min_value=24, max_value=51, step=0.1)
        
        # DiabetesPedigreeFunction
        st.subheader('How much your Diabetes Pedigree Function?')
        diabetes_pedigree_function = st.number_input('Peluang Turunan Diabetes dari Keluarga', min_value=0, max_value=2.4, step=0.1)

        # Age
        st.subheader('How old are you?')
        age = int(st.number_input('Umur saat ini', min_value=21, max_value=100, step=1))
        
        
        # Create the feature list based on the input data
        new_data = [[pregnancies, glucose, blood_pressure, skin_thickness, insulin, bmi, diabetes_pedigree_function, age]]

        if st.button('Predict'):
            # Convert the data into a DataFrame with proper columns
            new_data = pd.DataFrame(new_data, columns=kolom_data)
            
            # Make the prediction using the model
            result = model_load.predict(new_data)

            print(result)
            
            # # Display result in a more visually appealing way
            # if result[0] == 0:
            #     st.error('Siswa dropout', icon="🚨")  # Error with an icon
            # else:
            #     st.balloons()  # Show balloons animation
            #     st.success('Siswa bukan dropout 🎉')  # Success message with emoji
