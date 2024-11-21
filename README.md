
# LSTM RNN Model for Next-Word Prediction on Shakespeare's *Hamlet*  
This repository contains a Long Short-Term Memory (LSTM) Recurrent Neural Network (RNN) model trained on Shakespeare's *Hamlet* from the NLTK Gutenberg corpus. The model predicts the next word based on the input sentence and demonstrates how deep learning can generate text inspired by classical literature.

## 🚀 Live Demo  
Check out the live demonstration of the project on **Streamlit**:  
👉 [Live App Link](#) https://predict-the-next-word-hq2cuwkvpp7yqnksgh2ar6.streamlit.app/  

With the demo, you can input any sentence fragment inspired by Shakespearean language, and the model will predict the next word!

## 📜 Features  
- **Data Source**: Trained on the full text of *Hamlet* from NLTK's Gutenberg corpus.  
- **Model Architecture**:  
  - LSTM layers for capturing long-term dependencies in text.  
  - Built using TensorFlow/Keras for deep learning.  
- **Prediction Capability**:  
  - Input a sequence of words or a partial sentence.  
  - Outputs the most likely next word in Shakespearean style.  
- **Interactive Demo**:  
  - Streamlit app for easy and interactive usage.  

## 📚 Dataset  
The model is trained on *Hamlet* from NLTK's Gutenberg corpus. If you'd like to explore the dataset, you can access it via:  
```python
from nltk.corpus import gutenberg
print(gutenberg.raw('shakespeare-hamlet.txt'))
```

## 🧠 Model Details  
1. **Preprocessing**:  
   - Tokenization of the text into sequences.  
   - Creation of a word-to-index dictionary for encoding.  
2. **Model Training**:  
   - Built with an LSTM-based RNN.  
   - Trained to predict the next word in a sequence.  
3. **Evaluation**:  
   - The model's performance is evaluated based on its ability to generate meaningful text resembling Shakespearean language.  

## 🛠️ Installation  
1. Clone this repository:  
   ```bash
   git clone https://github.com/lalit-jamdagnee/Predict-the-next-word.git
   cd Predict-the-next-word
   ```
2. Install dependencies:  
   ```bash
   pip install -r requirements.txt
   ```
3. Run the Streamlit app locally:  
   ```bash
   streamlit run app.py
   ```

## 🎥 How It Works  
1. Enter a partial sentence in the input box.  
2. The model processes the text and predicts the next word.  
3. The output is displayed in real-time, creating a seamless user experience.  

## 🌟 Results  
The model generates predictions that closely align with Shakespeare's writing style, adding a touch of literary flair to your inputs. For example:  
- **Input**: "To be or not to"  
- **Output**: "buried"  

## 🔗 Technologies Used  
- **Python**  
- **TensorFlow/Keras**  
- **NLTK**  
- **Streamlit**  

## 📝 Future Enhancements  
- Extend training to include more of Shakespeare's works for improved predictions.  
- Add support for generating entire sentences or paragraphs.  
- Enhance the Streamlit interface with more features and styling.  

## 🤝 Contributing  
Contributions are welcome! Feel free to open issues or submit pull requests to improve the project.  

## 📜 License  
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.  

