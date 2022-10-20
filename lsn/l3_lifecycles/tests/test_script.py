from lsn.l3_lifecycles.tests.utils import SetUpTest, SetUpClassTest, TearDownTest, TearDownClassTest, Jerry, Universes


# TODO : this is how to initiiiiiiiitialize jerry = Jerry(origin=Universes.some_universe)

class TestJerryBoree(SetUpTest):
    # TODO: tests are already set up,
    #  i need a to waaa(:burp:)y to populate initial data
    #  note to self: should proobably use setUp to do so
    pass


class TestJerryBoreeCloningMachine(SetUpClassTest):
    # TODO: same jazz here,
    #  in case i ever lose a jerry miiight be a good idea to clone him into each jerry-boree instance
    #  in case i need to run several tests
    #  note to self: should proobably use setUpClass to do so
    pass


class TestJerryBoreeReturnMechanism(TearDownTest):
    # TODO: after tests are done should probably let them go wherever
    #  note to self: should proobably use tearDown to do so
    pass


class TestJerryBoreeReturnMechanismCloningMachine(TearDownClassTest):
    # TODO: almost forgot, should do the same for cloning machine tests
    #  note to self: should proobably use tearDownClass to do so
    pass
