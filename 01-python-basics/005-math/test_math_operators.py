import math_operators as exercise

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

def test_addition():
    if exercise.result_add == ...: return False
    assert exercise.result_add == 72 + 28

def test_subtraction():
    if exercise.result_sub == ...: return False
    assert exercise.result_sub == 110 - 11

def test_multiplication():
    if exercise.result_mul == ...: return False
    assert exercise.result_mul == 12 * 9

def test_division():
    if exercise.result_div == ...: return False
    assert exercise.result_div == 100 / 8

def test_floor_division():
    if exercise.result_floor == ...: return False
    assert exercise.result_floor == 100 // 8

def test_modulo():
    if exercise.result_mod == ...: return False
    assert exercise.result_mod == 25 % 4

def test_exponentiation():
    if exercise.result_exp == ...: return False
    assert exercise.result_exp == 5 ** 3

def test_challenge():
    if exercise.hours == ... or exercise.minutes == ...: return False
    assert exercise.hours == 197 // 60
    assert exercise.minutes == 197 % 60

# --- Main Test Runner ---

if __name__ == "__main__":
    print()
    print()
    print()
    print("--- Running Tests for Math Operators Exercise ---")

    tests = [
        (test_addition, "1. Addition"),
        (test_subtraction, "2. Subtraction"),
        (test_multiplication, "3. Multiplication"),
        (test_division, "4. Division"),
        (test_floor_division, "5. Floor Division"),
        (test_modulo, "6. Modulo"),
        (test_exponentiation, "7. Exponentiation"),
        (test_challenge, "⭐ Challenge Problem"),
    ]

    results = [run_test(func, name) for func, name in tests]

    print("-" * 45)
    if all(results):
        print("🎉 Congratulations! All tests passed! 🎉")
    else:
        failed_count = results.count(False)
        print(f"Hmm, it looks like {failed_count} test(s) need another look.")