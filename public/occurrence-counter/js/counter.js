const dataEl = document.getElementById('data');
const minCountEl = document.getElementById('minCount');
const resultsEl = document.getElementById('results');
let minResults = 0;

function calculate() {
	const value = dataEl.value;
	const list = value.split(determineDelimiter(value));

	const counts = new Map();
	for (let i = 0, len = list.length; i < len; i++) {
		const item = list[i];
		counts.set(item, (counts.get(item) || 0) + 1);
	}

	const keys = Array.from(counts.keys()).sort();
	const output = [];
	for (let i = 0, len = keys.length; i < len; i++) {
		const key = keys[i];
		const count = counts.get(key);
		if (count >= minResults) {
			output.push(key + ' - ' + count);
		}
	}

	resultsEl.innerHTML = output.join('<br>');
}

function determineDelimiter(value) {
	let newline = 1;
	let comma = 1;
	let pipe = 1;

	for (let i = 0, len = value.length; i < len; i++) {
		switch (value[i]) {
			case '\n':
				newline++;
				break;
			case ',':
				comma++;
				break;
			case '|':
				pipe++;
				break;
		}
	}

	if (newline > comma && newline > pipe) {
		return '\n';
	}
	if (comma > pipe) {
		return ',';
	}
	return '|';
}

function updateMinResults() {
	minResults = +minCountEl.value || 0;
}

dataEl.addEventListener('input', calculate);
minCountEl.addEventListener('input', function () {
	updateMinResults();
	calculate();
});
