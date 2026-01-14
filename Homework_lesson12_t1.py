import re


def delete_html_tags(html_file="draft.html", result_file="cleaned.txt") -> None:
    """
    This function reads an HTML file, 
    removes all HTML tags, and writes the cleaned text to a new file.

    Parameters: html_file, result_file

    Result: File to the output file where cleaned text will be saved.
    """
    with open(html_file, 'r', encoding='utf-8') as file:
        file_content = file.read()
        cleaned_text = re.sub(r'<[^>]+>', '', file_content)


    with open(result_file, 'w', encoding='utf-8') as result:
        result.write(cleaned_text)
        
delete_html_tags()

