import math
import sys
from google import genai
from google.genai import types
from PIL import Image
from io import BytesIO
import pathlib
from moviepy import VideoFileClip, CompositeVideoClip, ImageClip, TextClip, AudioFileClip, concatenate_videoclips
from gtts import gTTS


# Function to read API, prevents all users from committing code with hard coded key
def get_api_key(file_path: str) -> str:
    with open(file_path, 'r') as file:
        return file.readline().strip()

def generate_image(promtp:str)->Image:

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
        return image

def generate_audio (summary:str, path:str)->None:
    tts = gTTS(summary)
    tts.save(path)


def create_video_with_overlay(gameplay_video_path, overlay_image_path, overlay_text, audio_path):
    # Load gameplay video and extract a 60-second segment
    video = VideoFileClip(gameplay_video_path).subclipped(start_time=0, end_time=60)

    # Load narration audio
    audio = AudioFileClip(audio_path)
    # Calculate the number of loops needed
    loops_required = math.ceil(audio.duration / video.duration)

    # Concatenate the video to loop it
    if loops_required > 1:
        video = concatenate_videoclips([video] * loops_required)
    video = video.subclipped(0, audio.duration)  # Trim to exactly match audio duration

    # Load overlay image and set duration directly in the constructor
    image_clip = ImageClip(overlay_image_path, duration=video.duration)
    image_clip = image_clip.resized(height=400).with_position(("center", 250))

    # Combine video, image overlay, caption, and audio
    final_video = CompositeVideoClip([video, image_clip])
    final_video = final_video.with_audio(audio)

    # Export the final video
    final_video.write_videofile("final_output.mp4", fps=60)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    key = get_api_key("API_KEY.txt")
    client = genai.Client(api_key=key)


    if len(sys.argv) < 3:
        print("Error: No PDF file path provided or brainrot mode selected.")
        sys.exit(1)
    pdf_path = sys.argv[1]
    brainrot_mode = sys.argv[2]
    filepath = pathlib.Path(pdf_path)
    brainrot_mode = brainrot_mode.strip()
    brainrot_mode = int(brainrot_mode)
    print(brainrot_mode)

    if brainrot_mode == 1:
        prompt = "I have given you a PDF that outlines an academic concept. I want you to create a detailed summary of the" \
                 "content into a text that can be read in 60 seconds. The summary should include critical information and" \
                 "specific examples mentioned in the pdf. You do not need to add extra words or formatting, simply give the" \
                 "output as described. Use excessive Gen Z lingo in your summary to engage the younger audience."

    else:
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

    index = arr[0].find(".") + 3
    prompt = arr[0][index:]

    generated_image = generate_image(prompt)

    generated_image_path = "image.png"
    generated_image.save(generated_image_path);

    audio_path = "audio.mp3"
    generate_audio(summary.text, audio_path);

    gameplay_video_path = "Download.mp4"

    create_video_with_overlay(gameplay_video_path, generated_image_path, summary.text, audio_path)

    print ("Video generated")

