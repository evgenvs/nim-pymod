import numpy
import pytest
import time


def test_0_compile_pymod_test_mod(pmgen_py_compile):
        pmgen_py_compile(__name__)


@pytest.fixture(scope="module")
def seeded_random_number_generator():
    """Ensure that the random number generator has been seeded."""
    numpy.random.seed(int(time.time()))


@pytest.fixture
def random_1d_array_size(seeded_random_number_generator):
    """Return a random integer in the range [1, 20] to be the size of a 1-D array."""
    return numpy.random.randint(20) + 1  # So the size is always >= 1.

@pytest.fixture
def random_1d_array_of_bool(random_1d_array_size):
    """Return a randomly-sized array of random bool values."""
    return numpy.random.random_integers(0, 1, random_1d_array_size).astype(numpy.bool)

@pytest.fixture
def random_1d_array_of_integers(random_1d_array_size):
    """Return a randomly-sized 1-D array of random integers in the range [-100, 100]."""
    return numpy.random.random_integers(-100, 100, random_1d_array_size)

def _get_random_1d_array_of_type(test_1d_array_size, test_type):
    """Return a randomly-sized 1-D array of random integers in the range [-100, 100]."""
    return numpy.random.random_integers(-100, 100, test_1d_array_size
            ).astype(test_type)


@pytest.fixture
def random_2d_array_shape(seeded_random_number_generator):
    """Return a tuple of 2 random integers in the range [1, 10] to be the shape of a 2-D array."""
    dim1 = numpy.random.randint(10) + 1  # So the size is always >= 1.
    dim2 = numpy.random.randint(10) + 1  # So the size is always >= 1.
    return (dim1, dim2)

@pytest.fixture
def random_2d_array_of_integers(random_2d_array_shape):
    """Return a randomly-shaped 2-D array of random integers in the range [-100, 100]."""
    array_size = numpy.prod(random_2d_array_shape)
    return numpy.random.random_integers(-100, 100, array_size).reshape(random_2d_array_shape)

def _get_random_2d_array_of_type(test_2d_array_shape, test_type):
    """Return a randomly-shaped 2-D array of random integers in the range [-100, 100]."""
    array_size = numpy.prod(test_2d_array_shape)
    return numpy.random.random_integers(-100, 100, array_size).reshape(test_2d_array_shape
            ).astype(test_type)


@pytest.fixture
def random_3d_array_shape(seeded_random_number_generator):
    """Return a tuple of 3 random integers in the range [1, 10] to be the shape of a 3-D array."""
    dim1 = numpy.random.randint(10) + 1  # So the size is always >= 1.
    dim2 = numpy.random.randint(10) + 1  # So the size is always >= 1.
    dim3 = numpy.random.randint(10) + 1  # So the size is always >= 1.
    return (dim1, dim2, dim3)

@pytest.fixture
def random_4d_array_shape(seeded_random_number_generator):
    """Return a tuple of 4 random integers in the range [1, 10] to be the shape of a 4-D array."""
    dim1 = numpy.random.randint(10) + 1  # So the size is always >= 1.
    dim2 = numpy.random.randint(10) + 1  # So the size is always >= 1.
    dim3 = numpy.random.randint(10) + 1  # So the size is always >= 1.
    dim4 = numpy.random.randint(10) + 1  # So the size is always >= 1.
    return (dim1, dim2, dim3, dim4)

def _get_random_Nd_array_of_type(test_Nd_array_shape, test_type):
    """Return a randomly-shaped N-D array of random integers in the range [-100, 100]."""
    array_size = numpy.prod(test_Nd_array_shape)
    return numpy.random.random_integers(-100, 100, array_size).reshape(test_Nd_array_shape
            ).astype(test_type)


@pytest.mark.parametrize("input_type", [
        numpy.bool,
        numpy.bool_,
        numpy.int8,
        numpy.int16,
        numpy.int32,
        numpy.int64,
        numpy.uint8,
        numpy.uint16,
        numpy.uint32,
        numpy.uint64,
        numpy.float32,
        numpy.float64,
])
def test_returnPyArrayObjectPtrAsInt(pymod_test_mod, random_1d_array_size, input_type):
    arg = numpy.zeros(random_1d_array_size, dtype=input_type)
    res = pymod_test_mod.returnPyArrayObjectPtrAsInt(arg)
    assert res == id(arg)


