import os
import subprocess
import time
import html
from datetime import datetime

directory = "./students-code"
line_length = 80
line_character = "-"
formatted_line = line_character * line_length

def check_unused_files(folder_path):
    all_files = []
    used_files = set()

    # Gather all files
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if not file.endswith('.md'):
                all_files.append(os.path.relpath(os.path.join(root, file), folder_path))

    # Check for usage
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith(('.html', '.js', '.css', '.php')):
                file_path = os.path.join(root, file)
                with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                    content = f.read()
                    for target_file in all_files:
                        if target_file in content:
                            used_files.add(target_file)

    # Find unused files
    unused_files = set(all_files) - used_files
    return '\n'.join(sorted(unused_files))

def generate_html_report(folder_name, folder_path, htmlhint, csslint, purifycss, eslint, unused_files_report):
    html_content = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>{folder_name} - Bewertung Projektarbeit LBV_M291</title>
        <style>
            body {{
                font-family: 'Roboto', sans-serif;
                margin: 20px;
                padding: 0;
                line-height: 1.6;
                background-color: #f9f9f9;
                color: #333;
            }}
            h1, h2 {{
                color: #444;
                border-bottom: 2px solid #ddd;
                padding-bottom: 5px;
            }}
            h1 {{
                font-size: 24px;
                margin-bottom: 20px;
            }}
            h2 {{
                font-size: 20px;
                margin-top: 20px;
                margin-bottom: 10px;
            }}
            pre {{
                background: #fff;
                padding: 15px;
                border: 1px solid #ddd;
                border-radius: 5px;
                box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
                overflow-x: auto;
            }}
            .container {{
                max-width: 800px;
                margin: auto;
                padding: 20px;
                background: #fff;
                border-radius: 10px;
                box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
            }}
            .timestamp {{
                font-size: 14px;
                color: #888;
                margin-bottom: 10px;
            }}
        </style>
    </head>
    <body>
        <div class="container">
            <h1>{folder_name} - Code Quality Checker - Projektarbeit LBV M291</h1>
   
            <div class="timestamp">{datetime.now().strftime("%Y-%m-%d %H:%M")}</div>
         
            <h2>HTML Checker</h2>
            <pre>{html.escape(htmlhint)}</pre>
            <h2>JS Checker</h2>
            <pre>{eslint}</pre>
            <h2>Unused Files Report</h2>
            <pre>{unused_files_report}</pre>
            <h2>CSS Checker</h2>
            <pre>{stylelint}</pre>
            <h2>CSS Checker 2</h2>
            <pre>{csslint}</pre>
            <h2>CSS Purify</h2>
            <pre>{purifycss}</pre>
        </div>
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

        
        stylelint_command = f'node_modules/.bin/stylelint "{folder_path}/**/*.css"'
        stylelint = subprocess.run(
            stylelint_command,
            shell=True,
            capture_output=True,
            text=True
        )
        stylelint_tmp = stylelint.stdout + stylelint.stderr
        stylelint = stylelint_tmp.replace('\n', '<br>')

        unused_files_report = check_unused_files(folder_path)

        report_path = f"./student-reports/{folder}.html"
        html_content = generate_html_report(folder, folder_path, htmlhint, csslint, purifycss, eslint, unused_files_report)
      
        with open(report_path, 'w') as report_file:
            report_file.write(html_content)

        os.remove('output.css')
        time.sleep(1)


