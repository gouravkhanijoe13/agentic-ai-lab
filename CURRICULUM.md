# AI/LLM/Agents Learning Curriculum
**Learner:** Gourav Khanijoe | **Started:** 2026-04-29  
**Goal:** Become a practical AI/LLM/Agents Engineer. Build open-source proof of expertise.

---

## Phase 1: Core Curriculum — COMPLETE ✅

| # | Topic | Status | Date |
|---|-------|--------|------|
| 1 | LLM Fundamentals: What is an LLM? Calling the API, tokens, responses | ✅ Done | 2026-04-29 |
| 2 | Prompt Engineering: System prompts, temperature, few-shot, chain-of-thought | ✅ Done | 2026-04-30 |
| 3 | Tool Use / Function Calling: Give LLMs the ability to act | ✅ Done | 2026-05-02 |
| 4 | Building Your First Agent: ReAct loop, planning, execution | ✅ Done | 2026-05-03 |
| 5 | Agent Memory: Short-term, long-term, episodic memory patterns | ✅ Done | 2026-05-04 |
| 6 | Multi-Agent Systems: Orchestrators, subagents, handoffs | ✅ Done | 2026-05-05 |
| 7 | RAG (Retrieval Augmented Generation): Embeddings + vector search | ✅ Done | 2026-05-06 |
| 8 | Productionizing AI: Observability, evals, rate limits, cost | ✅ Done | 2026-05-07 |
| 9 | Capstone: AutoResearcher Agent — full open-source agent project | ✅ Done | 2026-05-08 |

---

## Phase 2: Advanced AI Engineering — COMPLETE ✅

| # | Topic | Status | Date |
|---|-------|--------|------|
| 10 | Structured Outputs & Validation: Pydantic, instructor, typed agents | ✅ Done | 2026-05-09 |
| 11 | LangGraph — Stateful Agent Graphs: cycles, branching, state machines | ✅ Done | 2026-05-10 |
| 12 | Fine-tuning Fundamentals: when to fine-tune, data prep, LoRA | ✅ Done | 2026-05-11 |
| 13 | Multimodal AI — Vision + Text: image understanding, Claude vision API | ✅ Done | 2026-05-12 |
| 14 | MCP — Model Context Protocol: build tools that plug into any AI system | ✅ Done | 2026-05-13 |
| 15 | Open-Source Project Publishing: GitHub, README, packaging, community | ✅ Done | 2026-05-14 |

---

## Phase 3: From Engineer to Expert — COMPLETE ✅

| # | Topic | Status | Date |
|---|-------|--------|------|
| 16 | **Deployment**: FastAPI + Docker + Fly.io/Railway | ✅ Done | 2026-05-15 |
| 17 | **Advanced Evals**: RAGAS, LLM-judge pipelines, eval datasets | ✅ Done | 2026-05-16 |
| 18 | **AI Security**: Prompt injection, guardrails, red-teaming, PII | ✅ Done | 2026-05-17 |
| 19 | **Streaming Agents**: SSE, real-time UIs with Streamlit/Gradio | ✅ Done | 2026-05-18 |
| 20 | **Vector DB in Production**: hnswlib, sqlite-vec, hybrid + RRF, MMR | ✅ Done | 2026-05-19 |
| 21 | **Agent Frameworks Deep Dive**: CrewAI, AutoGen, LangGraph side-by-side | ✅ Done | 2026-05-20 |
| 22 | **Cost Engineering**: Model routing, prompt caching, batching API | ✅ Done | 2026-05-21 |
| 23 | **Phase 3 Capstone**: AutoResearcher v1.0 — deployed, evaluated, secured | ✅ Done | 2026-05-22 |

---

## 🎓 Graduation — Phase 4: Specialization

The core curriculum is complete. You didn't pick a track before the next scheduled run, so we've defaulted to **Track 1 — Reliability & Safety** (highest-leverage given your L17/L18/L23 foundation). Want to switch? Tell me on any scheduled run and we'll pivot — no lesson is wasted, the foundations apply across all tracks.

### Phase 4 Track Menu

| Track | Focus | Why pick this |
|-------|-------|---------------|
| **1** *(active)* | **Reliability & Safety** — failure taxonomy, SLOs, golden suites, constitutional AI, jailbreak evals, Llama Guard, adversarial robustness | Builds directly on L17/L18/L23 |
| 2 | **Multi-Agent Coordination** — A2A protocol, blackboard architectures, debate systems, swarms | Deepens L6/L11/L21 |
| 3 | **Self-Hosted & Fine-Tuning** — vLLM serving, QLoRA on real data, DPO/ORPO, distillation, model merging | Deepens L12, shifts from API user to model owner |
| 4 | **Voice + Multimodal Agents** — Realtime API, ASR/TTS pipelines, image gen tools, document AI | Deepens L13 |
| 5 | **Agent-Ops & Infra** — Temporal/Inngest durable execution, GPU autoscaling, OpenTelemetry for LLMs | Deepens L8/L16 |

---

## Phase 4 — Track 1: Reliability & Safety — IN PROGRESS 🚀