@pytest.mark.parametrize("input_type,input_type_str", [
        # NOTE:  Pymod returns the type string "<type 'numpy.bool'>" rather than "<type 'bool'>",
        # which is what `str(numpy.bool)` returns in Python.
        # Pymod returns "<type 'numpy.bool'>" for consistency with all other Numpy type strings,
        # which are all of the form "<type 'numpy.xxxx'>" (eg, "<type 'numpy.int8'>").
        (numpy.bool,    "numpy.bool"),
        (numpy.bool_,   "numpy.bool"),
        (numpy.int8,    "numpy.int8"),
        (numpy.int16,   "numpy.int16"),
        (numpy.int32,   "numpy.int32"),
        (numpy.int64,   "numpy.int64"),
        (numpy.uint8,   "numpy.uint8"),
        (numpy.uint16,  "numpy.uint16"),
        (numpy.uint32,  "numpy.uint32"),
        (numpy.uint64,  "numpy.uint64"),
        (numpy.float32, "numpy.float32"),
        (numpy.float64, "numpy.float64"),
])
def test_returnDtypeAsString(pymod_test_mod, random_1d_array_size, input_type, input_type_str):
    arg = numpy.zeros(random_1d_array_size, dtype=input_type)
    res = pymod_test_mod.returnDtypeAsString(arg)
    assert res == input_type_str


def _get_array_data_address(arr):
    # It took me a long time to find out how to access the `arr.data` address
    # (ie, obtain the actual `arr.data` pointer as an integer) in Python!
    # If you simply invoke `arr.data` in Python, it returns you a temporary
    # intermediate buffer object, that has a different memory address!
    data_addr = arr.__array_interface__["data"][0]
    return data_addr


@pytest.mark.parametrize("input_type", [
        numpy.bool,
        numpy.bool_,
        numpy.int8,
        numpy.int16,
        numpy.int32,
        numpy.int64,
        numpy.uint8,
        numpy.uint16,
        numpy.uint32,
        numpy.uint64,
        numpy.float32,
        numpy.float64,
])
def test_returnDataPointerAsInt(pymod_test_mod, random_1d_array_size, input_type):
    arg = numpy.zeros(random_1d_array_size, dtype=input_type)
    res = pymod_test_mod.returnDataPointerAsInt(arg)
    data_addr = _get_array_data_address(arg)
    assert res == data_addr


def test_returnBoolDataPtrAsInt(pymod_test_mod, random_1d_array_size):
    arg = numpy.zeros(random_1d_array_size, dtype=numpy.bool)
    res = pymod_test_mod.returnBoolDataPtrAsInt(arg)
    data_addr = _get_array_data_address(arg)
    assert res == data_addr

def test_returnInt8DataPtrAsInt(pymod_test_mod, random_1d_array_size):
    arg = numpy.zeros(random_1d_array_size, dtype=numpy.int8)
    res = pymod_test_mod.returnInt8DataPtrAsInt(arg)
    data_addr = _get_array_data_address(arg)
    assert res == data_addr

def test_returnInt16DataPtrAsInt(pymod_test_mod, random_1d_array_size):
    arg = numpy.zeros(random_1d_array_size, dtype=numpy.int16)
    res = pymod_test_mod.returnInt16DataPtrAsInt(arg)
    data_addr = _get_array_data_address(arg)
    assert res == data_addr

def test_returnInt32DataPtrAsInt(pymod_test_mod, random_1d_array_size):
    arg = numpy.zeros(random_1d_array_size, dtype=numpy.int32)
    res = pymod_test_mod.returnInt32DataPtrAsInt(arg)
    data_addr = _get_array_data_address(arg)
    assert res == data_addr

def test_returnInt64DataPtrAsInt(pymod_test_mod, random_1d_array_size):
    arg = numpy.zeros(random_1d_array_size, dtype=numpy.int64)
    res = pymod_test_mod.returnInt64DataPtrAsInt(arg)
    data_addr = _get_array_data_address(arg)
    assert res == data_addr

def test_returnFloat32DataPtrAsInt(pymod_test_mod, random_1d_array_size):
    arg = numpy.zeros(random_1d_array_size, dtype=numpy.float32)
    res = pymod_test_mod.returnFloat32DataPtrAsInt(arg)
    data_addr = _get_array_data_address(arg)
    assert res == data_addr

