from my_package import myModule

def test_top_n():
    '''
    makes sure top_n works correctly
    '''

    assert myModule.top_n ([8, 3, 2, 7, 4], 3) == [8, 7, 4], "Incorrect"
    assert myModule.top_n ([30, 40, 2, 7, 4], 2) == [40, 30], "Incorrect"
    assert myModule.top_n ([1, 3, 2], 1) == [3], "Incorrect"
