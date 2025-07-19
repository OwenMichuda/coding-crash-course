import data_types as exercise

# def run_test(test_function, test_name):
#     """A helper function to run a test and print the result."""
#     try:
#         test_function()
#         print(f"✅ PASSED: {test_name}")
#         return True
#     except AssertionError as e:
#         print(f"❌ FAILED: {test_name}")
#         # print(f"   Reason: {e}") # Uncomment for more detailed error messages
#         return False

# --- Test Functions ---

def test_my_name():
    assert isinstance(exercise.my_name, str), "'my_name' should be a string."
    assert exercise.my_name == "Owen", "The value of 'my_name' should be 'Owen'."

def test_type_of_string():
    assert exercise.type_of_hello == str, "The type of 'EAT MY SHORTS!' is str."

def test_my_age():
    assert isinstance(exercise.my_age, int), "'my_age' should be an integer."
    assert exercise.my_age == 23, "The value of 'my_age' should be 24."

def test_type_of_100():
    assert exercise.type_of_100 == int, "The type of 100 is int."

def test_pi():
    assert isinstance(exercise.pi, float), "'pi' should be a float."
    assert exercise.pi == 3.14159, "The value of 'pi' should be 3.14159."

def test_type_of_negative_25_5():
    assert exercise.type_of_negative_25_5 == float, "The type of -25.5 is float."

def test_is_charlotte_right():
    assert isinstance(exercise.is_charlotte_right, bool), "'is_charlotte_right' should be a boolean."
    assert exercise.is_charlotte_right is False, "The value of 'is_charlotte_right' should be False."

def test_type_of_false():
    assert exercise.type_of_false == bool, "The type of False is bool."


# --- Main Test Runner ---

# if __name__ == "__main__":
#     print("--- Running Tests for Data Types Exercise ---")

#     tests = [
#         (test_my_name, "Part 1: 'my_name' variable"),
#         (test_type_of_string, "Part 1: Type of string"),
#         (test_my_age, "Part 2: 'my_age' variable"),
#         (test_type_of_100, "Part 2: Type of integer"),
#         (test_pi, "Part 3: 'pi' variable"),
#         (test_type_of_negative_25_5, "Part 3: Type of float"),
#         (test_is_charlotte_right, "Part 4: 'is_charlotte_right' variable"),
#         (test_type_of_false, "Part 4: Type of boolean"),
#     ]

#     results = [run_test(func, name) for func, name in tests]

#     print("-" * 43)
#     if all(results):
#         print("🎉 Congratulations! All tests passed! You've mastered basic data types. 🎉")
#     else:
#         failed_count = results.count(False)
#         print(f"Hmm, {failed_count} test(s) failed. Review the FAILED messages and try again!")