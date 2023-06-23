import sys
from src.exception import CustomException
from src.logger import logging
from src.pipeline.train_pipeline import TrainPipeline

train_obj = TrainPipeline()
train_obj.run_pipeline()