################################################################################
# This script will parse all the summaries written in this repository and
# update the main README.md file accordingly.
#
# Usage: python update_readme.py
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

readme_separator = "<!---REST_OF_FILE_IS_AUTO_GENERATED-->"


def get_json_from_summary(summary_path):
    with open(summary_path, 'r') as f:
        # skip first line
        f.readline()

        # second line should be json object
        json_str = f.readline().strip()

        try:
            return json.loads(json_str)
        except:
            raise ValueError(f"cannot find valid json in {summary_path}")


def generate_summary_text_lines(summaries):
    # sort summaries based on month

    sorted_summaries = {}

    for info in summaries:
        line = generate_bullet_point(info)
        key = get_month_key(info["date"])

        if key in sorted_summaries:
            sorted_summaries[key] += [line]
        else:
            sorted_summaries[key] = [line]

    # get the keys in descending order of time
    sorted_keys = sorted(sorted_summaries.keys(), reverse=True)

    # generate the lines of each month
    text = []

    for month_key in sorted_keys:
        lines = [get_month_header(month_key) + "\n"]
        lines += sorted_summaries[month_key]
        lines += [""]

        text += lines

    return text


def get_month_key(date_str: str):
    return date_str[:date_str.rfind("-")]


def get_month_header(month_key):
    # Structure output: yyyy - MMMM
    dt = datetime.datetime.fromisoformat(month_key + "-01")

    return dt.strftime("### %Y - %B")


def generate_bullet_point(info):
    # Structure:
    # <[Title of paper](link to pdf) - [summary/notes](link to markdown) - time spent-->

    title = info['title']
    url = info['url']
    path_to_md = info['file_path']
    time_spent = info['estimated_minutes']

    return f" * [{title}]({url}) - [summary]({path_to_md}) - {time_spent} minutes)  \n"


def main():
    # set working directory to root of path
    script_path = Path(os.path.abspath(__file__))
    root_dir = script_path.parent.parent.as_posix()

    os.chdir(root_dir)

    # parse all the summaries
    summaries_dir = os.path.join(root_dir, "summaries")
    summaries = []

    for file in os.listdir(summaries_dir):
        info = get_json_from_summary(os.path.join(summaries_dir, file))
        info["file_path"] = os.path.join("summaries", file)

        summaries.append(info)

    # generate README text of the summaries
    summaries_text_lines = generate_summary_text_lines(summaries)

    # load current README
    with open("README.md", 'r') as f:
        readme_lines = f.readlines()

    # generate the new README
    new_readme_lines = []

    for line in readme_lines:
        if readme_separator in line:
            new_readme_lines.append(line)
            break

        new_readme_lines.append(line)

    new_readme_lines += summaries_text_lines

    # save backup of old README and update new README
    with open("README.md.bck", 'w') as f:
        f.writelines(readme_lines)

    with open("README.md", "w") as f:
        f.writelines(new_readme_lines)


if __name__ == '__main__':
    main()
