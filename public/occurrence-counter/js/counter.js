let minResults = 0;
function calculate() {
  const data = document.getElementById('data').value;
  const list = data.split(determineDelimiter(data));

  const countedItems = new Map();
  list.forEach(function (item, index) {
    countedItems.set(item, (countedItems.get(item) || 0) + 1);
  });
  const sortedMap = new Map([...countedItems.entries()].sort());

  let result = '';
  sortedMap.forEach(function (value, key) {
    if (value >= minResults) {
      result += key + ' - ' + value + '<br>';
    }
  });
  document.getElementById('results').innerHTML = result;
}

function determineDelimiter(data) {
  const returnCount = data.split('\n').length;
  const commaCount = data.split(',').length;
  const pipeCount = data.split('|').length;

  if (returnCount > commaCount && returnCount > pipeCount) {
    return '\n';
  } else if (commaCount > pipeCount) {
    return ',';
  }
  return '|';
}

document.getElementById('data').addEventListener('keyup', function () {
  calculate();
});
document.getElementById('minCount').addEventListener('input', function () {
  minResults = document.getElementById('minCount').value;
  calculate();
});
