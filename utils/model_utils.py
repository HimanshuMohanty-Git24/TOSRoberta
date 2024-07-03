import torch

def predict_unfairness(text, model, tokenizer):
    inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True, max_length=512)
    
    model.eval()
    with torch.no_grad():
        outputs = model(**inputs)
    
    probabilities = torch.softmax(outputs.logits, dim=-1).squeeze()
    predicted_class = torch.argmax(probabilities).item()
    
    label_mapping = {0: 'clearly_fair', 1: 'potentially_unfair', 2: 'clearly_unfair'}
    predicted_label = label_mapping[predicted_class]
    
    return predicted_label, probabilities.tolist()