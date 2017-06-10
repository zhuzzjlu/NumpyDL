# -*- coding: utf-8 -*-


import pytest
import numpy as np
from npdl.layers import Embedding


def test_embed_words():
    embed_words = np.random.rand(100, 10)

    # static == False
    layer = Embedding(embed_words)

    assert len(layer.params) == 1
    assert len(layer.grads) == 1
    assert len(layer.param_grads) == 1

    # static == True
    layer = Embedding(embed_words, True)

    with pytest.raises(NotImplementedError):
        layer.forward(None)

    with pytest.raises(NotImplementedError):
        layer.backward(None)

    assert len(layer.params) == 0
    assert len(layer.grads) == 0
    assert len(layer.param_grads) == 0


def test_no_embed_words():
    # static == False
    layer = Embedding(input_size=100, n_out=10)

    assert len(layer.params) == 1
    assert len(layer.grads) == 1
    assert len(layer.param_grads) == 1

    # static == True
    layer = Embedding(static=True, input_size=100, n_out=10)

    assert len(layer.params) == 0
    assert len(layer.grads) == 0
    assert len(layer.param_grads) == 0
