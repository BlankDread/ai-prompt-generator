import random

def generate_prompt():
    subjects = ["a majestic lion", "a futuristic cityscape", "a hidden forest glade", "a steam punk robot", "a mythical dragon"]
    styles = ["in a photorealistic style", "as a watercolor painting", "in a pixel art style", "with vibrant neon colors", "in a dark, moody atmosphere"]
    actions = ["contemplating the sunset", "exploring ancient ruins", "engaged in an epic battle", "flying through the clouds", "casting a powerful spell"]

    subject = random.choice(subjects)
    style = random.choice(styles)
    action = random.choice(actions)

    prompt = f"{subject} {action}, {style}."
    return prompt
if __name__ == "__main__":
    print("Welcome to AI Prompt Generator!")
    generated_prompt = generate_prompt()
    print("\nHere are the generated prompt:")
    print(generated_prompt)
    print("\nFeel free to use this with your favorite AI image generator!")