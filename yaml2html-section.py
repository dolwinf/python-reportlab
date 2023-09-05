import yaml

# Load the YAML file
with open('control_catalog.yaml', 'r') as file:
    data = yaml.load(file, Loader=yaml.FullLoader)

# Extract data to create structured HTML content
metadata = data["catalog"]["metadata"]
control_group = data["catalog"]["groups"][0]
control = control_group["controls"][0]

# Initialize HTML content
html_content = """
<!DOCTYPE html>
<html>
<head>
    <title>Security Control Catalog</title>
</head>
<body>
"""

# Adding metadata details
html_content += f"<h1>{metadata['title']}</h1>"
html_content += f"<p>Title: {metadata['title']}</p>"
html_content += f"<p>Version: {metadata['version']}</p>"
html_content += f"<p>Published Date: {metadata['published']}</p>"
html_content += f"<p>Last Modified: {metadata['last-modified']}</p>"
html_content += f"<p>OSCAL Version: {metadata['oscal-version']}</p>"

# Adding control group details
html_content += f"<h2>Control Group ID: {control_group['id']}</h2>"
html_content += f"<p>Control Group Title: {control_group['title']}</p>"

# Adding individual control details
html_content += f"<h2>Control ID: {control['id']}</h2>"
html_content += f"<p>Control Title: {control['title']}</p>"
html_content += f"<p>Priority: {control['priority']}</p>"
html_content += f"<h3>Description</h3>"
html_content += f"<p>{control['statements']['description']}</p>"
html_content += f"<h3>Guidance</h3>"
html_content += f"<p>{control['statements']['guidance']}</p>"
html_content += f"<h3>References</h3>"
html_content += f"<p>{', '.join(control['properties'][0]['values'])}</p>"

# Closing HTML content
html_content += """
</body>
</html>
"""

# Write HTML content to file
with open('control_catalog.html', 'w') as html_file:
    html_file.write(html_content)
