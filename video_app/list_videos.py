from capable_video.video_app.public.models import Video

def list_all():
    return Video.query.all()
             
    

