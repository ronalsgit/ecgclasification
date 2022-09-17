import enum

DATASET = 'shayanfazeli/heartbeat'
FILENAMES = ['mitbih_test.csv', 'mitbih_train.csv', 'ptbdb_abnormal.csv', 'ptbdb_normal.csv']
FILENAMES = FILENAMES[0]
ARCHIVE_TYPE = '.ZIP'

class MODE(enum):
    READ = 'r'
    WRITE = 'W'
    READ_WRITE = 'rw'
class message:
    FILE_NOT_EXIST = 'The file does not exist'