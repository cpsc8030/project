
import subprocess
import time
import os
import re
import concurrent.futures

dir_files = '/Users/dmitry/Dev/workspace/clemson/sv/project/SciVisContest23/viz-no-network/timeseries/sample/neurons/'
dir_output = '/Users/dmitry/Dev/workspace/clemson/sv/project/SciVisContest23/viz-no-network/timeseries/sample/images_fixed/'

files = os.listdir(dir_files)
files = list(filter(lambda x: re.match(r".*_full.*", x), files))
files = sorted(files)

parameter = 'current_calcium'

angle_delta = 360.0 / (len(files) / 3.0)

def run_script(dir_in, dir_out, fn, angle):
    subprocess.run(['/Applications/ParaView-5.11.0.app/Contents/bin/pvpython', 'video_static_item.py', dir_in, dir_out, fn, str(angle)])


start = 0
chunk_size = 200

angle_multiplier = start
while start < 10000:
    with concurrent.futures.ThreadPoolExecutor(max_workers=8) as executor:
        futures = []
        for i, fn in enumerate(files[start:start + chunk_size]):
            print(fn)
            future = executor.submit(run_script, dir_files, dir_output, fn, angle_multiplier * angle_delta)
            futures.append(future)
            angle_multiplier += 1

        for future in concurrent.futures.as_completed(futures):
            pass

    start += chunk_size
    time.sleep(60 * 10)