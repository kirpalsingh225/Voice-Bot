from transformers import pipeline
from datasets import load_dataset
import soundfile as sf
import torch
import sounddevice as sd

synthesiser = pipeline("text-to-speech", "microsoft/speecht5_tts")

embeddings_dataset = load_dataset("Matthijs/cmu-arctic-xvectors", split="validation")
speaker_embedding = torch.tensor(embeddings_dataset[7306]["xvector"]).unsqueeze(0)
# You can replace this embedding with your own as well.

def speak_text(text):
    """
    Generate speech from text and play it in real time.
    Returns the audio array and sampling rate.
    """
    speech = synthesiser(text, forward_params={"speaker_embeddings": speaker_embedding})
    sd.play(speech["audio"], speech["sampling_rate"])
    sd.wait()
    return speech["audio"], speech["sampling_rate"]


