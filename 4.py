import os
import sys
import subprocess
from collections import Counter
from tabulate import tabulate

mrjob_code = '''
from mrjob.job import MRJob

class MRWordCount(MRJob):

    def mapper(self, _, line):
        words = line.split()
        for word in words:
            yield word, 1

    def reducer(self, word, counts):
        yield word, sum(counts)

if __name__ == '__main__':
    MRWordCount.run()
'''

with open('word_count_script.py', 'w') as script_file:
    script_file.write(mrjob_code)

input_filename = sys.argv[1] if len(sys.argv) > 1 else 'input.txt'

if not os.path.exists(input_filename):
    print(f"Error: The file '{input_filename}' was not found.")
    sys.exit(1)

print("Running MapReduce job...")

proc = subprocess.run([sys.executable, 'word_count_script.py', input_filename], capture_output=True, text=True)
if proc.returncode != 0:
    stderr = proc.stderr or ""
    if 'No module named' in stderr and 'mrjob' in stderr:
        print("mrjob not found — falling back to local word count.")
        counts = Counter()
        with open(input_filename, 'r', encoding='utf-8') as inf:
            for ln in inf:
                for w in ln.split():
                    counts[w] += 1
        with open('temp_output.txt', 'w', encoding='utf-8') as tmpf:
            for w, c in counts.items():
                tmpf.write(f'"{w}"\t{c}\n')
    else:
        print("MapReduce job failed:")
        if proc.stderr:
            print(proc.stderr)
        sys.exit(proc.returncode)

if proc.returncode == 0:
    with open('temp_output.txt', 'w', encoding='utf-8') as tmpf:
        tmpf.write(proc.stdout)
word_counts = []
with open('temp_output.txt', 'r', encoding='utf-8') as output_file:
    for line in output_file:
        line = line.strip()
        if not line:
            continue
        parts = line.split('\t')
        if len(parts) == 2:
            word, count = parts
            word = word.strip('"')
            try:
                count = int(count)
            except ValueError:
                continue
        else:
            tokens = line.rsplit(' ', 1)
            if len(tokens) == 2 and tokens[1].lstrip('-').isdigit():
                word = tokens[0].strip('"')
                count = int(tokens[1])
            else:
                continue
        word_counts.append((word, count))

word_counts.sort(key=lambda x: x[1], reverse=True)

print("\n--- MapReduce Results ---")
table = tabulate(word_counts, headers=['Word', 'Count'], tablefmt='grid')
print(table)

if os.path.exists('temp_output.txt'):
    os.remove('temp_output.txt')