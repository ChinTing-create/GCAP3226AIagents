# Part 1: Instruction Files for AI Agent Interaction

## 📚 What's in This Folder?

This folder contains sample instruction files that demonstrate how to work effectively with AI coding agents.

### Files in This Folder:

1. **InstructionsSample.md** - A template showing how to structure instructions for the AI agent
2. **planGovEnquiries.md** - Output file where the AI agent will save its analysis
3. **README.md** - This file, explaining the purpose and usage

---

## 🎓 Learning Objectives

By working with these files, you will learn to:
- Structure clear instructions for AI agents
- Specify input sources, processing steps, and output destinations
- Read and analyze project folders systematically
- Generate actionable plans based on data analysis

---

## 📋 How to Use InstructionsSample.md

### The Instruction File Structure:

```markdown
Input: [What to read - folder or file paths]
Process: [What the agent should do with the input]
Additional Notes: [Your own context, requirements, or constraints]
Output: [Where to save the results]
```

### Example Workflow:

1. **Read the instruction file**
   - Ask AI: "Please read /workspaces/GCAP3226AIagents/vibeCoding101/Part1ReadingEditingFiles/InstructionsSample.md"

2. **Ask AI to explain it**
   - Ask AI: "What does this instruction file ask you to do?"

3. **Execute the instructions**
   - Ask AI: "Please follow these instructions and complete the task"

4. **Review the output**
   - Ask AI: "Show me the content of planGovEnquiries.md"
   - Ask AI: "Can you explain the plan you created?"

---

## 💡 Why Use Instruction Files?

### Traditional Approach (Verbal Prompts):
```
"Hey AI, can you read the Team1_FluShot folder and then 
look at the files and figure out what data we need and 
then create a plan for asking the government?"
```
**Problems**: Vague, hard to repeat, no documentation

### Instruction File Approach:
```
Ask AI: "Please follow the instructions in InstructionsSample.md"
```
**Benefits**: 
- ✅ Clear and structured
- ✅ Repeatable
- ✅ Documented
- ✅ Easy to modify
- ✅ Can be shared with team members

---

## 🔨 Create Your Own Instruction File

Try creating your own instruction file for a different team project!

### Exercise Template:

```markdown
Input: /workspaces/GCAP3226AIagents/Team2_BusRouteCoordination
Process: 
- Read through all markdown files in the folder
- Identify the main policy issue being addressed
- List what data is currently available
- Suggest what additional data might be needed from government
- Draft key questions for a government enquiry

Additional Notes:
[Add your own context here - what's important for this project?]

Output: /workspaces/GCAP3226AIagents/vibeCoding101/Part1ReadingEditingFiles/myTeam2Analysis.md
```

Save this as `myInstructions.md` and ask the AI to follow it!

---

## 🎯 Tips for Writing Good Instruction Files

1. **Be Specific**: Use exact file paths
2. **Break Down Tasks**: List step-by-step what the agent should do
3. **Provide Context**: Add notes about why this matters
4. **Specify Output Format**: Tell the agent how to structure results
5. **Use Examples**: Show what you expect (if helpful)

---

## 📝 For Your Reflective Essay

As you work with instruction files, consider:
- How does this structured approach compare to ad-hoc prompting?
- What skills are you developing in communicating with AI?
- How might instruction files help in government data enquiries?
- What's the relationship between clear instructions and effective AI assistance?

---

## 🚀 Next Steps

After mastering Part 1:
1. Move on to Part 2 (Exploring APIs)
2. Apply instruction file techniques to other parts of the tutorial
3. Use this approach in your group project
4. Share your instruction files with team members

---

**Remember**: The goal is not just to get the AI to do work, but to learn how to **communicate effectively** with AI tools in a professional context!

---

# How to Retrieve Data from Hong Kong Census Dataset via API

Dataset: https://data.gov.hk/en-data/dataset/hk-censtatd-tablechart-110-01001

## Steps to Retrieve Data via API
1. Go to the dataset page and look for a section labeled “API”, “Data Resource”, or “Download”.
2. If an API is available, you will see a URL ending in `.json`, `.csv`, etc.
3. Copy this URL and paste it into your browser to download the data, or use Excel/Google Sheets to import the data.

## Example API Endpoint
For many datasets, the API endpoint looks like:
```
https://data.gov.hk/api/3/action/datastore_search?resource_id=110-01001
```
You can use this URL in your browser or in code to retrieve the data.

## Pseudocode for Non-Programmers
- Step 1: Open your web browser.
- Step 2: Copy the API URL from the dataset page.
- Step 3: Paste the URL into the browser and press Enter.
- Step 4: Download the data file (CSV or JSON).
- Step 5: Open the file with Excel or Google Sheets.

## Python Example
```python
import requests
import pandas as pd

api_url = "https://data.gov.hk/api/3/action/datastore_search?resource_id=110-01001"
response = requests.get(api_url)
if response.status_code == 200:
   data = response.json()
   records = data['result']['records']
   df = pd.DataFrame(records)
   df.to_csv("census_data.csv", index=False)
   print("Data downloaded and saved as census_data.csv")
else:
   print("Failed to fetch data. Status code:", response.status_code)
```