def test_returnFloat64DataPtrAsInt(pymod_test_mod, random_1d_array_size):
    arg = numpy.zeros(random_1d_array_size, dtype=numpy.float64)
    res = pymod_test_mod.returnFloat64DataPtrAsInt(arg)
    data_addr = _get_array_data_address(arg)
    assert res == data_addr


#def test_returnBoolDataPtrIndex0(pymod_test_mod, random_1d_array_of_bool):
#    arg = random_1d_array_of_bool.copy()
#    expectedRes = bool(arg[0])
#    res = pymod_test_mod.returnBoolDataPtrIndex0(arg)
#    assert res == expectedRes
#    assert type(res) == type(expectedRes)

#def test_returnInt8DataPtrIndex0(pymod_test_mod, random_1d_array_of_integers):
#    arg = random_1d_array_of_integers.astype(numpy.int8)
#    expectedRes = int(arg[0])
#    res = pymod_test_mod.returnInt8DataPtrIndex0(arg)
#    assert res == expectedRes
#    assert type(res) == type(expectedRes)

def test_returnInt16DataPtrIndex0(pymod_test_mod, random_1d_array_of_integers):
    arg = random_1d_array_of_integers.astype(numpy.int16)
    expectedRes = int(arg[0])
    res = pymod_test_mod.returnInt16DataPtrIndex0(arg)
    assert res == expectedRes
    assert type(res) == type(expectedRes)

def test_returnInt32DataPtrIndex0(pymod_test_mod, random_1d_array_of_integers):
    arg = random_1d_array_of_integers.astype(numpy.int32)
    expectedRes = int(arg[0])
    res = pymod_test_mod.returnInt32DataPtrIndex0(arg)
    assert res == expectedRes
    assert type(res) == type(expectedRes)

def test_returnInt64DataPtrIndex0(pymod_test_mod, random_1d_array_of_integers):
    arg = random_1d_array_of_integers.astype(numpy.int64)
    expectedRes = int(arg[0])
    res = pymod_test_mod.returnInt64DataPtrIndex0(arg)
    assert res == expectedRes
    assert type(res) == type(expectedRes)

def test_returnFloat32DataPtrIndex0(pymod_test_mod, random_1d_array_of_integers):
    arg = random_1d_array_of_integers.astype(numpy.float32)
    expectedRes = float(arg[0])
    res = pymod_test_mod.returnFloat32DataPtrIndex0(arg)
    assert res == expectedRes
    assert type(res) == type(expectedRes)

def test_returnFloat64DataPtrIndex0(pymod_test_mod, random_1d_array_of_integers):
    arg = random_1d_array_of_integers.astype(numpy.float64)
    expectedRes = float(arg[0])
    res = pymod_test_mod.returnFloat64DataPtrIndex0(arg)
    assert res == expectedRes
    assert type(res) == type(expectedRes)


@pytest.mark.parametrize("input_type", [
        numpy.bool,
        numpy.bool_,
        numpy.int8,
        numpy.int16,
        numpy.int32,
        numpy.int64,
        numpy.uint8,
        numpy.uint16,
        numpy.uint32,
        numpy.uint64,
        numpy.float32,
        numpy.float64,
])
def test_returnNdAttr_1d(pymod_test_mod, input_type, random_1d_array_size):
    arg = _get_random_1d_array_of_type(random_1d_array_size, input_type)

    resNd = pymod_test_mod.returnNdAttr(arg)
    assert resNd == len(arg.shape)
    assert resNd == arg.ndim

    resNdim = pymod_test_mod.returnNdimAttr(arg)
    assert resNdim == len(arg.shape)
    assert resNdim == arg.ndim


