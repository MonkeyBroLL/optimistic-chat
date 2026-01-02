import os

from langchain.chat_models import init_chat_model

def create_deepseek_model(temperature: float):
    """
    Create a DeepSeek chat model with the specified temperature.
    
    Args:
        temperature (float): The temperature parameter for the model
        
    Returns:
        A chat model instance configured with the specified temperature
    """
    return init_chat_model(
        model="deepseek-chat",
        api_key=os.environ.get('DEEPSEEK_API_KEY'),
        base_url="https://api.deepseek.com",
        temperature=temperature
    )