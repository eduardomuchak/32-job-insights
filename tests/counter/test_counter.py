from src.counter import count_ocurrences


def test_counter():
    file_path = "src/jobs.csv"
    languages = ["Python", "Javascript"]
    expected_results = [1639, 122]

    for language in range(len(languages)):
        assert (
            count_ocurrences(file_path, languages[language])
            == expected_results[language]
        )
