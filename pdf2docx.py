import os
import subprocess

for top, dirs, files in os.walk('/home/ankit/Desktop/freelance/9th March 2018 Emerald'):
    for filename in files:
        if filename.endswith('.pdf'):
            abspath = os.path.join(top, filename)
            subprocess.call('abiword --to=docx "{}"'
                            .format(abspath), shell=True)
