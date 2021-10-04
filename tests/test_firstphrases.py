#!/usr/bin/env python
# -*- coding: utf-8 -*-

from spacy.tokens import Doc
from spacy.vocab import Vocab

import os
import pke

valid_pos = {'NOUN', 'PROPN', 'ADJ'}
test_file = os.path.join('tests', 'data', '1939.doc')
doc = Doc(Vocab()).from_disk(test_file)


def test_firstphrases_candidate_selection():
    extractor = pke.unsupervised.FirstPhrases()
    extractor.load_document(input=doc)
    extractor.candidate_selection(pos=valid_pos)
    assert len(extractor.candidates) == 20


def test_firstphrases_candidate_weighting():
    extractor = pke.unsupervised.FirstPhrases()
    extractor.load_document(input=doc)
    extractor.candidate_selection(pos=valid_pos)
    extractor.candidate_weighting()
    keyphrases = [k for k, s in extractor.get_n_best(n=3)]
    assert keyphrases == ['compatibility', 'systems', 'linear constraints']


if __name__ == '__main__':
    test_firstphrases_candidate_selection()
    test_firstphrases_candidate_weighting()
