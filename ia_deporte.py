# Importar librerías
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

# Cargar los datos de ejemplo desde un archivo CSV
data = pd.read_csv('datos_deportistas.csv')

# Definir las variables de entrada (X) y la variable de salida (y)
X = data[['Energia', 'Comparacion', 'Estrés', 'Sueño']]
y = data['EstadoAnimo']

# Convertir variables categóricas en números
X = pd.get_dummies(X, drop_first=True)

# Dividir los datos en conjuntos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Crear y entrenar el modelo
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Pedir entrada al usuario (el deportista)
energia = int(input("¿Cómo te sientes de energía hoy (1-10)?: "))
comparacion = input("¿Cómo te sientes respecto a días anteriores (Mejor/Peor/Igual)?: ")
estres = int(input("¿Qué tan estresado te sientes (1-10)?: "))
sueno = int(input("¿Cuántas horas dormiste?: "))

# Crear el DataFrame con los datos del usuario
input_usuario = pd.DataFrame({
    'Energia': [energia],
    'Comparacion': [comparacion],
    'Estrés': [estres],
    'Sueño': [sueno]
})

# Convertir los datos del usuario
input_usuario = pd.get_dummies(input_usuario, drop_first=True)

# Completar columnas que faltan
input_usuario = input_usuario.reindex(columns=X.columns, fill_value=0)

# Hacer una predicción
estado_predicho = model.predict(input_usuario)
print(f"Según los datos, tu estado de ánimo probablemente será: {estado_predicho[0]}")
