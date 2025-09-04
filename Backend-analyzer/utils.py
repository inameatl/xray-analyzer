import re
from typing import Dict
from PIL import Image
import torch
from torchvision import transforms

# Disease keyword dictionary
DISEASE_KEYWORDS = {
    'COVID': [
        ('covid', 10), ('coronavirus', 10), ('sars-cov-2', 10),
        ('ground glass', 8), ('bilateral', 7), ('ggo', 8),
        ('peripheral', 6), ('pandemic', 5), ('respiratory', 4)
    ],
    'Normal': [
        ('normal', 10), ('clear', 8), ('healthy', 8),
        ('no abnormality', 9), ('unremarkable', 7),
        ('regular', 5), ('typical', 5), ('within normal limits', 8)
    ],
    'Viral Pneumonia': [
        ('viral', 10), ('influenza', 8), ('flu', 7),
        ('rsv', 8), ('patchy', 7), ('consolidation', 7),
        ('interstitial', 6), ('bilateral', 5), ('viral infection', 8)
    ],
    'Lung_Opacity': [
        ('opacity', 10), ('density', 8), ('shadow', 7),
        ('infiltrate', 8), ('consolidation', 7),
        ('mass', 8), ('nodule', 8), ('lesion', 7), ('abnormal', 6)
    ]
}

CLASS_NAMES = list(DISEASE_KEYWORDS.keys())


# 🔹 Image prediction
def predict_image(image: Image.Image, model, device, class_names=CLASS_NAMES):
    transform = transforms.Compose([
        transforms.Resize((224, 224)),
        transforms.ToTensor(),
        transforms.Normalize([0.485, 0.456, 0.406],
                             [0.229, 0.224, 0.225])
    ])

    tensor = transform(image).unsqueeze(0).to(device)

    with torch.no_grad():
        outputs = model(tensor).logits
        probs = torch.softmax(outputs, dim=1)
        pred = torch.argmax(probs, dim=1).item()

    return class_names[pred], float(probs[0][pred])


# 🔹 Text comment prediction
def predict_from_comment(comment: str, disease_keywords=DISEASE_KEYWORDS) -> Dict:
    comment_lower = comment.lower()
    scores = {d: 0 for d in disease_keywords}
    matched = {d: [] for d in disease_keywords}

    for disease, keywords in disease_keywords.items():
        for keyword, weight in keywords:
            if re.search(r'\b' + re.escape(keyword) + r'\b', comment_lower):
                scores[disease] += weight
                matched[disease].append((keyword, weight))

    best_disease = max(scores.items(), key=lambda x: x[1])[0]
    total_score = scores[best_disease]

    return {
        "predicted_disease": best_disease,
        "scores": scores,
        "matched_keywords": matched,
        "confidence": min(total_score / 50 * 100, 100)
    }
