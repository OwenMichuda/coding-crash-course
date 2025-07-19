import variables as exercise

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

def test_full_name():
    if exercise.full_name == ...: return False
    assert isinstance(exercise.full_name, str), "'full_name' should be a string."
    assert exercise.full_name != "", "'full_name' should not be an empty string."

def test_age():
    if exercise.age == ...: return False
    assert isinstance(exercise.age, int), "'age' should be an integer."
    assert exercise.age > 0, "'age' should be a positive number."

def test_height():
    if exercise.height == ...: return False
    assert isinstance(exercise.height, float), "'height' should be a float."
    assert 0.5 < exercise.height < 3.0, "'height' in meters should be a reasonable value."

def test_is_char_cute():
    if exercise.is_char_cute == ...: return False
    assert isinstance(exercise.is_char_cute, bool), "'is_char_cute' should be a boolean."
    assert exercise.is_char_cute is True, "come on, let's be honest"

# --- Main Test Runner ---

if __name__ == "__main__":
    print()
    print()
    print()
    print("--- Running Tests for Variables Exercise ---")

    tests = [
        (test_full_name, "full_name variable"),
        (test_age, "age variable"),
        (test_height, "height variable"),
        (test_is_char_cute, "is_char_cute variable"),
    ]

    results = [run_test(func, name) for func, name in tests]

    print("-" * 42)
    if all(results):
        print("🎉 Congratulations! All variable tests passed! 🎉")
    else:
        failed_count = results.count(False)
        print(f" {failed_count} test(s) failed. Double-check your variable assignments.")