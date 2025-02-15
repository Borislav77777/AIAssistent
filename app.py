from flask import Flask, render_template, request, jsonify
from transformers import pipeline

app = Flask(__name__)

# Инициализация простой модели для генерации текста
generator = pipeline('text-generation', model='gpt2')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate_response():
    try:
        user_input = request.json.get('message', '')
        
        # Генерация ответа
        response = generator(user_input, max_length=50, num_return_sequences=1)[0]['generated_text']
        
        return jsonify({'response': response})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    # Изменим порт на 8080
    app.run(host='0.0.0.0', port=8080, debug=True)