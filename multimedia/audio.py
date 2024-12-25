from telegram import Audio

def send_audio_question(update, context):
    question = "Identify the sound in the audio file."
    audio_path = "multimedia_files/audio_sample.mp3"

    with open(audio_path, "rb") as audio_file:
        update.message.reply_audio(audio=audio_file, caption=question)
