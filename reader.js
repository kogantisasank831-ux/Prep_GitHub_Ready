"use strict";
(() => {
  const article = document.querySelector("#lesson-content");
  if (!article) return;
  const week = article.dataset.week;
  const key = "applied-genai-roadmap-v1";
  function readState() {
    try { const s = JSON.parse(window.PrepStorage.get(key) || "{}");
      return { ...s, completed: Array.isArray(s.completed) ? s.completed.map(String) : [], notes: s.notes && typeof s.notes === "object" ? s.notes : {} };
    } catch { return { completed: [], notes: {} }; }
  }
  const checkbox = document.querySelector("#lesson-complete");
  const notes = document.querySelector("#lesson-notes");
  const state = readState();
  checkbox.checked = state.completed.includes(week);
  notes.value = state.notes[week] ?? "";
  checkbox.addEventListener("change", () => {
    const s = readState(); const completed = new Set(s.completed);
    checkbox.checked ? completed.add(week) : completed.delete(week);
    s.completed = [...completed]; window.PrepStorage.set(key, JSON.stringify(s));
  });
  notes.addEventListener("input", () => { const s = readState(); s.notes[week] = notes.value; window.PrepStorage.set(key, JSON.stringify(s)); });
  window.PrepStorage.set("applied-genai-last-week", week);

  // Keep all content in the document: progressive enhancement, print and no-JS work.
  const sections = [];
  let section = null;
  for (const node of [...article.childNodes]) {
    if (node.nodeType === 1 && node.tagName === "H2") {
      section = document.createElement("section"); section.className = "lesson-chapter";
      article.insertBefore(section, node); sections.push(section);
    }
    if (section) section.append(node);
  }
  if (!sections.length) return;
  // Answer keys stay accessible through native disclosure, including keyboard use.
  for (const heading of article.querySelectorAll("h3")) {
    if (!/answer key|suggested answer/i.test(heading.textContent)) continue;
    const details = document.createElement("details"); details.className = "answer-feedback";
    const summary = document.createElement("summary"); summary.textContent = "Reveal answer key";
    details.append(summary); heading.before(details);
    let next = heading.nextSibling;
    while (next && !(next.nodeType === 1 && /H[23]/.test(next.tagName))) {
      const move = next; next = next.nextSibling; details.append(move);
    }
    details.appendChild(heading); heading.hidden = true;
  }
  let full = false; let current = 0;
  const controls = document.createElement("nav"); controls.className = "chapter-controls";
  controls.setAttribute("aria-label", "Lesson reading controls");
  function button(label, handler) { const b = document.createElement("button"); b.type = "button"; b.textContent = label; b.addEventListener("click", handler); controls.append(b); return b; }
  const previous = button("← Previous section", () => go(current - 1));
  const count = document.createElement("span"); count.setAttribute("aria-live", "polite"); controls.append(count);
  const next = button("Next section →", () => go(current + 1));
  const all = button("Show full lesson", () => { full = !full; show(); });
  article.before(controls);
  function show() {
    sections.forEach((s, i) => s.hidden = !full && i !== current);
    previous.disabled = full || current === 0; next.disabled = full || current === sections.length - 1;
    all.textContent = full ? "Read section by section" : "Show full lesson";
    count.textContent = full ? `${sections.length} sections` : `${current + 1} / ${sections.length}`;
    document.querySelectorAll("#lesson-toc a").forEach(a => a.classList.toggle("active", a.hash === `#${sections[current].querySelector('h2').id}`));
    window.dispatchEvent(new Event("resize"));
  }
  function go(index) {
    current = Math.max(0, Math.min(sections.length - 1, index));
    const h = sections[current].querySelector("h2"); history.replaceState(null, "", `#${h.id}`); show(); h.tabIndex = -1; h.focus({preventScroll:true}); controls.scrollIntoView({block:"start"});
  }
  function fromHash() {
    let id; try { id = decodeURIComponent(location.hash.slice(1)); } catch { return; }
    const target = document.getElementById(id);
    const found = sections.findIndex(s => s === target || s.contains(target));
    if (found >= 0) { current = found; show(); target.scrollIntoView({block:"start"}); } else show();
  }
  window.addEventListener("hashchange", fromHash); fromHash();
})();
