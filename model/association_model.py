from abc import ABC

import torch
import torchvision
from transformers import pipeline
from datetime import datetime

from model.processing_model_base import ProcessingModelBase

print(torch.__version__)
print(torchvision.__version__)

with open('./model/association_dict.txt', 'r') as dict_file:
    CANDIDATE_LABELS = dict_file.read().split("\n")


MODEL_NAME = 'cross-encoder/nli-distilroberta-base'

MODEL = pipeline("zero-shot-classification", model=MODEL_NAME)


class AssociationModel(ProcessingModelBase, ABC):
    def __init__(self):
        super().__init__()

    def process_data(self, sequence_to_classify):
        started_time = datetime.now()
        predict = MODEL(sequence_to_classify, CANDIDATE_LABELS, multi_label=True)

        result = [predict['labels'][i] for i in range(len(predict['labels'])) if predict['scores'][i] > 0.9]

        ended_time = datetime.now()
        print(f'TIME:{ended_time - started_time}')

        return [{'name': tag} for tag in result]

