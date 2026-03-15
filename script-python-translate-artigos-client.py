from langchain_openai.chat_models.azure import AzureChatOpenAI

client = AzureChatOpenAI(
    azure_endpoint="https://oai-dev-eastus-001.openai.azure.com/",
    api_key="",
    api_version="2024-02-15-preview",
    deployment_name="gpt-4o-mini",
    max_retries=0
)

def translate_article(text, lang):
    messages = [
        ("system" , "Você atua como tradutor de textos"),
        ("user", f"Traduza o {text} para o idioma {lang} e responda em markdown")
    ]

    response = client.invoke(messages)
    print(response.content)
    return response.content

translate_article("Let's see if the deployment was succeeded.", "portugues")
