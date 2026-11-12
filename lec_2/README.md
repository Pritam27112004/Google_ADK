# Build Your First Google ADK Agent: Setup, LiteLLM Swapping & Web UI (https://www.youtube.com/watch?v=gFA9fKOOqhc)

1.Create folder and open inside VS Code 

 

2.Create virtual env - python -m venv .venv 

3.Activate - .venv\Scripts\Activate.ps1 

 

4.Install google adk - pip install google-adk 

 

5.adk command -> Check adk version - adk --version 

 

6.Create agent project - adk create campusx_bot 

 

7.Get Gemini API key 

 

8.Run the agent - adk run campusx_bot 

 

9.Run the web interface - adk web 

 

10.Run the api service - adk api_server 

 

11.Run with other models 

pip install litellm (using litellm you can connect with 100+ LLM providers who profide fast response so no need to change code)

Add -> model=LiteLlm(model="openai/gpt-4o") 

Get openai api key and add to .env 

 

12.Add model config  

generate_content_config=types.GenerateContentConfig(  

temperature=0.3, # lower = more consistent support answers max_output_tokens=800 

) 