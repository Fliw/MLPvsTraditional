import numpy as np
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers

# **Model Machine Learning (MLP)**

# Menyiapkan data
X = np.array(range(1, 11))  # Input
y = 2 * X  # Output sesuai dengan rumus

# Membagi data menjadi data latih dan data uji
X_train = X[:8]
y_train = y[:8]
X_test = X[8:]
y_test = y[8:]

# Membangun model regresi dengan lebih banyak lapisan dan neuron
model = keras.Sequential([
    layers.Dense(128, activation='relu', input_shape=(1,)),  # Lapisan tersembunyi dengan 128 neuron
    layers.Dense(64, activation='relu'),  # Lapisan tersembunyi kedua
    layers.Dense(32, activation='relu'),  # Lapisan tersembunyi ketiga
    layers.Dense(1)  # Lapisan output
])

# Mengompilasi model
model.compile(optimizer='adam', loss='mean_squared_error', metrics=['mean_absolute_error'])

# Melatih model dengan lebih banyak epoch dan menggunakan validation split
history = model.fit(X_train, y_train, epochs=250, validation_split=0.2)

# Menggunakan model untuk prediksi
def predict_next_number(input_value):
    input_tensor = tf.convert_to_tensor([[input_value]], dtype=tf.float32)  # Mengubah input ke tensor
    predicted_value = model.predict(input_tensor)
    return predicted_value[0][0]

# **Pendekatan Pemrograman Tradisional**

# Fungsi untuk menghitung output menggunakan rumus tradisional
def predict_next_number_traditional(input_value):
    return 2 * input_value  # Menggunakan rumus y = 2 * x

# Loop untuk meminta input pengguna setelah pelatihan
while True:
    user_input = input("Masukkan angka (atau ketik 'exit' untuk keluar): ")
    
    if user_input.lower() == 'exit':
        print("Keluar dari program.")
        break
    
    try:
        input_value = float(user_input)  # Mengubah input ke float
        
        # Prediksi dengan model MLP
        output_value_ml = predict_next_number(input_value)  # Memprediksi output dengan MLP
        print(f"[MLP] Input: {input_value}, Predicted Output: {output_value_ml:.4f}")
        
        # Prediksi dengan pendekatan tradisional
        output_value_traditional = predict_next_number_traditional(input_value)  # Memprediksi output dengan rumus tradisional
        print(f"[Traditional] Input: {input_value}, Predicted Output: {output_value_traditional:.4f}")
        
        # hitung jarak selisih antara kedua prediksi dalam persen
        difference = abs(output_value_ml - output_value_traditional)
        percent_difference = (difference / output_value_traditional) * 100
        print(f"Selisih: {percent_difference:.2f}%")
    except ValueError:
        print("Silakan masukkan angka yang valid.")
