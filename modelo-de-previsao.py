from flask import Flask, request, jsonify
from sklearn.linear_model import LinearRegression

app = Flask(__name__)

# Modelo de exemplo (apenas para demonstração)
X_train = [[1], [2], [3], [4], [5]]
y_train = [2, 4, 6, 8, 10]

model = LinearRegression()
model.fit(X_train, y_train)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    input_value = data['input']
    prediction = model.predict([[input_value]])[0]
    return jsonify({'prediction': prediction})

if __name__ == '__main__':
    app.run(debug=True)
