"""A list of 4,000 English words."""

from wordfreq import top_n_list

words: list[str] = top_n_list("en", 4000)

if len(words) != 4000:
    raise RuntimeError("Unable to load exactly 4,000 English words.")