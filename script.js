const navbar = document.querySelector('.navbar');
const navToggle = document.querySelector('.nav-toggle');
const revealItems = document.querySelectorAll('.reveal');

navToggle?.addEventListener('click', () => {
  const isOpen = navbar.classList.toggle('open');
  navToggle.setAttribute('aria-expanded', String(isOpen));
});

document.querySelectorAll('.nav-menu a, .nav-actions a').forEach((link) => {
  link.addEventListener('click', () => {
    navbar?.classList.remove('open');
    navToggle?.setAttribute('aria-expanded', 'false');
  });
});

function initTabs(tabBarSelector, panelAttr, tabAttr) {
  const tabBars = document.querySelectorAll(tabBarSelector);
  tabBars.forEach((tabBar) => {
    const section = tabBar.closest('section');
    if (!section) return;

    const tabs = tabBar.querySelectorAll('.tab');
    const panels = section.querySelectorAll(`[${panelAttr}]`);

    tabs.forEach((tab) => {
      tab.addEventListener('click', () => {
        const key = tab.getAttribute(tabAttr);
        tabs.forEach((t) => {
          t.classList.remove('active');
          t.setAttribute('aria-selected', 'false');
        });
        tab.classList.add('active');
        tab.setAttribute('aria-selected', 'true');

        panels.forEach((panel) => {
          const match = panel.getAttribute(panelAttr) === key;
          panel.classList.toggle('active', match);
          panel.hidden = !match;
        });
      });
    });
  });
}

initTabs('.capabilities .tab-bar', 'data-panel', 'data-tab');
initTabs('.security .tab-bar', 'data-sec-panel', 'data-sec-tab');

const deployTabs = document.querySelectorAll('.deploy-tab');
const deployCards = document.querySelectorAll('.deploy-card');
const deployCardsWrap = document.querySelector('.deploy-cards');

deployTabs.forEach((tab) => {
  tab.addEventListener('click', () => {
    const mode = tab.dataset.deploy;
    deployTabs.forEach((t) => {
      t.classList.remove('active');
      t.setAttribute('aria-selected', 'false');
    });
    tab.classList.add('active');
    tab.setAttribute('aria-selected', 'true');

    deployCards.forEach((card) => {
      const isActive = card.dataset.deployPanel === mode;
      card.classList.toggle('active', isActive);
    });

    deployCardsWrap?.classList.toggle('show-self', mode === 'self');
  });
});

const faqTriggers = document.querySelectorAll('.faq-trigger');

faqTriggers.forEach((trigger) => {
  trigger.addEventListener('click', () => {
    const expanded = trigger.getAttribute('aria-expanded') === 'true';
    const panelId = trigger.getAttribute('aria-controls');
    const panel = panelId ? document.getElementById(panelId) : null;

    faqTriggers.forEach((other) => {
      if (other !== trigger) {
        other.setAttribute('aria-expanded', 'false');
        const otherPanel = document.getElementById(other.getAttribute('aria-controls'));
        if (otherPanel) otherPanel.hidden = true;
      }
    });

    const nextExpanded = !expanded;
    trigger.setAttribute('aria-expanded', String(nextExpanded));
    if (panel) panel.hidden = !nextExpanded;
  });
});

function animateStat(el) {
  const target = Number(el.dataset.target);
  const suffix = el.dataset.suffix || '';
  const duration = 1400;
  const start = performance.now();

  function tick(now) {
    const progress = Math.min((now - start) / duration, 1);
    const eased = 1 - (1 - progress) ** 3;
    const value = Math.round(target * eased);
    el.textContent = `${value}${suffix}`;
    if (progress < 1) requestAnimationFrame(tick);
  }

  requestAnimationFrame(tick);
}

const statObserver = new IntersectionObserver(
  (entries) => {
    entries.forEach((entry) => {
      if (!entry.isIntersecting) return;
      const el = entry.target;
      if (el.dataset.animated) return;
      el.dataset.animated = 'true';
      animateStat(el);
      statObserver.unobserve(el);
    });
  },
  { threshold: 0.4 },
);

document.querySelectorAll('.stat-value').forEach((el) => statObserver.observe(el));

const revealObserver = new IntersectionObserver(
  (entries) => {
    entries.forEach((entry) => {
      if (entry.isIntersecting) {
        entry.target.classList.add('visible');
        revealObserver.unobserve(entry.target);
      }
    });
  },
  { threshold: 0.12 },
);

revealItems.forEach((item) => revealObserver.observe(item));
