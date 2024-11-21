import tensorflow as tf
import pickle
import numpy as np

# load the tokenizer 
with open('tokenizer.pickle', 'rb') as file:
    tokenizer = pickle.load(file)

# load the model 
model = tf.keras.models.load_model('next_word_lstm.h5')

# Function to predict the next word
def predict_next_word(model, tokenizer, text, max_sequence_len):
    # text preprocessing
    text = text.lower()
    token_list = tokenizer.texts_to_sequences([text])[0]
    if len(token_list) > max_sequence_len:
        token_list = token_list[-(max_sequence_len-1):]
    
    token_list = tf.keras.preprocessing.sequence.pad_sequences([token_list], padding='pre', maxlen = max_sequence_len-1)
    
    # prediction
    prediction = model.predict(token_list, verbose=0)
    predicted_word_index = np.argmax(prediction, axis=1)

    for word, index in tokenizer.word_index.items():
        if index == predicted_word_index:
            return word
    return None

max_sequence_len = model.input_shape[1]+1
## Streamlit app

import streamlit as st

# Title of the page
st.title('Next Word Prediction with LSTM')

input_text = st.text_input('Enter the sequence of words','to be or not to be')

if st.button('Predict next word'):
    word = predict_next_word(model, tokenizer, input_text, max_sequence_len)
    st.write(f'Predicted next word : {word}')
    st.write(f'The complete sentences is :\n{input_text} {word}')

