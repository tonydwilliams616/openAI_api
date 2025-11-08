# 🧠 ChatGPT API Connection Test — Image Generation Example

This repository contains example Python scripts that test connections to the **OpenAI API** using the `openai` Python client.  
Each file demonstrates different functionalities such as text generation, image generation, and handling responses from the ChatGPT models.

---

## 📄 Example: `generate_image.py`

This script demonstrates how to generate a **photorealistic image** using OpenAI’s image generation models (`gpt-image-1` or `dall-e-3`).  
It connects to the OpenAI API, sends a prompt, downloads the generated image, and saves it locally.

### 🧰 Features
- Connects to the OpenAI API.
- Sends a creative image prompt.
- Retrieves the generated image URL.
- Downloads and saves the image to disk.
- Optionally displays the generated image using Pillow (`PIL`).

---

## ⚙️ Requirements

Before running, make sure you have the following installed:

```bash
python >= 3.8
openai >= 1.0.0
requests
pillow