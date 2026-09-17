def ask(prompt):
	while True:
		answer = input(prompt).strip()
		if answer:
			return answer
		print("Please enter something.")


def collect_words():
	print("\nEnter the words for your story.")
	return {
		"adjective": ask("Adjective: "),
		"character": ask("A person's name: "),
		"place": ask("A place: "),
		"animal": ask("An animal: "),
		"food": ask("A food: "),
		"object": ask("An object: "),
		"verb": ask("A past-tense verb: "),
		"verb_ing": ask("A verb ending in -ing: "),
		"sound": ask("A funny sound: "),
		"number": ask("A number: "),
		"emotion": ask("An emotion: "),
	}


def tell_story(words):
	print("\n" + "=" * 72)
	print("THE MIDNIGHT MUSEUM HEIST")
	print("=" * 72)
	print(
		f"At exactly midnight, {words['character']} received a {words['adjective']} "
		f"message inviting them to enter the museum in {words['place']}. The message "
		f"promised a reward: {words['number']} pieces of {words['food']} and a "
		f"mysterious {words['object']} hidden behind the oldest painting."
	)
	print(
		f"When {words['character']} arrived, a talking {words['animal']} blocked "
		f"the door. The guard demanded a password, so {words['character']} "
		f"{words['verb']} a dramatic dance while {words['animal']} shouted "
		f"\"{words['sound']}!\""
	)
	print(
		f"The plan almost failed when the alarm began {words['verb_ing']} through "
		f"the halls. Feeling {words['emotion']}, {words['character']} grabbed the "
		f"{words['object']} and sprinted past a room full of statues. Just before "
		f"the doors locked, the {words['animal']} revealed that the entire heist "
		f"was actually an audition for the museum's strangest new night guard."
	)
	print("=" * 72)


def play():
	print("\nWelcome to Midnight Museum Mad Libs!")
	print("Fill in the prompts and create a story that probably should not be trusted.")
	tell_story(collect_words())


while True:
	play()
	again = input("\nMake another story? (y/n): ").strip().lower()
	if again not in {"y", "yes"}:
		print("\nThanks for playing!")
		break