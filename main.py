import dataReader
import tensorflow as tf


def main():
    print(dataReader.useME())
    print("hey")
    # Call the function with the path to your TensorFlow file
    databasePath = 'dataset/next_day_wildfire_spread_train_00.tfrecord'
   # dataReader.print_tfrecord(databasePath)
    dataReader.print_tfrecord_keys(databasePath)

def print_tensorflow_file_content(databasePath):
    reader = tf.data.TFRecordDataset(databasePath)

    for key in reader:
        print(repr(key))


if __name__ == '__main__':
    main()

