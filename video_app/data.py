from dataclasses import dataclass

@dataclass
class CapturedVideo:
        name: str= "None"
        width: str= "None"
        height: str= "None"
        resolution: int= 0
        frame_rate: str= "None"
        number_of_frames: str="None"
    