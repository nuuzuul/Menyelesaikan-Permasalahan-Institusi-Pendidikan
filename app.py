import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import joblib
import numpy as np

# Konfigurasi halaman
st.set_page_config(page_title="Prediksi Dropout Mahasiswa", layout="wide")

# Load model
model = joblib.load("dropout_prediction_model.joblib")

# Sidebar navigasi
st.sidebar.title("Navigasi")
halaman = st.sidebar.radio("Pilih Halaman", ["Beranda", "Dashboard", "Prediksi Dropout"])

# Halaman Beranda
if halaman == "Beranda":
    st.title("Website Prediksi Dropout Mahasiswa")
    st.write("""
    Aplikasi ini membantu memprediksi kemungkinan dropout mahasiswa berdasarkan data.
    """)
    st.image(
        "https://www.ciputramakassar.ac.id/baa/wp-content/uploads/2021/11/Article-Square-Cover-1024x1024.png",
        use_container_width=True
    )

# Halaman Dashboard Visualisasi
elif halaman == "Dashboard":
    st.title("Dashboard Data Mahasiswa")

    try:
        data = pd.read_csv("data.csv", delimiter=";")

        target_col = None
        for col in ["Target", "Status", "Dropout"]:
            if col in data.columns:
                target_col = col
                break

        if not target_col:
            st.warning("Kolom target dropout tidak ditemukan.")
        else:
            # Distribusi Target
            st.subheader("Distribusi Mahasiswa Dropout")
            fig, ax = plt.subplots()
            sns.countplot(data=data, x=target_col, hue=target_col, palette="Set2", ax=ax, legend=False)
            ax.set_title("Distribusi Status Dropout")
            st.pyplot(fig)

            # Univariate Analysis: Umur
            if "Age_at_enrollment" in data.columns:
                st.subheader("Distribusi Umur Mahasiswa")
                fig, ax = plt.subplots()
                sns.histplot(data["Age_at_enrollment"], kde=True, ax=ax, bins=20, color='skyblue')
                ax.set_title("Distribusi Umur Mahasiswa")
                st.pyplot(fig)

            # Univariate Analysis: Jenis Kelamin
            if "Gender" in data.columns:
                st.subheader("Distribusi Mahasiswa Berdasarkan Gender")

                # Mapping gender numerik ke label deskriptif
                gender_map = {0: 'Female', 1: 'Male'}
                data['Gender_Label'] = data['Gender'].map(gender_map)

                fig, ax = plt.subplots()
                sns.countplot(data=data, x="Gender_Label", hue=target_col, palette="pastel", ax=ax)
                ax.set_title("Perbandingan Dropout Berdasarkan Gender")
                st.pyplot(fig)

            # Multivariate: Korelasi antar fitur numerikal
            numeric_data = data.select_dtypes(include=[np.number])
            if not numeric_data.empty:
                st.subheader("Korelasi antar Fitur Numerik")
                corr = numeric_data.corr()
                fig, ax = plt.subplots(figsize=(10, 8))
                sns.heatmap(corr, annot=True, fmt=".2f", cmap="coolwarm", ax=ax)
                ax.set_title("Matriks Korelasi")
                st.pyplot(fig)

            # EDA: Dropout berdasarkan Status Beasiswa
            if "Scholarship_holder" in data.columns:
                st.subheader("Dropout Berdasarkan Status Beasiswa")
                                
                gender_map = {0: 'Female', 1: 'Male'}
                data['Scholarship_holder_Label'] = data['Scholarship_holder'].map(gender_map)

                fig, ax = plt.subplots()
                sns.countplot(data=data, x="Scholarship_holder_Label", hue=target_col, palette="Set3", ax=ax)
                ax.set_title("Hubungan Beasiswa dengan Dropout")
                st.pyplot(fig)

    except Exception as e:
        st.error(f"Terjadi kesalahan saat memuat data: {e}")

