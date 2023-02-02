import os
import json

src_dir = 'completions/'
prompts_dir = 'prompts/'

def open_file(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        return f.read()


if __name__ == '__main__':
    files = os.listdir(src_dir)
    data = list()
    for file in files:
        completions = open_file(src_dir + file)
        prompts = open_file(prompts_dir + file)
        info = {'prompt': prompts, 'completion': completions}
        data.append(info)
    with open('afro_agi_scene.json', 'w') as f:
        for i in data:
            json.dump(i, f)
            f.write('\n')