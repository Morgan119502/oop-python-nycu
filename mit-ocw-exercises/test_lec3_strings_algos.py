def test_example_loops():
    s = "qwertyuiop"
    result_for_index = ""
    for index in range(len(s)):
        if s[index] == 'i' or s[index] == 'u':
            result_for_index += "There is an i or u"

    result_for_char = ""
    for char in s:
        if char == 'i' or char == 'u':
            result_for_char += "There is an i or u"

    assert result_for_index == "There is an i or uThere is an i or u"
    assert result_for_char == "There is an i or uThere is an i or u"


def test_challenge_rewrite_while_loop():
    an_letters = "aefhilmnorsxAEFHILMNORSX"
    word = "example"
    times = 3

    result = ""
    for char in word:
        if char in an_letters:
            result += "Give me an " + char + "! " + char
        else:
            result += "Give me a  " + char + "! " + char

    expected_result = "Give me an e! eGive me an x! xGive me an a! aGive me an m! mGive me a  p! pGive me an l! lGive me an e! e"
    assert result == expected_result

    result = ""
    for _ in range(times):
        result += word + "!!!"

    expected_result = "example!!!example!!!example!!!"
    assert result == expected_result


# Add more test functions as needed for other examples...

# Run the tests
test_example_loops()
test_challenge_rewrite_while_loop()
# Add calls to other test functions as needed...
print("All tests passed!")
