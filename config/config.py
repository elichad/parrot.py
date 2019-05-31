import pyaudio
import pyautogui
pyautogui.FAILSAFE = False

FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100
CHUNK = 1024
RECORD_SECONDS = 0.05
TEMP_FILE_NAME = "play.wav"
PREDICTION_LENGTH = 10
SILENCE_INTENSITY_THRESHOLD = 400
INPUT_DEVICE_INDEX = 1

DATASET_FOLDER = "data/recordings"
RECORDINGS_FOLDER = "data/recordings"
REPLAYS_FOLDER = "data/replays"
REPLAYS_AUDIO_FOLDER = "data/replays/audio"
REPLAYS_FILE = REPLAYS_FOLDER + "/run.csv"
CLASSIFIER_FOLDER = "data/models"
OVERLAY_FOLDER = "data/overlays"
OVERLAY_FILE = "config/current-overlay-image.txt"
DEFAULT_CLF_FILE = "train_narud_complete2"

STARTING_MODE = "starcraft"

SAVE_REPLAY_DURING_PLAY = True
SAVE_FILES_DURING_PLAY = False
EYETRACKING_TOGGLE = "F4"
SPEECHREC_ENABLED = True
OVERLAY_ENABLED = True