from logic_utils import check_guess, get_hint_message

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    result = check_guess(50, 50)
    assert result == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    result = check_guess(60, 50)
    assert result == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    result = check_guess(40, 50)
    assert result == "Too Low"

def test_guess_too_low_across_digit_boundary():
    # Regression test: the game used to compare the secret as a string on
    # every other attempt, so "9" vs "10" was judged lexicographically
    # ("9" > "10") and wrongly reported "Too High" instead of "Too Low".
    result = check_guess(9, 10)
    assert result == "Too Low"

def test_guess_too_high_across_digit_boundary():
    # Same bug, opposite direction: 100 is actually higher than 99, but a
    # string comparison of "100" vs "99" would say otherwise.
    result = check_guess(100, 99)
    assert result == "Too High"

def test_hint_message_direction_matches_outcome():
    # Regression test: the hint text was swapped with its outcome, so a
    # guess that was too high told the player to "Go HIGHER" (and vice
    # versa) instead of pointing them toward the secret.
    assert "LOWER" in get_hint_message("Too High")
    assert "HIGHER" in get_hint_message("Too Low")
