from python_class_work import lesson_6
def execute_func(file_name, sheet_name):
    cases = lesson_6.read_data(file_name, sheet_name)
    for case in cases:
        case_id = case.get("case_id")
        url = case.get("url")
        data = eval(case["data"])
        expected_result = eval(case.get("expected_result"))
        expected_msg = expected_result.get("msg")

        real_result = lesson_6.api_func(url_api=url, data_api=data)
        real_msg = real_result.get("msg")

        print("真实执行结果:{}".format(real_msg))
        print("预期执行结果:{}".format(expected_msg))
        if real_msg == expected_msg:
            final_result = "Passed"
            print("第{}条测试用例执行通过!".format(case_id))
        else:
            final_result = "Failed"
            print("第{}条测试用例执行不通过!".format(case_id))
        print("*" * 20)
        lesson_6.write_result(file_name, sheet_name, final_result, case_id + 1, 8)

execute_func("test_case_api.xlsx", "login")

