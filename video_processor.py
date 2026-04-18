from moviepy.editor import VideoFileClip

def process_video(input_path):
    clip = VideoFileClip(input_path)
    
    # Example: cut first 10 seconds
    short_clip = clip.subclip(0, 10)
    
    output_path = "output.mp4"
    short_clip.write_videofile(output_path)
    
    return output_path