#include <iostream>
#include "methods.h"

extern "C" void wrapper(const string &dom_path, const string &data_path, const string &out_path, double epsilon, double theta, int n_samples, int seed) {
    engine eng(seed);
    table tbl(dom_path, data_path, true);
    bayesian bay(eng, tbl, epsilon, theta);
    bay.sampling(n_samples);
    bay.syn.printo_file(out_path);
}