| # | Topic | Status | Date |
|---|-------|--------|------|
| 24 | **Reliability Foundations** — failure-mode taxonomy, SLOs, reproducibility, `ReliabilityProfiler`, golden regression suite | ✅ Done | 2026-05-23 |
| 25 | **Constitutional AI & Self-Critique** — critique→revise loop, pairwise judge for adherence improvement | ✅ Done | 2026-05-24 |
| 26 | **Jailbreak Evals** — public attack catalogs, ASR/FRR trade-off harness | ✅ Done | 2026-05-25 |
| 27 | **Input/Output Moderation** — Llama Guard 3 + Claude classifier as I/O guards, MLCommons taxonomy, stacked vs single-layer defense, dual-cost/dual-safety scatter | ✅ Done | 2026-05-26 |
| 28 | **Adversarial Robustness & Semantic-Invariance Testing** — metamorphic harness, 7 perturbations, semantic-preservation gate, 3-axis scorecard (ASR · FRR · invariance), `RobustSecurityScorecard` | ✅ Done | 2026-05-27 |
| 29 | **Calibration & Refusal Quality** — Brier/ECE from scratch, reliability diagrams, `abstain` verdict, 3-way refusal-quality judge, `RefusalQualityScorecard`, `CalibrationSLO` CI gate, `CalibrationAwareAgent` mini-capstone | ✅ Done | 2026-05-28 |
| 30 | **Production Reliability Stack** — circuit breakers, model fallback, canary/A-B prompt deploys | ⏳ Next | — |
| 31 | **Track 1 Capstone** — Reliability Harness wired into AutoResearcher CI | ⏳ Pending | — |

---

## Learning Philosophy
- **Concept first, then code.** Every lesson explains the "why" before the "how."
- **Run the code.** Don't just read — execute, modify, experiment.
- **Incremental.** Each lesson builds directly on the previous one.
- **Language-agnostic.** We use Python (the AI ecosystem's native language), but the concepts apply everywhere.
- **Open-source goal.** Every lesson moves toward something publishable and demonstrable.

---

## Setup Requirements
- Python 3.10+ (or Google Colab — zero setup required)
- An Anthropic API key → https://console.anthropic.com
- All lessons are Colab-ready `.ipynb` notebooks

---

## Lesson Files
All notebooks saved in this folder (`/Learn AI/`):
- `Lesson_01_LLM_Fundamentals.ipynb`
- `Lesson_02_Prompt_Engineering.ipynb`
- `Lesson_03_Tool_Use_Function_Calling.ipynb`
- `Lesson_04_Building_Your_First_Agent.ipynb`
- `Lesson_05_Agent_Memory.ipynb`
- `Lesson_06_Multi_Agent_Systems.ipynb`
- `Lesson_07_RAG.ipynb`
- `Lesson_08_Productionizing_AI.ipynb`
- `Lesson_09_Capstone_AutoResearcher.ipynb`
- `Lesson_10_Structured_Outputs.ipynb`
- `Lesson_11_LangGraph_Stateful_Agent_Graphs.ipynb`
- `Lesson_12_Fine_Tuning_Fundamentals.ipynb`
- `Lesson_13_Multimodal_AI_Vision_Text.ipynb`
- `Lesson_14_MCP_Model_Context_Protocol.ipynb`
- `Lesson_15_Open_Source_Publishing.ipynb`
- `Lesson_16_Deployment_FastAPI_Docker.ipynb`
- `Lesson_17_Advanced_Evals_RAGAS_LLM_Judge.ipynb`
- `Lesson_18_AI_Security_Prompt_Injection_Guardrails_Red_Teaming.ipynb`
- `Lesson_19_Streaming_Agents_SSE_Realtime_UIs.ipynb`
- `Lesson_20_Vector_DBs_in_Production.ipynb`
- `Lesson_21_Agent_Frameworks_CrewAI_AutoGen_LangGraph.ipynb`
- `Lesson_22_Cost_Engineering.ipynb`
- `Lesson_23_Capstone_AutoResearcher_v1.ipynb`
- `Lesson_24_Reliability_Foundations.ipynb`
- `Lesson_25_Constitutional_AI_Self_Critique.ipynb`
- `Lesson_26_Jailbreak_Evals.ipynb`
- `Lesson_27_Input_Output_Moderation.ipynb`
- `Lesson_28_Adversarial_Robustness_Semantic_Invariance.ipynb`
- `Lesson_29_Calibration_Refusal_Quality.ipynb`
- `Lesson_30_Production_Reliability_Stack.ipynb`
- `Lesson_31_Track1_Capstone_Reliability_Harness.ipynb` ← Track 1 (Reliability & Safety) COMPLETE
- `Lesson_32_A2A_Protocol_Agent_To_Agent_Messaging.ipynb`
- `Lesson_33_Blackboard_Architectures_for_Collaborative_Agents.ipynb`
- `Lesson_34_Debate_Systems_with_Judge.ipynb`
- `Lesson_35_Parallel_Fan_out_and_Map_Reduce.ipynb`
- `Lesson_36_Track2_Capstone_Multi_Agent_Research_Swarm.ipynb` ← latest · Track 2 (Multi-Agent Coordination) COMPLETE

**Next:** Lesson 37 — Track 3 (Self-hosted & Fine-tuning) begins with vLLM + serving your own model. Reply "Track 4" (voice/multimodal) or "Track 5" (agent-ops/infra) before the next run to steer.

---

> **Note (2026-07-21):** this file stopped being maintained after Lesson 36. The
> live curriculum state now lives in the tutor's memory (`learning_progress.md`).
> Lessons 37–75 shipped as notebooks in this folder. Current position:
> **Phase 8 (Production Ops), Lesson 75 of ~76** — L76 is the Phase 8 capstone
> (consolidate and ship the `observability/` package wired into `agent-bench`).