@pytest.mark.parametrize("input_type", [
        numpy.bool,
        numpy.bool_,
        numpy.int8,
        numpy.int16,
        numpy.int32,
        numpy.int64,
        numpy.uint8,
        numpy.uint16,
        numpy.uint32,
        numpy.uint64,
        numpy.float32,
        numpy.float64,
])
def test_returnDimensionsAsTuple1D(pymod_test_mod, input_type, random_1d_array_size):
    arg = _get_random_1d_array_of_type(random_1d_array_size, input_type)
    expectedDimensions = arg.shape
    expectedShape = arg.shape

    resDimensions = pymod_test_mod.returnDimensionsAsTuple1D(arg)
    # FIXME:  Currently, Pymod incorrectly unwraps single-element-tuple return-types.
    # Thus, `resDimensions` should be a tuple-of-single-int, but instead it's an int.
    # We will fix this soon...
    resDimensions = (resDimensions,)
    assert resDimensions == expectedDimensions

    resShape = pymod_test_mod.returnShapeAsTuple1D(arg)
    # FIXME:  Currently, Pymod incorrectly unwraps single-element-tuple return-types.
    # Thus, `resShape` should be a tuple-of-single-int, but instead it's an int.
    # We will fix this soon...
    resShape = (resShape,)
    assert resShape == expectedShape


@pytest.mark.parametrize("input_type", [
        numpy.bool,
        numpy.bool_,
        numpy.int8,
        numpy.int16,
        numpy.int32,
        numpy.int64,
        numpy.uint8,
        numpy.uint16,
        numpy.uint32,
        numpy.uint64,
        numpy.float32,
        numpy.float64,
])
def test_returnStridesAsTuple1D(pymod_test_mod, input_type, random_1d_array_size):
    arg = _get_random_1d_array_of_type(random_1d_array_size, input_type)
    expectedStrides = arg.strides

    resStrides = pymod_test_mod.returnStridesAsTuple1D(arg)
    # FIXME:  Currently, Pymod incorrectly unwraps single-element-tuple return-types.
    # Thus, `resStrides` should be a tuple-of-single-int, but instead it's an int.
    # We will fix this soon...
    resStrides = (resStrides,)
    assert resStrides == expectedStrides


@pytest.mark.parametrize("input_type", [
        numpy.bool,
        numpy.bool_,
        numpy.int8,
        numpy.int16,
        numpy.int32,
        numpy.int64,
        numpy.uint8,
        numpy.uint16,
        numpy.uint32,
        numpy.uint64,
        numpy.float32,
        numpy.float64,
])
def test_returnNdAttr_2d(pymod_test_mod, input_type, random_2d_array_shape):
    arg = _get_random_2d_array_of_type(random_2d_array_shape, input_type)
    expectedDimensions = arg.shape
    expectedShape = arg.shape

    resNd = pymod_test_mod.returnNdAttr(arg)
    assert resNd == len(arg.shape)
    assert resNd == arg.ndim

    resNdim = pymod_test_mod.returnNdimAttr(arg)
    assert resNdim == len(arg.shape)
    assert resNdim == arg.ndim


@pytest.mark.parametrize("input_type", [
        numpy.bool,
        numpy.bool_,
        numpy.int8,
        numpy.int16,
        numpy.int32,
        numpy.int64,
        numpy.uint8,
        numpy.uint16,
        numpy.uint32,
        numpy.uint64,
        numpy.float32,
        numpy.float64,
])
def test_returnDimensionsAsTuple2D(pymod_test_mod, input_type, random_2d_array_shape):
    arg = _get_random_2d_array_of_type(random_2d_array_shape, input_type)
    expectedDimensions = arg.shape
    expectedShape = arg.shape

    resDimensions = pymod_test_mod.returnDimensionsAsTuple2D(arg)
    assert resDimensions == expectedDimensions

    resShape = pymod_test_mod.returnShapeAsTuple2D(arg)
    assert resShape == expectedShape


@pytest.mark.parametrize("input_type", [
        numpy.bool,
        numpy.bool_,
        numpy.int8,
        numpy.int16,
        numpy.int32,
        numpy.int64,
        numpy.uint8,
        numpy.uint16,
        numpy.uint32,
        numpy.uint64,
        numpy.float32,
        numpy.float64,
])
def test_returnStridesAsTuple2D(pymod_test_mod, input_type, random_2d_array_shape):
    arg = _get_random_2d_array_of_type(random_2d_array_shape, input_type)
    expectedStrides = arg.strides

    resStrides = pymod_test_mod.returnStridesAsTuple2D(arg)
    assert resStrides == expectedStrides


