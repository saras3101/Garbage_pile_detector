from inference import InferencePipeline
from inference.core.interfaces.stream.sinks import render_boxes

pipeline = InferencePipeline.init(
    model_id="garbage-can-overflow/1",
    video_reference="1093402459-preview.mp4",
    on_prediction=render_boxes
)

pipeline.start()
pipeline.join()