from collections import OrderedDict, Counter
import numpy as np
import feat_gen
import glob

def gen():
    # filenames = ['firstname.5k', 'lastname.5000', 'location', 'location.country', 'cap.1000', 'automotive.make', 'automotive.model', 'book.newspaper',
    # 'broadcast.tv_channel', 'business.brand', 'business.consumer_company', 'business.consumer_product', 'government.government_agency', 'sports.sports_team', 'time.holiday', 'lower.10000']
    # filenames = ['data/lexicon/' + filename for filename in filenames]
    filenames = Counter(glob.glob("data/lexicon/*"))
    for name in ['cap.10', 'cap.100', 'cap.500', 'firstname.10', 'firstname.100', 'firstname.500', 'firstname.1000', 'lastname.10', 'lastname.100','lastname.500', 'lastname.1000', 'lower.100', 'lower.500', 'lower.1000', 'lower.5000', 'dictionaries.conf']:
        key = 'data/lexicon/' + name
        del filenames[key]
    filenames = filenames.keys()
    for filename in filenames:
        vars()[filename[13:]] = OrderedDict()
        f = open(filename, "r")
        words = f.readlines()
        for word in words:
            vars()[filename[13:]][word.strip().lower()] = 1
        np.save("lexicon_features/" + filename[13:], vars()[filename[13:]])


if __name__ == "__main__":
    gen()