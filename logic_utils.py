# Fix: Normal and Hard ranges used to be swapped (Normal: 1-100, Hard: 1-50),
# so "Hard" had a smaller search space than "Normal" despite fewer allowed
# attempts. A bigger range now actually makes the game harder.
def get_range_for_difficulty(difficulty: str):
    """Return (low, high) inclusive range for a given difficulty."""
    if difficulty == "Easy":
        return 1, 20
    if difficulty == "Normal":
        return 1, 50
    if difficulty == "Hard":
        return 1, 100
    return 1, 50


def parse_guess(raw: str):
    """
    Parse user input into an int guess.

    Returns: (ok: bool, guess_int: int | None, error_message: str | None)
    """
    if raw is None or raw == "":
        return False, None, "Enter a guess."

    try:
        if "." in raw:
            value = int(float(raw))
        else:
            value = int(raw)
    except Exception:
        return False, None, "That is not a number."

    return True, value, None


# Fix: the caller in app.py used to convert `secret` to a string on every
# other attempt, which made this function fall into a string/lexicographic
# comparison (e.g. "9" > "10" is True) instead of a numeric one, giving
# wrong "Too High"/"Too Low" results. The caller now always passes an int,
# so the plain numeric comparison below is always correct.
def check_guess(guess, secret):
    """
    Compare guess to secret and return the outcome.

    outcome examples: "Win", "Too High", "Too Low"
    """
    if guess == secret:
        return "Win"
    if guess > secret:
        return "Too High"
    return "Too Low"


# Fix: "Too High" and "Too Low" were paired with the wrong message (a guess
# that was too high told the player to "Go HIGHER" instead of "Go LOWER",
# and vice versa). The pairing below is now consistent with the outcome.
HINT_MESSAGES = {
    "Win": "🎉 Correct!",
    "Too High": "📉 Go LOWER!",
    "Too Low": "📈 Go HIGHER!",
}


def get_hint_message(outcome: str) -> str:
    """Return the display message for a given outcome."""
    return HINT_MESSAGES[outcome]


def update_score(current_score: int, outcome: str, attempt_number: int):
    """Update score based on outcome and attempt number."""
    if outcome == "Win":
        points = 100 - 10 * (attempt_number + 1)
        if points < 10:
            points = 10
        return current_score + points

    if outcome == "Too High":
        if attempt_number % 2 == 0:
            return current_score + 5
        return current_score - 5

    if outcome == "Too Low":
        return current_score - 5

    return current_score
