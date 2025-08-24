# AI Story Generator
# Generative AI Internship Project
# Author: Nitesh Singh Farswan

from transformers import pipeline

def generate_story(prompt):
    # Load GPT-2 model
    generator = pipeline("text-generation", model="gpt2")

    # Generate story
    story = generator(prompt, max_length=200, num_return_sequences=1, do_sample=True, temperature=0.8)
    
    return story[0]['generated_text']

if __name__ == "__main__":
    print("🌟 Welcome to AI Story Generator 🌟")
    user_prompt = input("Enter your story idea: ")
    print("\n📖 Generated Story:\n")
    print(generate_story(user_prompt))
