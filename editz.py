from moviepy.editor import VideoFileClip, TextClip, AudioFileClip, CompositeAudioClip, afx, CompositeVideoClip
	
print("Movie PY Wakeup Call -- OKI !")

def EditVid(background_clip, background_song, background_voice):
	init_clip_0 = VideoFileClip(background_clip)
	voice = AudioFileClip(background_voice).fx(afx.audio_fadein, 1)
	bgm = AudioFileClip(background_song).fx(afx.audio_fadein, 1).fx(afx.volumex, 0.1)
	final = CompositeVideoClip([init_clip_0])
	final.audio = CompositeAudioClip([voice, bgm])
	final.write_videofile("Output.mp4")