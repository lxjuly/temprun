const form = document.querySelector("#runForm");
const statusPill = document.querySelector("#runStatus");
const eventLog = document.querySelector("#eventLog");
const attemptsSummary = document.querySelector("#attemptsSummary");
const lesson = document.querySelector("#lesson");

const stateEls = {
  request: document.querySelector('[data-step="request"]'),
  plan: document.querySelector('[data-step="plan"]'),
  synthesis: document.querySelector('[data-step="synthesis"]'),
  brief: document.querySelector('[data-step="brief"]'),
  web: document.querySelector('[data-agent="web"]'),
  systems: document.querySelector('[data-agent="systems"]'),
  critic: document.querySelector('[data-agent="critic"]'),
};

const agents = ["web", "systems", "critic"];
const delay = (ms) => new Promise((resolve) => setTimeout(resolve, ms));

function resetUi(topic) {
  eventLog.replaceChildren();
  document.querySelector("#requestText").textContent = topic;
  document.querySelector("#synthesisText").textContent = "waiting";
  document.querySelector("#briefText").textContent = "not started";
  attemptsSummary.textContent = "0 attempts";
  statusPill.textContent = "running";
  statusPill.className = "status-pill running";
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

async function runAgent(agent, failAgent, attempts) {
  setStep(agent, "active");
  document.querySelector(`#${agent}State`).textContent = "attempt 1";
  attempts.count += 1;
  attemptsSummary.textContent = `${attempts.count} attempts`;
  await delay(420 + agents.indexOf(agent) * 130);

  if (failAgent === agent) {
    setStep(agent, "retry");
    document.querySelector(`#${agent}State`).textContent = "failed, retry scheduled";
    logEvent(`${agent}`, "Activity failed once; RetryPolicy schedules attempt 2.");
    await delay(560);
    attempts.count += 1;
    attemptsSummary.textContent = `${attempts.count} attempts`;
    document.querySelector(`#${agent}State`).textContent = "attempt 2";
    await delay(420);
  }

  setStep(agent, "done");
  document.querySelector(`#${agent}State`).textContent = "completed";
  return `${agent}: finding captured`;
}

async function runWorkflow(event) {
  event.preventDefault();

  const formData = new FormData(form);
  const topic = formData.get("topic").toString().trim() || "Temporal workflow determinism";
  const depth = formData.get("depth").toString();
  const failAgent = formData.get("failAgent").toString();
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

  logEvent("Workflow", "fan-out scheduled three Activities in parallel.");
  const results = await Promise.all(agents.map((agent) => runAgent(agent, failAgent, attempts)));

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
