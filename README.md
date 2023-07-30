# ResumeSite
www.drew-erwin-resume.com site code

Blog post detailing creation of the site and challenges completed can be found linked on the site footer.

Resume.html, Resume.js, and Resume.css create the resume website. HTML and CSS create the website seen, while JS allowswith the footer and sends API calls.

_int_.py, function.json, local.settings.json, and requirements.txt all create the needed resources for the Azure Function.The Azure function grabs HTTP requests from the JS on the site and sends API calls to the Cosmos DB database. This allowsbetter security due to the site not being able to interact with the database directly.
