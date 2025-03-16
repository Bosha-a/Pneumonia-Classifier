# Pneumonia Classifier

This project aims to develop a deep learning model capable of detecting pneumonia from chest X-ray images. Leveraging convolutional neural networks (CNNs), the classifier distinguishes between normal and pneumonia-affected lungs, assisting in early diagnosis and treatment.

## Features

- **Deep Learning Model**: Utilizes a CNN architecture to analyze and classify chest X-ray images.
- **Web Application**: Provides a user-friendly interface for uploading X-ray images and viewing classification results.
- **Automated Detection**: Predicts pneumonia presence with high accuracy based on trained medical image data.

## Installation

To set up the project locally, follow these steps:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/Bosha-a/Pneumonia-Classifier.git
   cd Pneumonia-Classifier
   ```

2. **Create and activate a virtual environment**:
   ```bash
   python -m venv env
   source env/bin/activate  # On Windows: env\Scripts\activate
   ```

3. **Install the required dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

## Model Training

The model was trained using a dataset of labeled chest X-ray images. The training process involved:

- **Data Preprocessing**: Resizing images, normalization, and augmentation to enhance model robustness.
- **Model Architecture**: Implementing a CNN with layers optimized for feature extraction from medical images.
- **Evaluation**: Assessing model performance using metrics such as accuracy, precision, recall, and F1-score.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgements

- **Dataset**: The chest X-ray images used for training and evaluation were sourced from reputable medical imaging repositories.
- **Inspiration**: This project was inspired by the need for accessible tools to assist in the early detection of pneumonia

