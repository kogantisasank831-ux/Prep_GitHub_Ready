"use strict";
window.PrepStorage = (() => {
  let warned = false;
  const memory = new Map();
  function warn() {
    if (warned) return;
    warned = true;
    const show = () => {
      const note = document.createElement("p");
      note.className = "storage-notice";
      note.setAttribute("role", "status");
      note.textContent = "Browser storage is unavailable. Your changes may not survive a refresh.";
      document.body.prepend(note);
    };
    if (document.body) show(); else document.addEventListener("DOMContentLoaded", show, {once:true});
  }
  return {
    get(key) { try { return localStorage.getItem(key); } catch { warn(); return memory.get(key) ?? null; } },
    set(key, value) { memory.set(key, value); try { localStorage.setItem(key, value); return true; } catch { warn(); return false; } }
  };
})();
