import time
import numpy as np
from PIL import Image
import tensorflow as tf


# Function to load labels
def load_labels(path):
    with open(path, "r") as f:
        return {int(line.split()[0]): line.split()[1] for line in f.readlines()}


# Function to preprocess image
def preprocess_image(image_path, input_size):
    image = Image.open(image_path).convert("RGB")
    image = image.resize(input_size)
    image = np.array(image)
    image = np.expand_dims(image, axis=0)
    image = image / 255.0
    return image


# Function to evaluate model
def evaluate_model(model, label_path, image_paths, input_size):
    labels = load_labels(label_path)
    total_time = 0
    correct_predictions = 0

    for image_path in image_paths:
        image = preprocess_image(image_path, input_size)

        start_time = time.time()
        predictions = model.predict(image)
        inference_time = time.time() - start_time

        total_time += inference_time

        predicted_label = np.argmax(predictions[0])

        print(
            f"Image: {image_path}, Predicted: {labels[predicted_label]}, Time: {inference_time:.4f} seconds"
        )

        # Assuming ground truth label is in the file name (e.g., cat_1.jpg)
        ground_truth = image_path.split("/")[-1].split("_")[0]

        if labels[predicted_label] == ground_truth:
            correct_predictions += 1

    accuracy = correct_predictions / len(image_paths)
    average_time = total_time / len(image_paths)

    return average_time, accuracy


# Paths to models, labels, and validation images
model_paths = {
    "mobilenetv2": tf.keras.applications.MobileNetV2(weights="imagenet"),
    "xception": tf.keras.applications.Xception(weights="imagenet"),
    "efficientnet": tf.keras.applications.EfficientNetB0(weights="imagenet"),
}
label_path = "labels.txt"
image_paths = ["path_to_image1.jpg", "path_to_image2.jpg"]  # Add your image paths here

input_sizes = {
    "mobilenetv2": (224, 224),
    "xception": (299, 299),
    "efficientnet": (224, 224),
}

log = {}

# Evaluate all models
for model_name, model in model_paths.items():
    print(f"Evaluating {model_name}...")
    avg_time, accuracy = evaluate_model(
        model, label_path, image_paths, input_sizes[model_name]
    )
    log[model_name] = {"average_time_per_image": avg_time, "accuracy": accuracy}
    print(
        f"{model_name} - Average Time: {avg_time:.4f} seconds, Accuracy: {accuracy:.4f}"
    )

# Save log to a file
import json

with open("model_evaluation_log.json", "w") as f:
    json.dump(log, f, indent=4)

print("Evaluation complete. Log saved to model_evaluation_log.json")
