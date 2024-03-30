from flask import Flask, render_template, request
import joblib

app = Flask(__name__)

# Load the trained model
loaded_model = joblib.load('sentiment_analysis_model.joblib')

# Function to predict sentiment from text
def predict_sentiment(text):
    return loaded_model.predict([text])[0]

# Function to save feedback
def save_feedback(text, sentiment):
    with open('user_feedback.txt', 'a') as file:
        file.write(f'Text: {text}\nSentiment: {sentiment}\n\n')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        text = request.form['text']
        sentiment_prediction = predict_sentiment(text)
        save_feedback(text, sentiment_prediction)
        sentiment = "Negative" if sentiment_prediction == 0 else "Neutral" if sentiment_prediction == 1 else "Positive"
        return render_template('result.html', text=text, sentiment=sentiment)

if __name__ == '__main__':
    app.run(debug=True)
