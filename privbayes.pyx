from libcpp.string cimport string


cdef extern from "lib/wrapper.cpp":
    cdef void wrapper(const string &dom_path, const string &data_path, const string &out_path, double epsilon, double theta, int n_samples, int seed)


def py_wrapper(dom_path, data_path, out_path, epsilon, theta, n_samples, seed):
    wrapper(dom_path, data_path, out_path, epsilon, theta, n_samples, seed)
