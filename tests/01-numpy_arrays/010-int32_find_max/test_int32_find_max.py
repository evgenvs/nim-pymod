import array_utils
import numpy
import pytest


def test_0_compile_pymod_test_mod(pmgen_py_compile):
        pmgen_py_compile(__name__)


ndims_to_test = [1, 2, 3, 4]


# for loop, values

@pytest.mark.parametrize("ndim", ndims_to_test)
def test_int32FindMaxForLoopValues(pymod_test_mod, seeded_random_number_generator, ndim):
    arg = array_utils.get_random_Nd_array_of_ndim_and_type(ndim, numpy.int32)
    print ("\nrandom number seed = %d\nndim = %d, shape = %s\narg =\n%s" % \
            (seeded_random_number_generator, ndim, arg.shape, arg))
    expectedRes = arg.max()
    res = pymod_test_mod.int32FindMaxForLoopValues(arg)
    print ("res = %s" % str(res))
    assert res == expectedRes


# while loop, Forward Iter

@pytest.mark.parametrize("ndim", ndims_to_test)
def test_int32FindMaxWhileLoopForwardIter(pymod_test_mod, seeded_random_number_generator, ndim):
    arg = array_utils.get_random_Nd_array_of_ndim_and_type(ndim, numpy.int32)
    print ("\nrandom number seed = %d\nndim = %d, shape = %s\narg =\n%s" % \
            (seeded_random_number_generator, ndim, arg.shape, arg))
    expectedRes = arg.max()
    res = pymod_test_mod.int32FindMaxWhileLoopForwardIter(arg)
    print ("res = %s" % str(res))
    assert res == expectedRes


# for loop, Forward Iter

@pytest.mark.parametrize("ndim", ndims_to_test)
def test_int32FindMaxForLoopForwardIter(pymod_test_mod, seeded_random_number_generator, ndim):
    arg = array_utils.get_random_Nd_array_of_ndim_and_type(ndim, numpy.int32)
    print ("\nrandom number seed = %d\nndim = %d, shape = %s\narg =\n%s" % \
            (seeded_random_number_generator, ndim, arg.shape, arg))
    expectedRes = arg.max()
    res = pymod_test_mod.int32FindMaxForLoopForwardIter(arg)
    print ("res = %s" % str(res))
    assert res == expectedRes


# while loop, Rand Acc Iter

@pytest.mark.parametrize("ndim", ndims_to_test)
def test_int32FindMaxWhileLoopRandaccIterDeref(pymod_test_mod, seeded_random_number_generator, ndim):
    arg = array_utils.get_random_Nd_array_of_ndim_and_type(ndim, numpy.int32)
    print ("\nrandom number seed = %d\nndim = %d, shape = %s\narg =\n%s" % \
            (seeded_random_number_generator, ndim, arg.shape, arg))
    expectedRes = arg.max()
    res = pymod_test_mod.int32FindMaxWhileLoopRandaccIterDeref(arg)
    print ("res = %s" % str(res))
    assert res == expectedRes

@pytest.mark.parametrize("ndim", ndims_to_test)
def test_int32FindMaxWhileLoopRandaccIterIndex0(pymod_test_mod, seeded_random_number_generator, ndim):
    arg = array_utils.get_random_Nd_array_of_ndim_and_type(ndim, numpy.int32)
    print ("\nrandom number seed = %d\nndim = %d, shape = %s\narg =\n%s" % \
            (seeded_random_number_generator, ndim, arg.shape, arg))
    expectedRes = arg.max()
    res = pymod_test_mod.int32FindMaxWhileLoopRandaccIterIndex0(arg)
    print ("res = %s" % str(res))
    assert res == expectedRes

@pytest.mark.parametrize("ndim", ndims_to_test)
def test_int32FindMaxWhileLoopRandaccIterDerefPlusZeroOffset(pymod_test_mod, seeded_random_number_generator, ndim):
    arg = array_utils.get_random_Nd_array_of_ndim_and_type(ndim, numpy.int32)
    print ("\nrandom number seed = %d\nndim = %d, shape = %s\narg =\n%s" % \
            (seeded_random_number_generator, ndim, arg.shape, arg))
    expectedRes = arg.max()
    res = pymod_test_mod.int32FindMaxWhileLoopRandaccIterDerefPlusZeroOffset(arg)
    print ("res = %s" % str(res))
    assert res == expectedRes

@pytest.mark.parametrize("ndim", ndims_to_test)
def test_int32FindMaxWhileLoopRandaccIterDerefMinusZeroOffset(pymod_test_mod, seeded_random_number_generator, ndim):
    arg = array_utils.get_random_Nd_array_of_ndim_and_type(ndim, numpy.int32)
    print ("\nrandom number seed = %d\nndim = %d, shape = %s\narg =\n%s" % \
            (seeded_random_number_generator, ndim, arg.shape, arg))
    expectedRes = arg.max()
    res = pymod_test_mod.int32FindMaxWhileLoopRandaccIterDerefMinusZeroOffset(arg)
    print ("res = %s" % str(res))
    assert res == expectedRes

