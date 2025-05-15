import gradio as gr
from bark import SAMPLE_RATE, generate_audio, preload_models
from scipy.io.wavfile import write as write_wav
from IPython.display import Audio
import nemo.collections.asr as nemo_asr
import numpy as np
from PyPDF2 import PdfReader

# Initialize ASR model
asr_model = nemo_asr.models.ASRModel.from_pretrained(
    model_name="nvidia/parakeet-tdt-0.6b-v2"
)


def get_transcript(audio_file):
    return asr_model.transcribe([audio_file])[0].text


def extract_pdf_text(file):
    reader = PdfReader(file)
    text = ""
    for page in reader.pages:
        text += page.extract_text() + "\n" 
    return text.strip()


def text_to_speech(text, isText, pdf_file):
    if isText:
        full_text = text
    else:
        full_text = extract_pdf_text(pdf_file)

    audio = generate_audio(full_text, history_prompt="v2/en_speaker_1")
    write_wav("bark_full_conversation.wav", SAMPLE_RATE, audio)

    return "bark_full_conversation.wav"


def create_interface():
    with gr.Blocks(gr.themes.Base()) as interface:
        gr.Markdown("## 🎤 Speech to Text")
        with gr.Row():
            audio_file = gr.File(label="Upload an audio file (.wav, .mp3)")
            text_output = gr.Textbox(label="Transcription", lines=4)

        with gr.Row():
            t_button = gr.Button("Transcribe")
            clear_stt = gr.Button("Clear")
        t_button.click(fn=get_transcript, inputs=audio_file, outputs=text_output)
        clear_stt.click(lambda: (None, ""), outputs=[audio_file, text_output])

        gr.Markdown("---")

        gr.Markdown("## 🗣️ Text to Speech")

        with gr.Row():
            text_input = gr.Textbox(label="Enter text to convert to speech", lines=9)
            pdf_file = gr.File(label="Upload a PDF file")
        checkbox = gr.Checkbox(label="✅ Use this text instead of uploading a PDF")

        audio_output = gr.Audio(label="Generated Speech")

        with gr.Row():
            audio_button = gr.Button("Generate Speech")
            clear_tts = gr.Button("Clear")

        audio_button.click(
            fn=text_to_speech,
            inputs=[text_input, checkbox, pdf_file],
            outputs=audio_output,
        )

        clear_tts.click(
            lambda: ("", False, None, None),
            outputs=[text_input, checkbox, pdf_file, audio_output],
        )

    return interface


if __name__ == "__main__":
    interface = create_interface()
    interface.launch(share=True)
