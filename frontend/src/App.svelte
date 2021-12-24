<script>
	export let name;

    async function getMessage() {
		const res = await fetch(`http://127.0.0.1:8080`);
		const text = await res.json();

		if (res.ok) {
			return text.message;
		} else {
			throw new Error(text);
		}
	}

	let promise = getMessage();
</script>

<main>
	<h1>Hello {name}!</h1>
</main>

<style>
	main {
		text-align: center;
		padding: 1em;
		max-width: 240px;
		margin: 0 auto;
	}

	h1 {
		color: #ff3e00;
		text-transform: uppercase;
		font-size: 4em;
		font-weight: 100;
	}

	@media (min-width: 640px) {
		main {
			max-width: none;
		}
	}
</style>