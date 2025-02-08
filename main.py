from google import genai
from google.genai import types
from PIL import Image
from io import BytesIO
import pathlib
import moviepy as mp
from gtts import gTTS


# Function to read API, prevents all users from commiting code with hard coded key
def get_api_key(file_path: str) -> str:
    with open(file_path, 'r') as file:
        return file.readline().strip()

def generate_image(promtp:str)->None:

    generated_prompt = prompt + " *- NO TEXT PLEASE"

    response = client.models.generate_images(
        model='imagen-3.0-generate-002',
        prompt=generated_prompt,
        config=types.GenerateImagesConfig(
            number_of_images=1,
        )
    )
    for generated_image in response.generated_images:
        image = Image.open(BytesIO(generated_image.image.image_bytes))
        image.show()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    key = get_api_key("API_KEY.txt")

    client = genai.Client(api_key=key)

    # Read the PDF file as bytes
    filepath = pathlib.Path("CSP-1.pdf")

    prompt = "I have given you a PDF that outlines an academic concept. I want you to create a detailed summary of the" \
             "content into a text that can be read in 60 seconds. The summary should include critical information and" \
             "specific examples mentioned in the pdf. You do not need to add extra words or formatting, simply give the" \
             "output as described."

    # Send the PDF and prompt to Gemini API
    summary = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=[
            types.Part.from_bytes(
                data=filepath.read_bytes(),
                mime_type='application/pdf',
            ),
            prompt
        ]
    )

    prompt = "I am going to give a summary of an academical concept. I want you to analyze it and give " \
             "me 5 key ideas that I can use to generate images relevant to the content. Keep it simple " \
             "and use general language. Limit your output to 20 words max" \
             "Give you output as an ordered list" + summary.text

    chat = client.chats.create(model="gemini-2.0-flash")

    generated_prompts = chat.send_message(prompt)

    prompt = "Rank you outputs 1-5 based on relevance to the subject of the academic summary."

    ranked_output = chat.send_message(prompt)

    arr = ranked_output.text.split("\n");
    arr.pop(0)
    arr.pop(0)
    print(arr)

    index = arr[0].find(".") + 3
    prompt = arr[0][index:]

    generate_image(prompt)

    print(prompt)
