# Audio to Text - Text to Audio

A powerful application that combines Speech-to-Text and Text-to-Speech capabilities using state-of-the-art AI models.

## Features

- **Speech to Text**: Convert audio files to text using NVIDIA's Parakeet ASR model
- **Text to Speech**: Convert text to natural-sounding speech using Suno's Bark model
- **PDF Support**: Extract text from PDF files and convert it to speech
- **User-friendly Interface**: Built with Gradio for easy interaction

## Installation

1. Clone this repository:

```bash
<<<<<<< HEAD
git clone https://github.com/yourusername/audio-to-text-and-text-to-audio.git
cd audiotext
=======
git clone https://github.com/fatihberkanteren/audio-to-text-and-text-to-audio.git
cd audio-to-text-and-text-to-audio
>>>>>>> 2c26e71 (docs: add example audio file information to README)
```

2. Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Usage

Run the application:

```bash
python audiotext.py
```

The application will start a local web server and provide a URL where you can access the interface.

## Example

You can test the Speech-to-Text functionality using this example audio file:

```bash
wget https://dldata-public.s3.us-east-2.amazonaws.com/2086-149220-0033.wav
```

This is a sample audio file that you can use to test the transcription capabilities of the application.

## Requirements

- Python 3.8 or higher
- CUDA-compatible GPU (recommended for better performance)

## License

MIT License
