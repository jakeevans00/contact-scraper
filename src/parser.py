import ast

def convert_txt_to_html(response_text):
    try:
        data = ast.literal_eval(response_text)
        html_content = data['results'][0]['content']
        with open('results.html', 'w') as file:
            file.write(str(html_content))
        return html_content
    except (SyntaxError, KeyError, IndexError) as e:
        print(f"Error parsing response: {e}")
        return None