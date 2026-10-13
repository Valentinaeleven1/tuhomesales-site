const yearEl = document.getElementById('year');
if (yearEl) {
  yearEl.textContent = new Date().getFullYear();
}

const counters = document.querySelectorAll('[data-count]');

const animateCounter = (element) => {
  const target = Number(element.dataset.count);
  const duration = 1200;
  const start = performance.now();

  const update = (now) => {
    const progress = Math.min((now - start) / duration, 1);
    const eased = 1 - Math.pow(1 - progress, 3);
    const value = target * eased;

    element.textContent = target % 1 === 0 ? Math.round(value) : value.toFixed(1);

    if (progress < 1) {
      requestAnimationFrame(update);
    } else {
      element.textContent = target % 1 === 0 ? target : target.toFixed(1);
    }
  };

  requestAnimationFrame(update);
};

counters.forEach((counter) => {
  animateCounter(counter);
});
