import os

# vars
CLASSIFIER_TYPE = 'multi'
NUM_EPOCHS = 3
BATCH_SIZE = 32
NUM_FOLDS = 3
OPTIMIZER = 'adam'
VERBOSE = 1

# data names
DATASET_NAME = 'CICIDS2018'
name = '_optimized_' + CLASSIFIER_TYPE + '.pkl' 
X_test_name = CLASSIFIER_TYPE + '_X_test.pkl'
y_test_name = CLASSIFIER_TYPE + '_y_test.pkl'

# paths
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
DATASET_DIR = os.path.join(ROOT_DIR, "datasets")
MODEL_DIR = os.path.join(ROOT_DIR, "saved_models")
DATA_DIR = os.path.join(ROOT_DIR, "main", DATASET_NAME, 'data')
PICKLE_DIR = os.path.join(ROOT_DIR, DATASET_NAME)
OPTIMIZED_DATASET_PATH = os.path.join(DATASET_DIR, DATASET_NAME, DATASET_NAME + name)

# print colors
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'