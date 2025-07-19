import final_challenge as ex

def run_test(test_function, test_name):
    """A helper function to run a test and print the result."""
    try:
        test_function()
        print(f"✅ PASSED: {test_name}")
        return True
    except AttributeError as e:
        # This error happens if a required variable wasn't created.
        print(f"🤔 SKIPPED: {test_name} (Variable not found: {e})")
        return False
    except AssertionError:
        # This error happens if the variable's value is incorrect.
        print(f"❌ FAILED: {test_name}")
        return False

# --- Test Functions ---

def test_total_cost():
    # Expected cost: (3 * 45) + 120 + 250 = 505
    try:
        # Guess common variable names to give the user flexibility.
        cost_var_name = "total_cost"
        possible_names = [cost_var_name, "total_giblet_cost", "dodo_love_cost"]
        for name in possible_names:
            if hasattr(ex, name):
                cost_var_name = name
                break
        else:
            raise AttributeError("'total_cost' or similar variable")

        total_cost = getattr(ex, cost_var_name)
        assert total_cost == 505
    except AttributeError as e:
        # Re-raise with a more specific message for the run_test function
        raise AttributeError(str(e))


def test_giblets_remaining():
    # Expected remaining: 1250 - 505 = 745
    try:
        remaining_var_name = "giblets_left"
        possible_names = [remaining_var_name, "remaining_giblets", "giblets_after_trade"]
        for name in possible_names:
            if hasattr(ex, name):
                remaining_var_name = name
                break
        else:
            raise AttributeError("'giblets_left' or similar variable")

        giblets_left = getattr(ex, remaining_var_name)
        assert giblets_left == 745
    except AttributeError as e:
        raise AttributeError(str(e))


def test_can_afford_tickles_before():
    # Expected: 1250 >= 1000 is True
    assert hasattr(ex, 'can_afford_tickles_before'), "Variable 'can_afford_tickles_before' not found."
    assert ex.can_afford_tickles_before is True, "The value for 'can_afford_tickles_before' is incorrect."


def test_can_afford_tickles_after():
    # Expected: 745 >= 1000 is False
    assert hasattr(ex, 'can_afford_tickles_after'), "Variable 'can_afford_tickles_after' not found."
    assert ex.can_afford_tickles_after is False, "The value for 'can_afford_tickles_after' is incorrect."


# --- Main Test Runner ---

if __name__ == "__main__":
    print("--- Running Tests for Birdbrain's Giblet Bonanza ---")

    tests = [
        (test_total_cost, "Calculating Total Dodo Treasure Cost"),
        (test_giblets_remaining, "Calculating Remaining Giblets"),
        (test_can_afford_tickles_before, "Checking for Tickle Sesh (Before)"),
        (test_can_afford_tickles_after, "Checking for Tickle Sesh (After)"),
    ]

    results = [run_test(func, name) for func, name in tests]

    print("-" * 55)
    if all(results):
        print("🎉🎉🎉 WOOO! Birdbrain is a BEAST! All tests passed! 🎉🎉🎉")
        print("You successfully used variables, data types, math, and comparisons!")
    else:
        failed_count = results.count(False)
        print(f"{failed_count} part(s) need another look. You got this Birdbrain!")