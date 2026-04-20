# engine_ner.py

from gliner import GLiNER

# 1. Load the template
model = GLiNER.from_pretrained("urchade/gliner_medium-v2.1")

def clean_with_gliner(text):
    # 2. We define which categories of PII we want to find.
    labels = ["person", "email", "phone number", "address", "birthday"]
    
    # 3. GLiNER finds the entities
    entities = model.predict_entities(text, labels, threshold=0.5)
    
    # 4. The "Backwards Replacement" Technique
    # Important: If we start from the beginning, the indexes at the end of the text change!
    # Therefore, we order from the highest index to the lowest.
    
    anonymized = text
    for ent in sorted(entities, key=lambda x: x['start'], reverse=True):
        start = ent['start']
        end = ent['end']
        label = ent['label'].upper()
        anonymized = anonymized[:start] + f"[{label}]" + anonymized[end:]
        
    return anonymized

    # Display predicted entities and their labels
    #for entity in entities:
    #    print(entity["text"], "=>", entity["label"])

if __name__ == "__main__":
    sample_text = """
    My name is Alexandre Silva Rodrigues Neves Lachat and my email is alex.silva@outlook.com. 
    I live in Lisbon, at Rua das Flores 123. My phone is +351 912 345 678.
    """
    
    result = clean_with_gliner(sample_text)
    
    print("\n--- ANONYMOUS TEXT ---")
    print(result)