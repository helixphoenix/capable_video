
from capable_video.video_app.database import Column, db


class Video(db.Model):
    __tablename__ = "videos"
    id=Column(db.Integer, primary_key=True)
    name = Column(db.String(80), unique=True, nullable=False)
    width = Column(db.String(80),  nullable=False)
    height = Column(db.String(80),  nullable=False)
    resolution = Column(db.String(80), nullable=False)
    frame_rate = Column(db.String(80), nullable=False)
    number_of_frames = Column(db.String(80), nullable=True)