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
    from moviepy.editor import *
import os
from .download_background import download_background  # ← New import

def make(config, topic):
    # Check if voiceover exists
    if not os.path.exists("assets/voiceover.mp3"):
        print("❌ No voiceover found. Skipping video creation.")
        return

    audio = AudioFileClip("assets/voiceover.mp3")
    duration = audio.duration

    # --- 🔥 REPLACEMENT: Auto-download background video ---
    bg_video_path = download_background(config, topic)
    if not bg_video_path:
        print("❌ No background video. Using black screen.")
        video = ColorClip(size=(1080, 1920), color=(0, 0, 0), duration=duration)
    else:
        try:
            video = VideoFileClip(bg_video_path).subclip(0, duration)
            video = video.resize(height=1920)  # Ensure 9:16 (Instagram Reels)
        except Exception as e:
            print("⚠️ Video load failed, using fallback:", e)
            video = ColorClip(size=(1080, 1920), color=(0, 0, 0), duration=duration)
    # --- END OF REPLACEMENT ---

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
