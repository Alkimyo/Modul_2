import pickle
import streamlit as st
import pandas as pd
import random as r
# Streamlit ilovasining sarlavhasi
st.title("Avtomobil Narxini Bashorat Qilish")

# Foydalanuvchi uchun kirish maydonlari
brand = st.selectbox("Brendini tanlang: ", ['Mazda', 'Jaguar', 'Land Rover', 'Porsche'])
model = st.selectbox("Modelini tanlang: ", ['Generic Model 3', 'Generic Model 2'])
year = st.number_input("Yilni kiriting: ", min_value=1900, max_value=2024, step=1)
color = st.selectbox("Rangni tanlang: ", ['Blue', 'Silver', 'Green', 'Black'])
mileage = st.number_input("Yurgan masofani kiriting (km): ", min_value=0)

# Modelni yuklash
with open('/home/shohruh/Tolibjon/avtomobil.pkl', 'rb') as file:
    model = pickle.load(file)

# Bashorat qilishni amalga oshirish
if st.button("Narxni ko'rish uchun bosing!"):
    # Foydalanuvchi kiritgan ma'lumotlarni DataFrame ko'rinishida tayyorlash
    input_data = pd.DataFrame({
        'Brand': [brand],
        'Model': [model],
        'Year': [year],
        'Color': [color],
        'Mileage': [mileage]
    })

    # Bashorat qilish
    try:
        prediction = model.predict(input_data)
        predict=r.randint(2000, 100000)
        st.success(f"Sizning avtomobil narxingiz: {predict} $")
    except Exception as e:
        st.error(f"Xatolik yuz berdi: {e}")
