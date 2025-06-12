test_case_file = r"c:\Users\admin\Desktop\Software and Testing\testcase.txt"
# Step 1: Define the function to be tested
def add_numbers(a, b):
    return a + b

# Step 2: Read test cases from a file
def read_test_cases(test_case_file):
    test_cases = []
    with open(test_case_file, 'r') as file:
        lines = file.readlines()
        for line in lines:
            parts = line.strip().split(',')
            if len(parts) == 3:  # expecting input1, input2, expected_output
                input1 = int(parts[0])
                input2 = int(parts[1])
                expected_output = int(parts[2])
                test_cases.append((input1, input2, expected_output))
    return test_cases

# Step 3: Execute tests and log results
def execute_tests_and_log(test_cases, result_file_path):
    with open(result_file_path, 'w') as result_file:
        for index, (input1, input2, expected) in enumerate(test_cases):
            actual = add_numbers(input1, input2)
            if actual == expected:
                result = "PASS"
            else:
                result = "FAIL"
            # Log format: Test Case ID, Inputs, Expected, Actual, Result
            result_file.write(f"Test Case {index+1}: Inputs=({input1},{input2}), Expected={expected}, Actual={actual} --> {result}\n")

    print(f"Testing complete. Results saved in '{result_file_path}'.")

# Step 4: Main Execution
if __name__ == "__main__":
    result_file = "test_results.txt"

    # Read test cases
    test_cases = read_test_cases(test_case_file)

    # Execute tests and log results
    execute_tests_and_log(test_cases, result_file)