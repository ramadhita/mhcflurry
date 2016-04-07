import numpy as np

from dummy_predictors import always_zero_predictor_with_unknown_AAs


def test_always_zero_9mer_inputs():

    test_9mer_peptides = [
        "SIISIISII",
        "AAAAAAAAA",
    ]

    n_expected = len(test_9mer_peptides)
    y = always_zero_predictor_with_unknown_AAs.predict_peptides(test_9mer_peptides)
    assert len(y) == n_expected
    assert np.all(y == 0)

    # call the predict method for 9mers directly
    y = always_zero_predictor_with_unknown_AAs.predict_9mer_peptides(test_9mer_peptides)
    assert len(y) == n_expected
    assert np.all(y == 0)

    ic50 = always_zero_predictor_with_unknown_AAs.predict_peptides_ic50(test_9mer_peptides)
    assert len(y) == n_expected
    assert np.all(ic50 == always_zero_predictor_with_unknown_AAs.max_ic50), ic50


def test_always_zero_8mer_inputs():
    test_8mer_peptides = [
        "SIISIISI",
        "AAAAAAAA",
    ]

    n_expected = len(test_8mer_peptides)
    y = always_zero_predictor_with_unknown_AAs.predict_peptides(test_8mer_peptides)
    assert len(y) == n_expected
    assert np.all(y == 0)

    ic50 = always_zero_predictor_with_unknown_AAs.predict_peptides_ic50(test_8mer_peptides)
    assert len(y) == n_expected
    assert np.all(ic50 == always_zero_predictor_with_unknown_AAs.max_ic50), ic50


def test_always_zero_10mer_inputs():

    test_10mer_peptides = [
        "SIISIISIYY",
        "AAAAAAAAYY",
    ]

    n_expected = len(test_10mer_peptides)
    y = always_zero_predictor_with_unknown_AAs.predict_peptides(test_10mer_peptides)
    assert len(y) == n_expected
    assert np.all(y == 0)

    ic50 = always_zero_predictor_with_unknown_AAs.predict_peptides_ic50(test_10mer_peptides)
    assert len(y) == n_expected
    assert np.all(ic50 == always_zero_predictor_with_unknown_AAs.max_ic50), ic50


def test_encode_peptides_9mer():
    X = always_zero_predictor_with_unknown_AAs.encode_9mer_peptides(["AAASSSYYY"])
    assert X.shape[0] == 1, X.shape
    assert X.shape[1] == 9, X.shape

    X, indices = always_zero_predictor_with_unknown_AAs.encode_peptides(["AAASSSYYY"])
    assert len(indices) == 1
    assert indices[0] == 0
    assert X.shape[0] == 1, X.shape
    assert X.shape[1] == 9, X.shape


def test_encode_peptides_8mer():
    X, indices = always_zero_predictor_with_unknown_AAs.encode_peptides(["AAASSSYY"])
    assert len(indices) == 9
    assert (indices == 0).all()
    assert X.shape[0] == 9, (X.shape, X)
    assert X.shape[1] == 9, (X.shape, X)


def test_encode_peptides_10mer():
    X, indices = always_zero_predictor_with_unknown_AAs.encode_peptides(["AAASSSYYFF"])
    assert len(indices) == 10
    assert (indices == 0).all()
    assert X.shape[0] == 10, (X.shape, X)
    assert X.shape[1] == 9, (X.shape, X)
