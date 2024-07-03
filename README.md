# TOSRoberta: Terms of Service Analyzer 📜🤖

TOSRoberta is an advanced Terms of Service (ToS) analyzer powered by a fine-tuned RoBERTa-large model. It classifies clauses in ToS documents based on their fairness level, helping users quickly identify potentially unfair terms.

![image](https://github.com/HimanshuMohanty-Git24/TOSRoberta/assets/94133298/c4f6a293-9109-4e63-86e6-766dc16ad589)


## 🌟 Features

- 📊 Analyzes ToS documents and classifies clauses into three categories:
  - ✅ Clearly Fair
  - ⚠️ Potentially Unfair
  - ❌ Clearly Unfair
- 📁 Supports both PDF and text file uploads
- 💻 User-friendly web interface built with Streamlit
- 🧠 Powered by a fine-tuned RoBERTa-large model (CodeHima/Tos-Roberta)

## 🚀 Model Performance

Our Tos-Roberta model demonstrates strong performance on the task of ToS clause classification:

- **Validation Accuracy**: 89.64%
- **Test Accuracy**: 85.84%

Detailed performance metrics per epoch:

| Epoch | Training Loss | Validation Loss | Accuracy | F1 Score | Precision | Recall   |
|-------|---------------|-----------------|----------|----------|-----------|----------|
| 1     | 0.443500      | 0.398950        | 0.874699 | 0.858838 | 0.862516  | 0.874699 |
| 2     | 0.416400      | 0.438409        | 0.853012 | 0.847317 | 0.849916  | 0.853012 |
| 3     | 0.227700      | 0.505879        | 0.896386 | 0.893325 | 0.891521  | 0.896386 |
| 4     | 0.052600      | 0.667532        | 0.891566 | 0.893167 | 0.895115  | 0.891566 |
| 5     | 0.124200      | 0.747090        | 0.884337 | 0.887412 | 0.891807  | 0.884337 |

## 📁 Project Structure

```
tos-analyzer/
│
├── app.py
├── requirements.txt
├── utils/
│   ├── __init__.py
│   ├── text_processing.py
│   └── model_utils.py
└── README.md
```

## 🛠️ Installation

1. Clone the repository:
   ```
   git clone https://github.com/HimanshuMohanty-Git24/TOSRoberta.git
   cd TOSRoberta
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Run the Streamlit app:
   ```
   streamlit run app.py
   ```

## 📊 Training Visualization

We used Weights & Biases for monitoring the training process. Here's a glimpse of our training metrics:

![image](https://github.com/HimanshuMohanty-Git24/TOSRoberta/assets/94133298/d28bbd84-9008-4d19-bff1-4b62874a5faa)


## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgements

- [Hugging Face](https://huggingface.co/) for the Transformers library
- [Streamlit](https://streamlit.io/) for the easy-to-use web app framework
- [Weights & Biases](https://wandb.ai/) for experiment tracking

## 📬 Contact

Himanshu Mohanty - [CodingHima](https://x.com/CodingHima) - codehimanshu24@gmail.com

Project Link: [https://github.com/HimanshuMohanty-Git24/TOSRoberta](https://github.com/HimanshuMohanty-Git24/TOSRoberta)

---

⭐️ If you find this project useful, please consider giving it a star!
