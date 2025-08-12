from moviepy.editor import *
import os

def make(config, topic):
    # Check if voiceover exists
    if not os.path.exists("assets/voiceover.mp3"):
        print("❌ No voiceover found. Skipping video creation.")
        return

    audio = AudioFileClip("assets/voiceover.mp3")
    duration = audio.duration

    # Use a placeholder video (you can replace with Pexels download logic)
    # For now, you'll need to add a file: assets/stock.mp4
    if not os.path.exists("assets/stock.mp4"):
        print("⚠️ No stock video found. Use a 9:16 video named 'stock.mp4' in assets/")
        # Create silent color clip as fallback
        video = ColorClip(size=(1080, 1920), color=(0, 0, 0), duration=duration)
    else:
        video = VideoFileClip("assets/stock.mp4").subclip(0, duration)
        video = video.resize(height=1920)  # 9:16 for Reels

    # Add subtitle
    txt_clip = TextClip(
        "AI News Daily", fontsize=60, color='white',
        size=video.size, method='caption', align='center'
    ).set_duration(duration)

    final = CompositeVideoClip([video, txt_clip.set_position('center')])
    final = final.set_audio(audio)

    final.write_videofile(
        "assets/final_video.mp4",
        fps=24,
        codec='libx264',
        audio_codec='aac',
        temp_audiofile='temp-audio.m4a',
        remove_temp=True
    )
    print("✅ Video created: final_video.mp4")
