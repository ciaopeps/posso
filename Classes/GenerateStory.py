from Classes.main import *
from Classes.globals import *
import os
import requests
# import argparse

def to_app():
    print('to app')
    title, article = send_story()
    D[title] = article

# def load_model():
#
#
#     model_type = "mega"
#
#     model_dir = os.path.join('../grover/models', model_type)
#     print(model_dir)
#     if not os.path.exists(model_dir):
#         print('creating folder')
#         os.makedirs(model_dir)
#
#     for ext in ['data-00000-of-00001', 'index', 'meta']:
#         print('downloading model file ==> ', ext)
#         r = requests.get(f'https://storage.googleapis.com/grover-models/{model_type}/model.ckpt.{ext}', stream=True)
#         with open(os.path.join(model_dir, f'model.ckpt.{ext}'), 'wb') as f:
#             file_size = int(r.headers["content-length"])
#             if file_size < 1000:
#                 raise ValueError("File doesn't exist? idk")
#             chunk_size = 1000
#             for chunk in r.iter_content(chunk_size=chunk_size):
#                 f.write(chunk)
#         print(f"Just downloaded {model_type}/model.ckpt.{ext}!", flush=True)