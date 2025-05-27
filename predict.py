import streamlit as st
import pandas as pd
import joblib

# Load model, scaler, dan fitur
model = joblib.load('model_rf.pkl')
scaler = joblib.load('scaler.pkl')
selected_features = list(model.feature_names_in_)

features_to_scale = [
    'Curricular_units_2nd_sem_approved',
    'Curricular_units_2nd_sem_grade',
    'Curricular_units_1st_sem_approved',
    'Curricular_units_1st_sem_grade',
    'Admission_grade',
    'Curricular_units_2nd_sem_evaluations',
    'Age_at_enrollment',
    'Previous_qualification_grade',
    'Curricular_units_1st_sem_evaluations'
]
features_not_scaled = ['Tuition_fees_up_to_date']
status_map_reverse = {0: "Enrolled", 1: "Graduate", 2: "Dropout"}

st.title("Prediksi Status Mahasiswa")

with st.form("input_form"):
    st.subheader("Masukkan Data Mahasiswa")
    
    col1, col2 = st.columns(2)

    with col1:
        cu2_approved = st.number_input('Mata kuliah semester 2 yang lulus', min_value=0)
        cu2_grade = st.number_input('Nilai rata-rata semester 2', min_value=0.0)
        cu2_eval = st.number_input('Evaluasi semester 2', min_value=0)
        admission_grade = st.number_input('Nilai masuk', min_value=0.0)
        age = st.number_input('Umur saat masuk', min_value=15)
    
    with col2:
        cu1_approved = st.number_input('Mata kuliah semester 1 yang lulus', min_value=0)
        cu1_grade = st.number_input('Nilai rata-rata semester 1', min_value=0.0)
        cu1_eval = st.number_input('Evaluasi semester 1', min_value=0)
        prev_qualification = st.number_input('Nilai kualifikasi sebelumnya', min_value=0.0)
        tuition_paid = st.selectbox('Pembayaran SPP up-to-date?', ['Ya', 'Tidak'])

    submit = st.form_submit_button("Prediksi")

if submit:
    # Buat input dataframe
    sample_input = pd.DataFrame([{
        'Curricular_units_2nd_sem_approved': cu2_approved,
        'Curricular_units_2nd_sem_grade': cu2_grade,
        'Curricular_units_1st_sem_approved': cu1_approved,
        'Curricular_units_1st_sem_grade': cu1_grade,
        'Admission_grade': admission_grade,
        'Curricular_units_2nd_sem_evaluations': cu2_eval,
        'Tuition_fees_up_to_date': 1 if tuition_paid == 'Ya' else 0,
        'Age_at_enrollment': age,
        'Previous_qualification_grade': prev_qualification,
        'Curricular_units_1st_sem_evaluations': cu1_eval
    }])

    # Tambah kolom yang tidak ada agar sesuai dengan selected_features
    for col in selected_features:
        if col not in sample_input.columns:
            sample_input[col] = 0

    # Scaling & gabung
    features_to_scale_filtered = [f for f in selected_features if f in features_to_scale]
    features_not_scaled_filtered = [f for f in selected_features if f in features_not_scaled]

    X_to_scale = sample_input[features_to_scale_filtered]
    X_not_scaled = sample_input[features_not_scaled_filtered]

    X_scaled_part = scaler.transform(X_to_scale)
    X_scaled_df = pd.DataFrame(X_scaled_part, columns=features_to_scale_filtered)

    sample_final = pd.concat([X_scaled_df, X_not_scaled], axis=1)
    sample_final = sample_final[selected_features]

    # Prediksi
    pred = model.predict(sample_final)[0]
    probs = model.predict_proba(sample_final)[0]

    st.success(f"🎓 Prediksi Status Mahasiswa: **{status_map_reverse[pred]}**")

    st.subheader("Probabilitas:")
    for i, prob in enumerate(probs):
        st.write(f"- {status_map_reverse[i]}: {prob:.2%}")
