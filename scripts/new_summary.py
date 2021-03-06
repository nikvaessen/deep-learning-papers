################################################################################
# This script will ask the user for some information regarding the soon-to-be
# read paper before generating the starting point for the summary according to
# a summary template.
#
# Usage: python new_summary.py
#
# Author: Nik Vaessen
################################################################################

import os
import re
import datetime
import json

from pathlib import Path

################################################################################
# Implement functionality of script

title_template_str = "---title---"
estimated_minutes_template_str = "---time---"
url_template_str = "---url---"
date_template_str = "---date---"
topics_template_str = "---topic---"
meta_json_template_str = "---json---"


def main():
    # set working directory to root of path
    script_path = Path(os.path.abspath(__file__))
    root_dir = script_path.parent.parent.as_posix()

    os.chdir(root_dir)

    # Query essential information for creating new summary document
    title = input("What is the title of the article?: ")
    filename = input("What should the name of the summary markdown file be?: ")
    url = input("What is the URL of of the article?: ")
    estimated_minutes = input("How many minutes do you expect to read this paper?: ")
    topics = input("Give a comma-separated list of covered topic(s): ")
    date = datetime.datetime.now().strftime("%Y-%m-%d")
    meta_obj = json.dumps({
        "title": title,
        "url": url,
        "topics": topics,
        "date": date,
        "estimated_minutes": estimated_minutes
    })

    # Insert the information into the template file
    file = Path("summary_template.md").read_text()

    file = re.sub(title_template_str, title, file)
    file = re.sub(estimated_minutes_template_str, estimated_minutes, file)
    file = re.sub(url_template_str, url, file)
    file = re.sub(date_template_str, date, file)
    file = re.sub(topics_template_str, topics, file)
    file = re.sub(meta_json_template_str, meta_obj, file)

    # Create the new summary file
    summaries_dir = os.path.join(root_dir, "summaries")

    if not os.path.exists(summaries_dir):
        os.mkdir(summaries_dir)

    new_fn = os.path.join(summaries_dir, f"{filename}.md")

    with open(new_fn, 'w') as f:
        f.write(file)


if __name__ == '__main__':
    main()
