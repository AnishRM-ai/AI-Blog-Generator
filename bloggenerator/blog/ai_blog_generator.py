# blog/ai_blog_generator.py
import openai

def generate_blog_content(title):
    openai.api_key = 'your_openai_api_key'
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=f"Write a blog post about {title}",
        max_tokens=500
    )
    content = response.choices[0].text.strip()
    return content
