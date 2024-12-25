from telegram import Video

def send_video_question(update, context):
    question = "Watch the video and answer the question."
    video_path = "multimedia_files/video_sample.mp4"

    with open(video_path, "rb") as video_file:
        update.message.reply_video(video=video_file, caption=question)
