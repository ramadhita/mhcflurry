import time

from mhcflurry.allele_encoding import AlleleEncoding
from mhcflurry.amino_acid import BLOSUM62_MATRIX
from nose.tools import eq_
from numpy.testing import assert_equal
import numpy
import pandas


def test_allele_encoding_speed():
    encoding = AlleleEncoding(
        ["A*02:01", "A*02:03", "A*02:01"],
        {
            "A*02:01": "AC",
            "A*02:03": "AE",
        }
    )
    start = time.time()
    encoding1 = encoding.fixed_length_vector_encoded_sequences("BLOSUM62")
    assert_equal(
        [
            [BLOSUM62_MATRIX["A"], BLOSUM62_MATRIX["C"]],
            [BLOSUM62_MATRIX["A"], BLOSUM62_MATRIX["E"]],
            [BLOSUM62_MATRIX["A"], BLOSUM62_MATRIX["C"]],
        ], encoding1)
    print("Simple encoding in %0.2f sec." % (time.time() - start))
    print(encoding1)

    encoding = AlleleEncoding(
        ["A*02:01", "A*02:03", "A*02:01"] * int(1e5),
        {
            "A*02:01": "AC" * 16,
            "A*02:03": "AE" * 16,
        }
    )
    start = time.time()
    encoding1 = encoding.fixed_length_vector_encoded_sequences("BLOSUM62")
    print("Long encoding in %0.2f sec." % (time.time() - start))


def test_pca():
    encoding = AlleleEncoding(
        ["A*02:01", "A*02:03", "A*02:01"],
        {
            "A*02:01": "AC",
            "A*02:03": "AE",
        }
    )
    encoded1 = encoding.fixed_length_vector_encoded_sequences(
        "transform:pca:BLOSUM62")

    numpy.testing.assert_array_equal(encoded1[0], encoded1[2])
    assert not numpy.array_equal(encoded1[0], encoded1[1])
    print(encoded1)