audio_folder = r"C:\Users\Admin\Documents\projects\PROSNAL_VAI\Voice_training\train"
test_audio_file = r"C:\Users\Admin\Documents\projects\PROSNAL_VAI\Voice_training\test\tarak.wav"


import numpy as np
import os
import librosa
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.preprocessing import LabelEncoder

# Function to extract audio features from a file
def extract_features(file_path):
    try:
        # Load the audio file using librosa
        audio, _ = librosa.load(file_path, sr=None)
        # Extract MFCC (Mel-frequency cepstral coefficients) features
        mfccs = librosa.feature.mfcc(y=audio, sr=16000, n_mfcc=13)
        return np.mean(mfccs.T, axis=0)
    except Exception as e:
        print(f"Error extracting features from {file_path}: {str(e)}")
        return None

# Function to collect audio features and labels from a directory
def collect_features_and_labels(directory):
    features = []
    labels = []
    for subdir in os.listdir(directory):
        if os.path.isdir(os.path.join(directory, subdir)):
            for filename in os.listdir(os.path.join(directory, subdir)):
                if filename.endswith('.wav'):
                    file_path = os.path.join(directory, subdir, filename)
                    label = subdir
                    feature = extract_features(file_path)
                    if feature is not None:
                        features.append(feature)
                        labels.append(label)
    return features, labels


if __name__ == "__main__":
    # Replace 'path/to/audio/directory' with the path to your labeled audio data
    audio_directory = audio_folder

    # Collect audio features and labels
    features, labels = collect_features_and_labels(audio_directory)
    print('Total Training sample: ', len(features))

    # Encode the labels
    label_encoder = LabelEncoder()
    encoded_labels = label_encoder.fit_transform(labels)

    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(features, encoded_labels, test_size=0.2, random_state=42)

    # Train an SVM classifier
    clf = SVC(kernel='linear')
    clf.fit(X_train, y_train)



    # testing
    # Perform speaker recognition on a test feature
    test_feature = extract_features(test_audio_file)  # Replace with your test audio file
    predicted_label = clf.predict([test_feature])
    print('predicted_label: ', predicted_label)

    # Map the predicted label back to the original speaker name
    predicted_speaker = label_encoder.inverse_transform(predicted_label)
    print('predicted_speaker: ', predicted_speaker)

    print(f"Recognized speaker: {predicted_speaker[0]}")
