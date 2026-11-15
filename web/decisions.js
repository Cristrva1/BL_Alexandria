(function (root) {
  function fold(value) { return String(value || "").normalize("NFD").replace(/\p{M}/gu, "").toLowerCase(); }
  function ids(value, byId) {
    const source = Array.isArray(value) ? value : typeof value === "string" ? value.split(",") : [];
    return [...new Set(source.filter(id => typeof id === "string" && Object.hasOwn(byId, id)))].slice(0, 3);
  }
  function href(selected, byId) {
    const clean = ids(selected, byId);
    return "#/comparar" + (clean.length ? "?" + new URLSearchParams({ids:clean.join(",")}) : "");
  }
  function relationship(a, b) {
    const contains = (refs, id) => (refs || []).some(ref => (ref.id || ref) === id);
    if (contains(a.alt_refs,b.id) || contains(b.alt_refs,a.id)) return "alternative";
    if (contains(a.combine_refs,b.id) || contains(b.combine_refs,a.id)) return "complement";
    return "undocumented";
  }
  function candidates(repos, query, selected, goal, suggested=[]) {
    const terms=fold(query).trim().split(/\s+/).filter(Boolean);
    return repos.filter(item => !selected.includes(item.id)
      && (!goal || (item.goals || []).includes(goal) || suggested.includes(item.id))
      && terms.every(term => fold([item.name,item.id,item.gh,item.lead,...(item.tags||[])].join(" ")).includes(term))
      && (terms.length || goal || suggested.includes(item.id)))
      .sort((a,b) => (fold(b.name)===fold(query)?1:0)-(fold(a.name)===fold(query)?1:0) || a.name.localeCompare(b.name,"es"));
  }
  function different(row, items) { return new Set(items.map(item => JSON.stringify(row.value(item)))).size > 1; }
  function recipeParts(recipe) {
    const available=new Set(recipe.steps.filter(step=>step.id).map(step=>step.id));
    const minimum=[...new Set((recipe.plan?.minimum || []).filter(id=>available.has(id)))];
    const instead=[...new Set((recipe.plan?.instead || []).filter(id=>available.has(id) && !minimum.includes(id)))];
    return {minimum,instead,extra:[...available].filter(id=>!minimum.includes(id) && !instead.includes(id))};
  }
  const api={ids,href,relationship,candidates,different,recipeParts};
  if (typeof module === "object" && module.exports) module.exports=api;
  else root.AlexandriaDecisions=api;
})(typeof globalThis !== "undefined" ? globalThis : this);
