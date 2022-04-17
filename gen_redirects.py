# imports
import glob

# html generation method
def getHtmlRedirectPage(newUrl: str) -> str:
	return f'''<!DOCTYPE HTML>

	<html lang="en">

		<head>

			<meta charset="utf-8" />
			<meta http-equiv="refresh" content="0;url={newUrl}" />
			<link rel="canonical" href="{newUrl}" />

		</head>

		<body>

			<h1>

				This page has been moved to <a href="{newUrl}">{newUrl}</a>

			</h1>

		</body>

	</html>'''

# step 1: get list of html files here
filesList = [file for file in glob.glob('*.html')]
print(filesList)

# step 2: generate list of new urls here
urlsList = [f'https://www.jamesgoodman.me/{file}' for file in filesList]
print(urlsList)

for file in filesList:
	url  = f'https://www.jamesgoodman.me/{file}'
	html = getHtmlRedirectPage(url)

	with open(file,'w') as file2write:
		file2write.write(html)