@pytest.mark.parametrize("input_type", [
        numpy.bool,
        numpy.bool_,
        numpy.int8,
        numpy.int16,
        numpy.int32,
        numpy.int64,
        numpy.uint8,
        numpy.uint16,
        numpy.uint32,
        numpy.uint64,
        numpy.float32,
        numpy.float64,
])
def test_returnNdAttr_3d(pymod_test_mod, input_type, random_3d_array_shape):
    arg = _get_random_Nd_array_of_type(random_3d_array_shape, input_type)

    resNd = pymod_test_mod.returnNdAttr(arg)
    assert resNd == len(arg.shape)
    assert resNd == arg.ndim

    resNdim = pymod_test_mod.returnNdimAttr(arg)
    assert resNdim == len(arg.shape)
    assert resNdim == arg.ndim


@pytest.mark.parametrize("input_type", [
        numpy.bool,
        numpy.bool_,
        numpy.int8,
        numpy.int16,
        numpy.int32,
        numpy.int64,
        numpy.uint8,
        numpy.uint16,
        numpy.uint32,
        numpy.uint64,
        numpy.float32,
        numpy.float64,
])
def test_returnDimensionsAsTuple3D(pymod_test_mod, input_type, random_3d_array_shape):
    arg = _get_random_Nd_array_of_type(random_3d_array_shape, input_type)
    expectedDimensions = arg.shape
    expectedShape = arg.shape

    resDimensions = pymod_test_mod.returnDimensionsAsTuple3D(arg)
    assert resDimensions == expectedDimensions

    resShape = pymod_test_mod.returnShapeAsTuple3D(arg)
    assert resShape == expectedShape


@pytest.mark.parametrize("input_type", [
        numpy.bool,
        numpy.bool_,
        numpy.int8,
        numpy.int16,
        numpy.int32,
        numpy.int64,
        numpy.uint8,
        numpy.uint16,
        numpy.uint32,
        numpy.uint64,
        numpy.float32,
        numpy.float64,
])
def test_returnStridesAsTuple3D(pymod_test_mod, input_type, random_3d_array_shape):
    arg = _get_random_Nd_array_of_type(random_3d_array_shape, input_type)
    expectedStrides = arg.strides

    resStrides = pymod_test_mod.returnStridesAsTuple3D(arg)
    assert resStrides == expectedStrides


@pytest.mark.parametrize("input_type", [
        numpy.bool,
        numpy.bool_,
        numpy.int8,
        numpy.int16,
        numpy.int32,
        numpy.int64,
        numpy.uint8,
        numpy.uint16,
        numpy.uint32,
        numpy.uint64,
        numpy.float32,
        numpy.float64,
])
def test_returnNdAttr_4d(pymod_test_mod, input_type, random_4d_array_shape):
    arg = _get_random_Nd_array_of_type(random_4d_array_shape, input_type)

    resNd = pymod_test_mod.returnNdAttr(arg)
    assert resNd == len(arg.shape)
    assert resNd == arg.ndim

    resNdim = pymod_test_mod.returnNdimAttr(arg)
    assert resNdim == len(arg.shape)
    assert resNdim == arg.ndim


@pytest.mark.parametrize("input_type", [
        numpy.bool,
        numpy.bool_,
        numpy.int8,
        numpy.int16,
        numpy.int32,
        numpy.int64,
        numpy.uint8,
        numpy.uint16,
        numpy.uint32,
        numpy.uint64,
        numpy.float32,
        numpy.float64,
])
def test_returnDimensionsAsTuple4D(pymod_test_mod, input_type, random_4d_array_shape):
    arg = _get_random_Nd_array_of_type(random_4d_array_shape, input_type)
    expectedDimensions = arg.shape
    expectedShape = arg.shape

    resDimensions = pymod_test_mod.returnDimensionsAsTuple4D(arg)
    assert resDimensions == expectedDimensions

    resShape = pymod_test_mod.returnShapeAsTuple4D(arg)
    assert resShape == expectedShape


@pytest.mark.parametrize("input_type", [
        numpy.bool,
        numpy.bool_,
        numpy.int8,
        numpy.int16,
        numpy.int32,
        numpy.int64,
        numpy.uint8,
        numpy.uint16,
        numpy.uint32,
        numpy.uint64,
        numpy.float32,
        numpy.float64,
])
def test_returnStridesAsTuple4D(pymod_test_mod, input_type, random_4d_array_shape):
    arg = _get_random_Nd_array_of_type(random_4d_array_shape, input_type)
    expectedStrides = arg.strides

    resStrides = pymod_test_mod.returnStridesAsTuple4D(arg)
    assert resStrides == expectedStrides
