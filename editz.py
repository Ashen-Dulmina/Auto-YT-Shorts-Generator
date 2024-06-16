from moviepy.editor import VideoFileClip, TextClip, AudioFileClip, CompositeAudioClip, afx
	
def EditVid(background_clip, text, text_duration, text_color, text_size, background_song, background_voice):
	init_clip_0 = VideoFileClip(background_clip)
	txt_added_clip = TextClip(text,fontsize=text_size,color=text_color).set_pos('center').set_duration(text_duration)
	voice = AudioFileClip(voiceover).fx(afx.audio_fadein, 1)
	bgm = AudioFileClip(background_song).fx(afx.audio_fadein, 1).fx(afx.volumex, 0.2)
	final = CompositeVideoClip([txt_clip, init_clip_0])
	final.audio = CompositeAudioClip([voice, bgm])
	final.write_videofile("Output.mp4")