const drawBtn = document.getElementById('draw');
const interpretBtn = document.getElementById('interpret');
const cardsEl = document.getElementById('cards');
const resultsEl = document.getElementById('results');

let lastCards = [];

async function apiDraw(n) {
  const res = await fetch(`/api/draw?n=${n}`);
  return res.json();
}

async function apiInterpret(cards) {
  const res = await fetch(`/api/interpret`, {
    method: 'POST',
    headers: {'Content-Type': 'application/json'},
    body: JSON.stringify({cards})
  });
  return res.json();
}

function renderCards(cards) {
  cardsEl.innerHTML = '';
  cards.forEach((c, i) => {
    const d = document.createElement('div');
    d.className = 'card';
    const img = document.createElement('img');
    img.src = `/static/images/${c.id}.svg`;
    img.alt = c.name;
    if (c.reversed) img.classList.add('reversed');
    d.appendChild(img);
    const m = document.createElement('div');
    m.className = 'meta';
    m.textContent = c.reversed ? '逆位' : '';
    d.appendChild(m);
    cardsEl.appendChild(d);
  });
}

function renderInterpretations(iters) {
  resultsEl.innerHTML = '';
  iters.forEach(it => {
    const p = document.createElement('div');
    p.className = 'interpret';
    p.innerHTML = `<h3>${it.name} ${it.reversed? '（逆位）':''}</h3><p>${it.text}</p>`;
    resultsEl.appendChild(p);
  });
}

drawBtn.addEventListener('click', async () => {
  const n = document.getElementById('count').value;
  resultsEl.innerHTML = '';
  const data = await apiDraw(n);
  lastCards = data.cards;
  renderCards(lastCards);
  interpretBtn.classList.remove('hidden');
  // staggered deal animation
  const cardNodes = Array.from(document.querySelectorAll('.card'));
  cardNodes.forEach((node, i) => {
    node.classList.remove('deal');
    setTimeout(() => node.classList.add('deal'), 80 * i);
  });
});

interpretBtn.addEventListener('click', async () => {
  if (!lastCards.length) return;
  const data = await apiInterpret(lastCards);
  renderInterpretations(data.interpretations);
  // animate interpretations appearing
  const items = document.querySelectorAll('.interpret');
  items.forEach((it, idx) => setTimeout(() => it.classList.add('show'), idx * 120));
});
