import git

repo = git.Repo('./')
commits = list(repo.iter_commits('master', max_count=50))  # Adjust as needed

diffs = []
for commit in commits:
    for diff_item in commit.diff():
        diffs.append(diff_item)

from transformers import GPT2Tokenizer, GPT2LMHeadModel

tokenizer = GPT2Tokenizer.from_pretrained("gpt2-medium")
model = GPT2LMHeadModel.from_pretrained("gpt2-medium")

def summarize(diff):
    input_text = "Summarize the following code change: " + diff
    input_ids = tokenizer.encode(input_text, return_tensors="pt")
    output = model.generate(input_ids, max_length=100, num_return_sequences=1, no_repeat_ngram_size=2)
    summary = tokenizer.decode(output[0], skip_special_tokens=True)
    return summary

summaries = [summarize(diff) for diff in diffs]



def create_update_summary(summaries):
    update_note = " ".join(summaries)
    input_text = "Provide a general summary of the following update: " + update_note
    input_ids = tokenizer.encode(input_text, return_tensors="pt")
    output = model.generate(input_ids, max_length=200, num_return_sequences=1, no_repeat_ngram_size=2)
    return tokenizer.decode(output[0], skip_special_tokens=True)

update_summary = create_update_summary(summaries)
print(update_summary)