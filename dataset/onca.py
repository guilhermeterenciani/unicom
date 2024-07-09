# https://github.com/htdt/hyp_metric/blob/master/proxy_anchor/dataset/cub.py
from .base import *

from .base import *


class Onca(BaseDataset):
    def __init__(self, root, mode, transform = None):
        self.root = root + '/Dataset'
        self.mode = mode
        self.transform = transform

        

        if self.mode == 'train':
            self.classes = range(0,7)
        elif self.mode == 'eval':
            self.classes = range(0,7)

        BaseDataset.__init__(self, self.root, self.mode, self.transform)
        metadata = open(os.path.join(self.root, 'train.csv' if self.mode == 'train' else 'test.csv'))
        metadata = [line.strip('\n').split(',') for line in metadata]
        for i, (image_id, class_id, _, path) in enumerate(metadata):
            if int(class_id) in self.classes:
                self.ys += [int(class_id)]
                self.I += [int(image_id)]
                self.im_paths.append(os.path.join(path))
