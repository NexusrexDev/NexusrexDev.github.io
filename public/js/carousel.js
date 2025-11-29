document.addEventListener('DOMContentLoaded', function () {
  const carousels = document.querySelectorAll('[data-carousel]');

  carousels.forEach((carousel) => {
    const track = carousel.querySelector('.carousel-track');
    const slides = Array.from(carousel.querySelectorAll('.carousel-slide'));
    const prevBtn = carousel.querySelector('.carousel-prev');
    const nextBtn = carousel.querySelector('.carousel-next');
    const indicators = Array.from(carousel.querySelectorAll('.carousel-indicator'));

    if (!track || slides.length === 0) return;

    let index = 0;
    const setPosition = () => {
      const offset = -index * 100;
      track.style.transform = `translateX(${offset}%)`;
      indicators.forEach((btn, i) => btn.classList.toggle('active', i === index));
    };

    // Hook up buttons
    if (prevBtn) prevBtn.addEventListener('click', () => {
      index = (index - 1 + slides.length) % slides.length;
      setPosition();
    });
    if (nextBtn) nextBtn.addEventListener('click', () => {
      index = (index + 1) % slides.length;
      setPosition();
    });

    // Indicators
    indicators.forEach((btn) => {
      btn.addEventListener('click', (e) => {
        const slide = parseInt(btn.getAttribute('data-slide'), 10) || 0;
        index = Math.max(0, Math.min(slide, slides.length - 1));
        setPosition();
      });
    });

    // Keyboard navigation while focused
    carousel.addEventListener('keydown', (e) => {
      if (e.key === 'ArrowLeft') {
        index = (index - 1 + slides.length) % slides.length; setPosition();
      } else if (e.key === 'ArrowRight') {
        index = (index + 1) % slides.length; setPosition();
      }
    });

    // Initialize
    setPosition();
  });
});
