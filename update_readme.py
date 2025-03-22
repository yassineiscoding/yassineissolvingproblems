import os
import re
import datetime
from collections import defaultdict

def scan_solutions(directory='.'):
    solved_problems = []
    difficulty_count = defaultdict(int)
    latest_submission = None
    latest_time = None
    
    for problem_folder in sorted(os.listdir(directory)):
        problem_path = os.path.join(directory, problem_folder)
        if not os.path.isdir(problem_path):
            continue
        
        readme_file = os.path.join(problem_path, 'README.md')
        if not os.path.exists(readme_file):
            continue
        
        with open(readme_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        title_match = re.search(r'##\s*(\d+\.\s*.+)', content)
        difficulty_match = re.search(r'\b(Easy|Medium|Hard)\b', content)
        
        problem_name = title_match.group(1) if title_match else problem_folder
        difficulty = difficulty_match.group(1) if difficulty_match else "Unknown"
        submission_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        problem_link = f"[{problem_name}]({problem_folder})"
        
        solved_problems.append((difficulty, problem_link))
        difficulty_count[difficulty] += 1
        
        if latest_time is None or submission_time > latest_time:
            latest_time = submission_time
            latest_submission = (problem_name, problem_folder, submission_time)

    return solved_problems, difficulty_count, latest_submission

def generate_readme(solved_problems, difficulty_count, latest_submission, output_file='README.md'):
    difficulty_icons = {"Easy": "🟢", "Medium": "🟡", "Hard": "🔴"}
    
    total_solved = sum(difficulty_count.values())
    stats_section = f"""
## LeetCode Progress

- **Total Problems Solved:** {total_solved}
- **Easy:** {difficulty_count['Easy']} 🟢
- **Medium:** {difficulty_count['Medium']} 🟡
- **Hard:** {difficulty_count['Hard']} 🔴
    """
    
    if latest_submission:
        latest_section = f"""
### Most Recent Submission
- **Problem:** [{latest_submission[0]}]({latest_submission[1]})
- **Submitted On:** {latest_submission[2]}
        """
    else:
        latest_section = "### Most Recent Submission\n_No recent submissions found._"
    
    problem_list = "\n".join([f"- {difficulty_icons.get(d, '')} {p}" for d, p in sorted(solved_problems)])
    problem_section = f"""ß
    ## Solved Problems
    {problem_list if problem_list else "No problems solved yet."}
    """
    
    full_readme = f"{stats_section}\n\n{latest_section}\n\n{problem_section}"
    
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(full_readme)

if __name__ == "__main__":
    solutions, difficulty_stats, latest = scan_solutions()
    generate_readme(solutions, difficulty_stats, latest)