# Halaman Prediksi Dropout
elif halaman == "Prediksi Dropout":
    st.title("Pengisian Data Prediksi Dropout Mahasiswa")

    # Fungsi encoding
    def encode_binary(val): return 1 if val == "Yes" else 0
    def encode_gender(val): return 1 if val == "Male" else 0
    def encode_marital_status(val): return {"Single": 0, "Married": 1, "Divorced": 2, "Widowed": 3}.get(val, 0)
    def encode_application_mode(val): return {"Online": 1, "In-person": 2, "Other": 3}.get(val, 3)
    def encode_course(val): return {"Engineering": 1, "Economics": 2, "Management": 3, "Other": 0}.get(val, 0)
    def encode_prev_qualification(val): return {"High School": 1, "Bachelor": 2, "Other": 0}.get(val, 0)
    def encode_nationality(val): return 0 if val == "Local" else 1
    def encode_attendance(val): return 0 if val == "Daytime" else 1

    # Form input
    with st.form("dropout_form"):
        st.subheader("Isi Data Mahasiswa")
        
        # Input data
        marital_status = st.selectbox("Status Pernikahan", ["Single", "Married", "Divorced", "Widowed"])
        application_mode = st.selectbox("Mode Aplikasi", ["Online", "In-person", "Other"])
        course = st.selectbox("Program Studi", ["Engineering", "Economics", "Management", "Other"])
        attendance = st.selectbox("Waktu Kuliah", ["Daytime", "Evening"])
        prev_qualification = st.selectbox("Kualifikasi Sebelumnya", ["High School", "Bachelor", "Other"])
        prev_qual_grade = st.number_input("Nilai Kualifikasi Sebelumnya", min_value=0.0, max_value=20.0)
        nationality = st.selectbox("Kebangsaan", ["Local", "International"])
        admission_grade = st.number_input("Nilai Masuk", min_value=0.0, max_value=20.0)
        displaced = st.selectbox("Mahasiswa Pindahan", ["Yes", "No"])
        special_needs = st.selectbox("Berkebutuhan Khusus", ["Yes", "No"])
        debtor = st.selectbox("Menunggak Pembayaran", ["Yes", "No"])
        tuition_up_to_date = st.selectbox("Pembayaran Terkini", ["Yes", "No"])
        gender = st.selectbox("Jenis Kelamin", ["Male", "Female"])
        scholarship = st.selectbox("Beasiswa", ["Yes", "No"])
        age = st.number_input("Umur Saat Masuk", min_value=15, max_value=60)
        international = st.selectbox("Mahasiswa Internasional", ["Yes", "No"])
        units_1st_credited = st.number_input("Unit Semester 1 Diakui", min_value=0)
        units_1st_enrolled = st.number_input("Unit Semester 1 Diambil", min_value=0)
        units_1st_eval = st.number_input("Evaluasi Semester 1", min_value=0)
        units_1st_approved = st.number_input("Unit Semester 1 Lulus", min_value=0)
        units_1st_grade = st.number_input("Nilai Semester 1", min_value=0.0, max_value=20.0)
        units_1st_no_eval = st.number_input("Unit Tanpa Evaluasi", min_value=0)

        submit = st.form_submit_button("Prediksi")

    # Prediksi
    if submit:
        try:
            # Transform data input ke bentuk array tanpa nama kolom
            input_data = np.array([[
                encode_marital_status(marital_status),
                encode_application_mode(application_mode),
                encode_course(course),
                encode_attendance(attendance),
                encode_prev_qualification(prev_qualification),
                prev_qual_grade,
                encode_nationality(nationality),
                admission_grade,
                encode_binary(displaced),
                encode_binary(special_needs),
                encode_binary(debtor),
                encode_binary(tuition_up_to_date),
                encode_gender(gender),
                encode_binary(scholarship),
                age,
                encode_binary(international),
                units_1st_credited,
                units_1st_enrolled,
                units_1st_eval,
                units_1st_approved,
                units_1st_grade,
                units_1st_no_eval
            ]])

            # Prediksi dengan model
            prediction = model.predict(input_data)[0]

            if prediction == 1:
                st.error("Mahasiswa berpotensi Dropout.")
            else:
                st.success("Mahasiswa tidak berpotensi Dropout.")

        except Exception as e:
            st.error(f"Terjadi kesalahan saat memproses prediksi: {e}")