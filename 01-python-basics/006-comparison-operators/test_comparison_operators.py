import comparison_operators as ex

def run_test(test_function, test_name):
    """A helper function to run a test and print the result."""
    try:
        # Check if the placeholder '...' is still present
        if test_function() is False:
             print(f"🤔 SKIPPED: {test_name} (answer not filled in)")
             return False
        print(f"✅ PASSED: {test_name}")
        return True
    except AssertionError:
        print(f"❌ FAILED: {test_name}")
        return False

# --- Test Functions ---

# Part 1 Tests
def test_answer_1():
    if ex.answer_1 is ...: return False
    assert ex.answer_1 is True

def test_answer_2():
    if ex.answer_2 is ...: return False
    assert ex.answer_2 is False

# Part 2 Tests
def test_result_3():
    if ex.result_3 is ...: return False
    assert ex.result_3 is (ex.num_a == ex.num_b)

def test_result_4():
    if ex.result_4 is ...: return False
    assert ex.result_4 is (ex.num_c > ex.num_d)

def test_result_5():
    if ex.result_5 is ...: return False
    assert ex.result_5 is (ex.num_e <= ex.num_f)

# Part 3 Tests
def test_did_i_pass():
    if ex.did_i_pass is ...: return False
    assert ex.did_i_pass is (ex.my_score >= ex.passing_score)

def test_is_perfect():
    if ex.is_perfect is ...: return False
    assert ex.is_perfect is (ex.my_score == ex.perfect_score)

# --- Main Test Runner ---

if __name__ == "__main__":
    print()
    print()
    print()
    print("--- Running Tests for Comparison Operators Exercise ---")

    tests = [
        (test_answer_1, "Question 1: Evaluating !="),
        (test_answer_2, "Question 2: Evaluating <="),
        (test_result_3, "Question 3: Writing =="),
        (test_result_4, "Question 4: Writing >"),
        (test_result_5, "Question 5: Writing <="),
        (test_did_i_pass, "Question 6: Challenge (Pass)"),
        (test_is_perfect, "Question 7: Challenge (Perfect)"),
    ]

    results = [run_test(func, name) for func, name in tests]

    print("-" * 55)
    if all(results):
        print("🎉 Fantastic work! All tests passed! You're a natural. 🎉")
    else:
        failed_count = results.count(False)
        print(f"{failed_count} test(s) need another look. You've got this!")