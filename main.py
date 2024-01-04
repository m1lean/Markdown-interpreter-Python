import markdown

def markdown_to_html(markdown_text):
     # Convert Markdown text to HTML
     html_content = markdown.markdown(markdown_text)
     return html_content

if __name__ == "__main__":
     # Usage example
     markdown_text = """
     # Markdown example

     This is an **example** of text in *Markdown* format.

     *List 1
     *List 2
     *List 3
     """

     # Convert Markdown to HTML
     html_result = markdown_to_html(markdown_text)

     # Output the result
     print(html_result)
