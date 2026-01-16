import re


def delete_html_tags(html_file: str = "draft.html", result_file: str = "cleaned.txt") -> None:
    """Read an HTML file, remove tags and write cleaned text to a file.

    Parameters:
        html_file: Path to the input HTML file.
        result_file: Path to write the cleaned text.
    Results:
        A text file without HTML tags.
    """
    try:
        with open(html_file, "r", encoding="utf-8") as file:
            file_content = file.read()
        cleaned_text = re.sub(r"<.*?>", "", file_content, flags=re.S)
        lines = cleaned_text.splitlines()
        final_result = "\n".join(line.strip() for line in lines if line.strip())
        with open(result_file, "w", encoding="utf-8") as result:
            result.write(final_result)
        print(f"Файл '{result_file}' успішно створено без HTML тегів.")
    except FileNotFoundError as exc:
        print(f"Помилка при записі файлу '{result_file}': {exc}")
    delete_html_tags()
