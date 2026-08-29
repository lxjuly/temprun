const form = document.querySelector("#runForm");
const statusPill = document.querySelector("#runStatus");
const eventLog = document.querySelector("#eventLog");
const attemptsSummary = document.querySelector("#attemptsSummary");
const lesson = document.querySelector("#lesson");
const flow = document.querySelector(".flow");
const agentGrid = document.querySelector(".agent-grid");

const stateEls = {
  request: document.querySelector('[data-step="request"]'),
  plan: document.querySelector('[data-step="plan"]'),
  synthesis: document.querySelector('[data-step="synthesis"]'),
  brief: document.querySelector('[data-step="brief"]'),
  web: document.querySelector('[data-agent="web"]'),
  papers: document.querySelector('[data-agent="papers"]'),
  systems: document.querySelector('[data-agent="systems"]'),
  implementation: document.querySelector('[data-agent="implementation"]'),
  security: document.querySelector('[data-agent="security"]'),
  critic: document.querySelector('[data-agent="critic"]'),
};

const agents = ["web", "papers", "systems", "implementation", "security", "critic"];
const failureScenarios = {
  "": {},
  "systems-once": { systems: 1 },
  "systems-twice": { systems: 2 },
  "source-and-security": { papers: 1, security: 1 },
  multiple: { papers: 1, systems: 2, security: 1 },
};
const delay = (ms) => new Promise((resolve) => setTimeout(resolve, ms));

function resetUi(topic) {
  eventLog.replaceChildren();
  document.querySelector("#requestText").textContent = topic;
  document.querySelector("#synthesisText").textContent = "waiting";
  document.querySelector("#briefText").textContent = "not started";
  attemptsSummary.textContent = "0 attempts";
  statusPill.textContent = "running";
  statusPill.className = "status-pill running";
  flow.classList.remove("fanout-running");
  agentGrid.classList.remove("running");
  lesson.textContent =
    "Temporal records Activity attempts in history and retries by policy.";

  for (const node of Object.values(stateEls)) {
    node.classList.remove("active", "done", "retry");
  }
  for (const agent of agents) {
    document.querySelector(`#${agent}State`).textContent = "queued";
  }
}

function setStep(name, state) {
  stateEls[name].classList.remove("active", "done", "retry");
  if (state) {
    stateEls[name].classList.add(state);
  }
}

function logEvent(title, detail) {
  const item = document.createElement("li");
  item.innerHTML = `<strong>${title}</strong> ${detail}`;
  eventLog.append(item);
}

function updateAttemptCount(attempts) {
  attemptsSummary.textContent = `${attempts.count} attempts`;
}

async function runAgent(agent, failureCount, attempts) {
  const agentEl = stateEls[agent];
  setStep(agent, "active");

  for (let attempt = 1; attempt <= failureCount; attempt += 1) {
    agentEl.style.setProperty("--attempt-duration", `${900 + agents.indexOf(agent) * 110}ms`);
    document.querySelector(`#${agent}State`).textContent = `attempt ${attempt}`;
    attempts.count += 1;
    updateAttemptCount(attempts);
    await delay(900 + agents.indexOf(agent) * 110);
    setStep(agent, "retry");
    document.querySelector(`#${agent}State`).textContent = `failed, retry ${attempt + 1} scheduled`;
    logEvent(`${agent}`, `Activity attempt ${attempt} failed; RetryPolicy schedules attempt ${attempt + 1}.`);
    await delay(620);
    setStep(agent, "active");
  }

  const finalAttempt = failureCount + 1;
  agentEl.style.setProperty("--attempt-duration", `${1100 + agents.indexOf(agent) * 130}ms`);
  document.querySelector(`#${agent}State`).textContent = `attempt ${finalAttempt}`;
  attempts.count += 1;
  updateAttemptCount(attempts);
  await delay(1100 + agents.indexOf(agent) * 130);
  setStep(agent, "done");
  document.querySelector(`#${agent}State`).textContent = `completed on attempt ${finalAttempt}`;
  return `${agent}: finding captured after ${finalAttempt} attempt${finalAttempt === 1 ? "" : "s"}`;
}

async function runWorkflow(event) {
  event.preventDefault();

  const formData = new FormData(form);
  const topic = formData.get("topic").toString().trim() || "Temporal workflow determinism";
  const depth = formData.get("depth").toString();
  const scenarioName = formData.get("failureScenario").toString();
  const failures = failureScenarios[scenarioName] || {};
  const attempts = { count: 0 };

  resetUi(topic);

  setStep("request", "active");
  logEvent("Workflow", `started for ${topic}.`);
  await delay(360);
  setStep("request", "done");

  setStep("plan", "active");
  logEvent("Activity", `plan_research selected ${agents.join(", ")} agents.`);
  await delay(520);
  setStep("plan", "done");

  const failingAgents = Object.entries(failures)
    .filter(([, count]) => count > 0)
    .map(([agent, count]) => `${agent} x${count}`)
    .join(", ");
  logEvent("Workflow", "fan-out scheduled six Activities in parallel.");
  logEvent("Failure plan", failingAgents || "no controlled Activity failures.");
  flow.classList.add("fanout-running");
  agentGrid.classList.add("running");
  statusPill.textContent = "6 parallel";
  const results = await Promise.all(
    agents.map((agent) => runAgent(agent, failures[agent] || 0, attempts))
  );
  flow.classList.remove("fanout-running");
  agentGrid.classList.remove("running");

  setStep("synthesis", "active");
  document.querySelector("#synthesisText").textContent = `${results.length} results ready`;
  logEvent("Activity", `synthesize_research combined results at ${depth} depth.`);
  await delay(640);
  setStep("synthesis", "done");

  setStep("brief", "done");
  document.querySelector("#briefText").textContent = `${topic} researched by ${results.length} agents`;
  logEvent("Result", "ResearchBrief returned to the caller.");

  statusPill.textContent = "complete";
  statusPill.className = "status-pill done";
  lesson.textContent =
    "Interview point: Workflows coordinate durable state; Activities do side effects and may run more than once.";
}

form.addEventListener("submit", runWorkflow);
