from processor_regex import classify_with_regex
from processor_bert import classify_with_bert
from processor_llm import classify_with_llm
import pandas as pd

def classify(logs):
    labels = []
    for source, log in logs:
        label = classify_log(source, log)
        labels.append(label)
    return labels

def classify_log(source, log_message):
    if source == "LegacyCRM":
        label = classify_with_llm(log_message)
    else:
        label = classify_with_regex(log_message)
        if label is None:
            label = classify_with_bert(log_message)
    return label

def classify_csv(input_file):
    df = pd.read_csv(input_file)

    df['target_label'] = classify(list(zip(df['source'], df['log_message'])))
    
    output_file = "resources/output.csv"
    df.to_csv(output_file, index=False)


if __name__ == "__main__":
    classify_csv("resources/test.csv")
    logs = [
        ("ModernCRM","User User123 logged in."),
        ("BillingSystem","Backup started at 12:00"),
        ("AnalyticsEngine","Backup completed successfully."),
        ("ModernHR", "Admin access escalation detected for user 9429"),
        ("LegacyCRM", "Case escalation for ticket ID 7324 failed because the assigned support agent is no longer active."),
        ("LegacyCRM", "Invoice generation process aborted for order ID 8910 due to invalid tax calculation module.")
    ]

    classified_logs = classify(logs)
    print(classified_logs)