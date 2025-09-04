import torch
from transformers import ResNetForImageClassification

# Path to your trained model weights
MODEL_PATH = r"C:\code\xray\models\covid_resnet50.pth"

# Class names (must match your training)
CLASS_NAMES = ['COVID', 'Normal', 'Viral Pneumonia', 'Lung_Opacity']

# Select device
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# Load pretrained ResNet-50 and apply your trained weights
checkpoint = torch.load(MODEL_PATH, map_location=device)

model = ResNetForImageClassification.from_pretrained(
    "microsoft/resnet-50",
    num_labels=len(CLASS_NAMES),
    ignore_mismatched_sizes=True
)

model.load_state_dict(checkpoint['model_state_dict'])
model.to(device)
model.eval()
