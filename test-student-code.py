import os
import subprocess
import time

directory = "./students-code"
line_length = 80
line_character = "-"
formatted_line = line_character * line_length

def generate_html_report(folder_name, folder_path, htmlhint, csslint, purifycss, eslint):
    html_content = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>{folder_name} - Bewertung Projektarbeit LBV_M291</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                margin: 20px;
                padding: 0;
                line-height: 1.6;
            }}
            h1, h2 {{
                color: #333;
            }}
            pre {{
                background: #f4f4f4;
                padding: 10px;
                border: 1px solid #ddd;
                overflow-x: auto;
            }}
        </style>
    </head>
    <body>
        <h1>Bewertung Projektarbeit LBV_M291</h1>
        <h2>{folder_name}</h2>
        <pre>{formatted_line}\n{folder_path}\n{formatted_line}</pre>
        <h2>HTML Checker</h2>
        <pre>{htmlhint}</pre>
        <h2>CSS Checker</h2>
        <pre>{csslint}</pre>
        <h2>CSS Purify</h2>
        <pre>{purifycss}</pre>
        <h2>JS Checker</h2>
        <pre>{eslint}</pre>
    </body>
    </html>
    """
    return html_content

for folder in os.listdir(directory):
    folder_path = os.path.join(directory, folder)
    if os.path.isdir(folder_path):
        print(f"Processing {folder}...")

        purifycss = subprocess.run(
            ['./node_modules/.bin/purifycss', '-ri'] + 
            [f"{folder_path}/**/*.css", f"{folder_path}/**/*.html", '-o', '/dev/null'], 
            capture_output=True, text=True
        ).stdout

        csslint = subprocess.run(
            f"rm -f output.css; find {folder_path} -name '*.css' -type f -exec cat {{}} \\; > output.css; node node_modules/.bin/csslint --config=.csslint --quiet ./output.css", 
            shell=True, capture_output=True, text=True
        ).stdout

        htmlhint = subprocess.run(
            ['node_modules/.bin/htmlhint', '--config', '.htmlhint', folder_path], 
            capture_output=True, text=True
        ).stdout

        eslint = subprocess.run(
            ['node_modules/.bin/eslint', folder_path], 
            capture_output=True, text=True
        ).stdout

        report_path = f"./student-reports/{folder}.html"
        html_content = generate_html_report(folder, folder_path, htmlhint, csslint, purifycss, eslint)

        with open(report_path, 'w') as report_file:
            report_file.write(html_content)

        os.remove('output.css')
        time.sleep(1)
