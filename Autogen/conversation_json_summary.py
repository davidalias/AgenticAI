import json
from autogen.agentchat import ConversableAgent
from llm_config import llm_config

# Define a custom summarization agent
class SummarizationAgent(ConversableAgent):
    def summarize_json_with_tables(self, json_data: str) -> str:
        # Parse JSON string
        data = json.loads(json_data)
        conversation = data.get("conversation", [])

        # Build formatted conversation text
        formatted_conversation = []
        for turn in conversation:
            user_input = turn.get("user", "")
            system_response = turn.get("assistant", {})
            content = system_response.get("content", {})
            text = content.get("text", "")
            table = content.get("table", {})

            formatted_conversation.append(f"User: {user_input}")
            formatted_conversation.append(f"Assistant: {text}")

            # Format table if present
            if table:
                headers = table.get("headers", [])
                rows = table.get("rows", [])
                table_md = "| " + " | ".join(headers) + " |\n"
                table_md += "| " + " | ".join(["---"] * len(headers)) + " |\n"
                for row in rows:
                    table_md += "| " + " | ".join(map(str, row)) + " |\n"
                formatted_conversation.append("Assistant Table:\n" + table_md)

        # Combine all into a single prompt
        conversation_text = "\n".join(formatted_conversation)
        prompt = f"""Conversation:{conversation_text}"""
        
        # Get response from the agent
        response = self.generate_reply(messages=[{"role": "user", "content": prompt}])
        return response

# Instantiate the agent
summarizer = SummarizationAgent(
    name="SummarizerAgent",
    system_message="""You are a cybersecurity analyst who summarize conversations and presents key data in a professional tone within 1-2 sentences.               
                      If there are tables present, for each table provide:
                      - Column-wise statistics (mean, median for numeric columns)
                      - Any notable observations
                      - Include them in markdown format""",
  
    llm_config= llm_config # Replace with your model config
)


# Example JSON conversation
json_conversation = """
{
  "conversation": [
    {
      "user": "Show threats with highest priority",
      "assistant": {
        "type": "mixed",
        "content": {
          "text": "SELECT threat_name, priority from threat ORDERBY priority DESC",
          "table": {
            "headers": ["threat_name", "priority"],
            "rows": [
              ["Threat A", 1],
              ["Threat B", 1],
              ["Threat C", 1],
              ["Threat D", 0],
              ["Threat E", 0],
              ["Threat F", 0]
            ]
          }
        }
      }
    },
    {
      "user": "Which of those threats were detected within 48h?",
      "assistant": {
        "type": "mixed",
        "content": {
          "text": "SELECT threat_name, priority from threat WHERE event_time >= NOW() - INTERVAL '48' HOUR ORDERBY priority DESC;",
          "table": {
            "headers": ["threat_name", "priority"],
            "rows": [
              ["Threat C", 1],
              ["Threat B", 1],
              ["Threat D", 0]
            ]
          }
        }
      }
    }
  ]
}

"""

# Generate summary
summary = summarizer.summarize_json_with_tables(json_conversation)
print("Conversation Summary:\n", summary)
