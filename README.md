# 💬 X-Ray Comment Analyzer

A web application that allows users to upload chest X-ray images, describe what they see, and receive AI feedback comparing their analysis to a trained deep learning model. Built with **FastAPI**, **React**, and **Tailwind CSS**.

---

## 🏗 Features

- Upload X-ray images (PNG, JPG, JPEG).  
- Enter your textual analysis of the X-ray.  
- AI predicts disease from the image using **ResNet-50**.  
- Comment analysis matches keywords against common disease patterns.  
- Highlights matches and provides a confidence score.  
- Displays educational feedback if the analysis and AI prediction differ.  
- Responsive frontend with **Tailwind CSS**.  

---

## 🧩 Supported Diseases

- **COVID-19** – Bilateral ground glass opacities, peripheral distribution.  
- **Normal** – Clear lung fields, no abnormalities.  
- **Viral Pneumonia** – Patchy bilateral opacities, interstitial patterns.  
- **Lung Opacity** – Focal consolidations, shadows, or nodules.  

---

## ⚡ Tech Stack

- **Backend:** FastAPI, PyTorch, Transformers, Pillow.  
- **Frontend:** React, Tailwind CSS, Axios.  
- **Machine Learning:** ResNet-50 fine-tuned on X-ray dataset.  

---

## 📂 ⚙️ Installation

### Backend

```bash
cd backend
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
pip install -r requirements.txt
uvicorn main:app --reload

### frontend

cd frontend
npm install
npm run dev



