import os
import openai

openai.api_key = "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"

response = openai.Completion.create(
  model="babbage:ft-personal-2023-03-17-10-52-31",
  prompt="what is Mobius DTaas",
  temperature=0.7,
  max_tokens=100,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)
print(response["choices"][0]["text"])