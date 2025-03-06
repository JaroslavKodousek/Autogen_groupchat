Here’s the improved version with clearer wording, consistency, and minor fixes:  

---

# AutoGen Script  

## Overview  
This repository contains a Python-based AutoGen script that utilizes three different agents to generate responses automatically.  

## Setup  

1. **Configure Your API Key**  
   Set your OpenAI API key in `autogen_config.json`:  

   ```json
   {
       "api_key": "YOUR_OPENAI_API_KEY",
       "model": "gpt-4",
       "temperature": 0.7,
       "max_tokens": 1000,
       "top_p": 1.0,
       "frequency_penalty": 0.0,
       "presence_penalty": 0.0
   }
   ```  

2. **Modify the Input Message**  
   Specify your desired message in `autogen_groupchat.py` by editing the script:  

   ```python
   # Initiate the chat
   user_proxy.initiate_chat(
       manager,
       message="Compare Apple stocks with Microsoft stocks over the past year."
   )
   ```  
