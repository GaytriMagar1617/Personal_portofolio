const API = 'http://localhost:5000/api';

// ── VISITOR TRACKING ──
(async function trackVisit() {
  try {
    await fetch(`${API}/visit`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ page: window.location.pathname || '/' }),
    });
  } catch (e) {}
})();

// ── MOBILE MENU TOGGLE ──
function toggleMenu() {
  const menu = document.getElementById('mobileMenu');
  menu.classList.toggle('open');
}

// ── BACK TO TOP BUTTON ──
window.addEventListener('scroll', () => {
  const backTop = document.getElementById('backTop');
  if (window.scrollY > 400) {
    backTop.classList.add('visible');
  } else {
    backTop.classList.remove('visible');
  }
});

// ── SMOOTH SCROLL ──
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
  anchor.addEventListener('click', function (e) {
    const target = document.querySelector(this.getAttribute('href'));
    if (target) {
      e.preventDefault();
      target.scrollIntoView({ behavior: 'smooth' });
    }
  });
});

// ── CONTACT FORM SUBMIT ──
async function handleSubmit() {
  const btn    = document.getElementById('submitBtn');
  const msgDiv = document.getElementById('formMsg');

  const name    = document.getElementById('contactName').value.trim();
  const email   = document.getElementById('contactEmail').value.trim();
  const subject = document.getElementById('contactSubject').value.trim();
  const message = document.getElementById('contactMessage').value.trim();

  if (!name || !email || !message) {
    msgDiv.style.display = 'block';
    msgDiv.style.color   = '#f87171';
    msgDiv.textContent   = '⚠️ Please fill in your name, email and message.';
    return;
  }

  btn.textContent = 'Sending...';
  btn.disabled    = true;

  try {
    const res  = await fetch(`${API}/contact`, {
      method:  'POST',
      headers: { 'Content-Type': 'application/json' },
      body:    JSON.stringify({ name, email, subject, message }),
    });
    const data = await res.json();

    if (data.success) {
      btn.textContent      = 'Message Sent! ✓';
      btn.style.background = '#34d399';
      msgDiv.style.display = 'block';
      msgDiv.style.color   = '#34d399';
      msgDiv.textContent   = '✅ Your message was saved! I will get back to you soon.';

      document.getElementById('contactName').value    = '';
      document.getElementById('contactEmail').value   = '';
      document.getElementById('contactSubject').value = '';
      document.getElementById('contactMessage').value = '';

      setTimeout(() => {
        btn.textContent      = 'Send Message →';
        btn.style.background = '';
        btn.disabled         = false;
        msgDiv.style.display = 'none';
      }, 4000);
    } else {
      throw new Error(data.error || 'Unknown error');
    }
  } catch (err) {
    btn.textContent      = 'Send Message →';
    btn.disabled         = false;
    msgDiv.style.display = 'block';
    msgDiv.style.color   = '#f87171';
    msgDiv.textContent   = `❌ Failed to send: ${err.message}`;
  }
}

// ── SCROLL FADE-IN ANIMATION ──
const observer = new IntersectionObserver(
  (entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.style.opacity   = '1';
        entry.target.style.transform = 'translateY(0)';
      }
    });
  },
  { threshold: 0.1 }
);

document.querySelectorAll('.project-card, .skill-card, .timeline-item').forEach(el => {
  el.style.opacity    = '0';
  el.style.transform  = 'translateY(24px)';
  el.style.transition = 'opacity 0.5s ease, transform 0.5s ease';
  observer.observe(el);
});

// ── ACTIVE NAV HIGHLIGHT ──
const sections = document.querySelectorAll('section[id]');
const navLinks = document.querySelectorAll('.nav-links a');

window.addEventListener('scroll', () => {
  let current = '';
  sections.forEach(section => {
    const sectionTop = section.offsetTop - 100;
    if (window.scrollY >= sectionTop) {
      current = section.getAttribute('id');
    }
  });

  navLinks.forEach(link => {
    link.style.color = '';
    if (link.getAttribute('href') === `#${current}`) {
      link.style.color = 'var(--accent)';
    }
  });
});
