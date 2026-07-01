from sentence_transformers import SentenceTransformer
import joblib

transformer_model = SentenceTransformer("all-MiniLM-L6-v2")
classify_model = joblib.load("models/log_classifier.joblib")

def classify_with_bert(log_message):
    
    message_embedding = transformer_model.encode(log_message) #compute embedding for the input log
    probabilities = classify_model.predict_proba([message_embedding])[0]
    if max(probabilities>0.5):
        #classification
        predicted_class = classify_model.predict([message_embedding])[0]
        return predicted_class
    else:
        return "Unclassified"

if __name__=="__main__":
    logs = [
        "System crashed due to driver errors when starting the server",
        "Hey bro, chill yo",
        "Multiple login failures occured on user 6454 account",
        "Server A790 was restarted unexpectedly during the process of data transfer"
    ]

    for log in logs:
        label = classify_with_bert(log)
        print(log, "->", label)

