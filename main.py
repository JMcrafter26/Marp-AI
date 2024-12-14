
from ollama import chat
from ollama import Client
import os

# Generate markdown presentation using the Ollama API and Marp CLI
def generate_presentation(topic, style):
    prompt = f"""Create a presentation on {topic} in the marp presentation markdown format. Example for the topic "Python":
    ```
    ---
    title: Python
    theme: {style}
    ---

    # Python

    Python is an interpreted high-level general-purpose programming language.

    ---

    # Table of Contents

    - Introduction
    - Features
    - Applications
    - Conclusion
    
    ---

    # Introduction

    Python is a versatile programming language that can be used for many different types of projects.

    It is known for its readability and ease of use which makes it a great language for beginners and experts alike.

    ---

    # Features

    - Easy to learn
    - Open-source
    - Cross-platform
    - Object-oriented
    - Extensive libraries

    ---

    # Applications

    Python is used in many different fields such as:

    - Web development
    - Data science
    - Machine learning
    - Automation
    - Game development

    ---

    # Conclusion

    Python is a powerful language that can be used for a wide variety of projects.

    It is a great language to learn for beginners and experts alike.
    
    ```

    Marp supports most of the features of the markdown language and allows you to create beautiful presentations with ease.
    It also supports math equations, images, and code blocks.
    IMPORTANT: Do not put more than 500 words or more than 8 bullet points on one slide, split the content into multiple slides if necessary.

    """

    client = Client(
        host='http://localhost:11434',
        # headers={'x-some-header': 'some-value'}
    )
    response = client.chat(
        messages=[
            {
                'role': 'system',
                'content': prompt,
            },
            {
                'role': 'user',
                'content': topic,
            }
        ],
        model='llama3.2:3b',
    )

    # print(response)
    # save the response to a markdown file
    with open(topic + '.md', 'w') as f:
        f.write(response['message']['content'])

# convert the markdown presentation to a PDF
def convert_to_pdf(topic):
    # if os is windows
    if os.name == 'nt':
        try:
            os.system(f'marp.exe "{topic}.md" --pdf')
        except Exception as e:
            print(e)
    elif os.name == 'posix':
        try:
            os.system(f'marp "{topic}.md" --pdf')
        except Exception as e:
            print(e)
    return f"{topic}.pdf"


def main():
    if os.name == 'nt' and not os.path.exists('marp.exe') or os.name == 'posix' and not os.path.exists('marp'):
        print("Marp CLI not found. Please download and install Marp CLI from https://github.com/marp-team/marp-cli/releases and place the executable in the 'marp' folder.")
        return

    topic = input("Enter the topic for the presentation: ")
    # topic = "Ancient Egypt" # for testing
    style = 'uncover' # Available styles: 'default', 'gaia' and 'uncover'

    print(f"\nGenerating presentation on {topic}...")
    print(f"--Please always check the generated presentation for accuracy and completeness!--")
    presentation = generate_presentation(topic, style)
    print(f"Presentation generated successfully!")
    print(f"Converting presentation to PDF...")
    pdfFile = convert_to_pdf(topic)
    print(f"\n\nPresentation saved to {pdfFile}")

if __name__ == '__main__':
    main()