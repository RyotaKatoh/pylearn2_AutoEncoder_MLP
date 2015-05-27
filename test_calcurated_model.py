import numpy as np
import pickle
import theano
from pylearn2.datasets.dogcat_dataset import DogCatDataset


if __name__ == "__main__":
    model = pickle.load(open('dae_mlp.pkl'))
    test_data = DogCatDataset("test")

    results = model.fprop(theano.shared(test_data.X)).eval()

    nCorrect = 0
    for result, label in zip(results, test_data.y):
        if np.argmax(result) == np.argmax(label):
            nCorrect += 1

    print '%d / %d' %(nCorrect, len(test_data.X))
