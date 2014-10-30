from .. import blank_space_remover, stl_converter
bsr=blank_space_remover.bsr
stl=stl_converter.stl
import pytest

@pytest.mark.bsr
def test_remove_space_from_beginning_and_end():
    word = '     aaa    '
    word = bsr(word)
    assert word == 'aaa'

@pytest.mark.stl
def test_stl():
    word1 = 'one, two, three'
    word1 = stl(word1)

    word2 = '   one,,,two, thr ee   '
    word2 = stl(word2)

    word3 = ''
    word3=stl(word3)
    
    assert word1 == ['one','two','three']
    assert word2 == ['one','two','thr ee']
    assert word3 == []
