# coding: utf-8
import compute

result = ["8", "4", "7", "3", "6"]

def main():
    compute.x5_eq_batch(result, ["01", "34", "56", "78", "9"])
    compute.x5_eq_simple(result, ["01234", "56789", "56790"])
    compute.x5_cb_g120(result, ["1", "2", "3", "4", "52"])
    compute.x5_cb_g60(result, ["01", "234"])
    compute.x5_cb_g30(result, ["01", "2"])
    compute.x5_cb_g20(result, ["0", "12"])
    compute.x5_cb_g10(result, ["0", "1"])
    compute.x5_cb_g5(result, ["0", "1"])
    compute.x5_unf_m1(result, ["0", "1", "2", "3"])
    compute.x5_unf_m2(result, ["0", "1", "2", "3"])
    compute.x5_unf_m3(result, ["0", "1", "2", "3"])
    compute.x5_fun_f1(result, ["1", "2", "3", "4", "5"])
    compute.x5_fun_f2(result, ["1", "2", "3", "4", "5"])
    compute.x5_fun_f3(result, ["1", "2", "3", "4", "5"])
    compute.x5_fun_f4(result, ["1", "2", "3", "4", "5"])

    compute.x4f_eq_batch(result, ["01", "34", "56", "78"])
    compute.x4f_eq_simple(result, ["0123", "4567", "8901"])
    compute.x4f_cb_g24(result, ["1", "2", "3", "4"])
    compute.x4f_cb_g12(result, ["1", "23"])
    compute.x4f_cb_g6(result, ["1", "23"])
    compute.x4f_cb_g4(result, ["1", "234"])
    compute.x4f_unf_m1(result, ["0", "1", "2", "3"])
    compute.x4f_unf_m2(result, ["0", "1", "2", "3"])

    compute.x4b_eq_batch(result, ["01", "34", "56", "78"])
    compute.x4b_eq_simple(result, ["0123", "4567", "8901"])
    compute.x4b_cb_g24(result, ["1", "2", "3", "4"])
    compute.x4b_cb_g12(result, ["1", "23"])
    compute.x4b_cb_g6(result, ["1", "23"])
    compute.x4b_cb_g4(result, ["1", "234"])
    compute.x4b_unf_m1(result, ["0", "1", "2", "3"])
    compute.x4b_unf_m2(result, ["0", "1", "2", "3"])

    compute.x3f_eq_batch(result, ["01", "34", "56"])
    compute.x3f_eq_simple(result, ["012", "345", "678"])
    compute.x3f_eq_sum(result, ["1", "2"])
    compute.x3f_eq_diff(result, ["1", "2"])
    # compute.x3f_cb_gx(result, [])
    compute.x3f_cb_sum(result, ["1", "2"])
    compute.x3f_cb_mix(result, ["012", "345"])
    compute.x3f_cb_with(result, ["1"])
    compute.x3f_cb_g3(result, ["1", "234"])
    compute.x3f_cb_g6(result, ["0", "1", "2", "3"])
    compute.x3f_unf_m1(result, ["0", "1", "2", "3"])
    compute.x3f_unf_m2(result, ["0", "1", "2", "3"])

    compute.x3m_eq_batch(result, ["01", "34", "56"])
    compute.x3m_eq_simple(result, ["012", "345", "678"])
    compute.x3m_eq_sum(result, ["1", "2"])
    compute.x3m_eq_diff(result, ["1", "2"])
    # compute.x3m_cb_gx(result, [])
    compute.x3m_cb_sum(result, ["1", "2"])
    compute.x3m_cb_mix(result, ["012", "345"])
    compute.x3m_cb_with(result, ["1"])
    compute.x3m_cb_g3(result, ["1", "234"])
    compute.x3m_cb_g6(result, ["0", "1", "2", "3"])
    compute.x3m_unf_m1(result, ["0", "1", "2", "3"])
    compute.x3m_unf_m2(result, ["0", "1", "2", "3"])

    compute.x3b_eq_batch(result, ["01", "34", "56"])
    compute.x3b_eq_simple(result, ["012", "345", "678"])
    compute.x3b_eq_sum(result, ["1", "2"])
    compute.x3b_eq_diff(result, ["1", "2"])
    # compute.x3b_cb_gx(result, [])
    compute.x3b_cb_sum(result, ["1", "2"])
    compute.x3b_cb_mix(result, ["012", "345"])
    compute.x3b_cb_with(result, ["1"])
    compute.x3b_cb_g3(result, ["1", "234"])
    compute.x3b_cb_g6(result, ["0", "1", "2", "3"])
    compute.x3b_unf_m1(result, ["0", "1", "2", "3"])
    compute.x3b_unf_m2(result, ["0", "1", "2", "3"])

    compute.x2f_eq_batch(result, ["01", "234"])
    compute.x2f_eq_simple(result, ["01", "23", "45"])
    compute.x2f_eq_sum(result, ["1", "2"])
    compute.x2f_eq_diff(result, ["1", "2"])
    compute.x2f_cb_batch(result, ["12", "34"])
    compute.x2f_cb_simple(result, ["1", "2"])
    compute.x2f_cb_sum(result, ["1", "2"])
    compute.x2f_cb_with(result, ["1"])

    compute.x2b_eq_batch(result, ["01", "234"])
    compute.x2b_eq_simple(result, ["01", "23", "45"])
    compute.x2b_eq_sum(result, ["1", "2"])
    compute.x2b_eq_diff(result, ["1", "2"])
    compute.x2b_cb_batch(result, ["12", "34"])
    compute.x2b_cb_simple(result, ["1", "2"])
    compute.x2b_cb_sum(result, ["1", "2", "9"])
    compute.x2b_cb_with(result, ["3"])

    compute.x1_fix_batch(result, ["01", "23", "456", "37", "89"])



if __name__ == '__main__':
    main()