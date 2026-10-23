# Serverless Image Processing Pipeline (AWS S3 & Lambda)

An automated, serverless image processing pipeline built on **Amazon S3** and **AWS Lambda (Python 3.11 + Pillow)**. When an image is uploaded to the source S3 bucket, it automatically triggers a Lambda function that resizes/converts the image and stores the processed output.

---

## 🏗️ Architecture Flow

1. **Upload:** User or application uploads an image to the **Source S3 Bucket**.
2. **Trigger:** S3 generates an `ObjectCreated` event notification that automatically triggers the **AWS Lambda Function**.
3. **Process:** The Lambda function reads the image stream into memory, applies transformations (e.g., thumbnail resizing via **Pillow**), and formats the output.
4. **Store:** The processed image is saved into the destination folder/bucket.

---

## 📁 Repository Structure

```text
image-processing-pipeline/
├── lambda_function.py        # Core Python execution logic for image processing
├── requirements.txt          # Python dependencies (Pillow)
├── build_layer.sh            # Shell script to package dependencies into a Lambda Layer
└── README.md                 # Project documentation
