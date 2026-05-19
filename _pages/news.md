---
layout: archive
title: "News"
excerpt: "Recent research highlights, conference activities, project milestones, media, demonstrations, and publication updates."
permalink: /news/
author_profile: true
---

<p class="news-date">May 15, 2026</p>

## Distributed Edge Storage Systems in *Mathematics*

We are pleased to share a new open-access article in *Mathematics* on proactive high availability for microservice-based distributed edge storage. The paper studies a practical reliability problem for mobile edge computing: storage services must remain available for immersive and IoT workloads while facing both abrupt failures and slower software-aging effects.

<figure>
  <img src="/images/news/260515/distributed-edge-storage-cover.webp" alt="Scientific illustration of distributed edge storage with live migration and proactive rejuvenation" width="1200" height="675" loading="lazy" decoding="async">
  <figcaption>Scientific illustration: SRN-based availability analysis for live migration, rejuvenation, and proactive high-availability policies.</figcaption>
</figure>

### What the paper contributes

- Develops a **Stochastic Reward Net (SRN)** model for a multi-node edge storage architecture with hardware failures, software failures, software aging, high availability, live migration, and rejuvenation.
- Evaluates six policy scenarios and introduces **Capacity-Oriented Availability (COA)** as the expected number of usable microservices while the storage layer remains operational.
- Runs steady-state and sensitivity analyses over twelve timing parameters to identify which policy and timing choices most affect service availability.

### Why this matters

- The Crossref abstract verifies that policies including **live migration** achieve the highest, or effectively tied-highest, COA across broad failure and repair ranges.
- The paper highlights a subtle operational risk called **Proactive Crash (PC)**: uncoordinated rejuvenation can reduce availability when services are terminated before live migration finishes evacuating them.
- The results give concrete configuration guidance: let migration complete before rejuvenation, and tune rejuvenation intervals so they are neither too frequent nor too sparse.

**Publication record:** Published online on May 15, 2026 in *Mathematics*, Volume 14, Issue 10, Article 1704 ([DOI](https://doi.org/10.3390/math14101704), [MDPI article](https://www.mdpi.com/2227-7390/14/10/1704)).

---
<p class="news-date">February 22, 2026</p>

## VAE+DDPG for Autonomous Navigation in Low-Light Environments

We are pleased to share a new open-access article in *Advanced Intelligent Systems* that tackles a practical robotics bottleneck: indoor navigation when ambient light drops and depth sensing becomes unreliable. Instead of treating low-light degradation as only a control problem, the paper redesigns the representation itself so the policy learns from geometry-focused latent features rather than directly from brightness-sensitive observations.

<figure>
  <img src="/images/news/260222/vae-ddpg-cover.webp" alt="Scientific illustration of VAE+DDPG low-light autonomous navigation with latent depth perception" width="1200" height="675" loading="lazy" decoding="async">
  <figcaption>Scientific illustration: attention-enhanced latent perception and jointly tuned reinforcement learning for low-light indoor navigation.</figcaption>
</figure>

### What the paper contributes

- Introduces an attention-enhanced **VAE+** encoder that combines **Feature Pyramid Network (FPN)** structure and **CBAM** attention to learn illuminance-robust depth features.
- Couples that encoder with **Deep Deterministic Policy Gradient (DDPG)** and jointly tunes the perception module and control policy instead of freezing the encoder after pretraining.
- Evaluates the method in cluttered Gazebo navigation scenes and unseen-maze transfer tests; the public codebase shows a TurtleBot3-style setup with dual depth cameras and goal-conditioned state inputs.

### Why this matters

- Crossref metadata for the published abstract says the learned latent space shifts toward **geometric features rather than raw intensity values**, which is exactly the right bias when low-light sensing degrades.
- A public abstract summary indexed alongside the DOI reports roughly **88%** success at **30 Lx** and almost **94%** at **300 Lx**, while plain DDPG stabilizes near **70%** and unseen-maze transfer drops only about **3 points**.
- The published abstract also states that deployment processes depth frames at **10 Hz** on a single **RTX 4070**, suggesting the method is practical not only in simulation but also as an affordable indoor autonomy pipeline.

**Publication record:** Published online on February 22, 2026 in *Advanced Intelligent Systems* as open access, article e202500636 ([DOI](https://doi.org/10.1002/aisy.202500636), [Wiley article](https://advanced.onlinelibrary.wiley.com/doi/10.1002/aisy.202500636), [code repository](https://github.com/uiseoklee/VAEplusDDPG)).

---
<p class="news-date">December 31, 2025</p>

## Availability Modeling for Edge Systems under Correlated Failures

We are pleased to highlight a new publication in the *Journal of The Korea Society of Computer and Information* that focuses on a realism gap in edge dependability studies: failures in edge environments are often correlated rather than isolated. When power, network, or site-level disruptions strike multiple nodes at once, recovery policies that look effective under independent-failure assumptions can behave very differently in practice.

<figure>
  <img src="/images/news/251201/edge-availability-cover.webp" alt="Scientific illustration of edge availability modeling under correlated failures and adaptive recovery" width="1200" height="675" loading="lazy" decoding="async">
  <figcaption>Scientific illustration: correlated-failure modeling, COA-based evaluation, and adaptive recovery guidance.</figcaption>
</figure>

### What the paper contributes

- Extends an SRN-based edge availability model to explicitly represent correlated failures rather than only independent ones.
- Defines a **Capacity-Oriented Availability (COA)** metric that captures the overhead of High Availability (HA) and Live Migration (LM) policies.
- Uses discrete-event sensitivity analysis to compare recovery behavior across different failure intervals and correlated-failure scales.

### Why this matters

- The official KCI abstract reports that the combined **HA+LM** policy performs better when failure intervals are long.
- The same abstract reports a policy reversal once the number of correlated-failure nodes exceeds **5**, because LM node-search overhead slows recovery during larger incidents.
- This turns the paper into practical guidance for adaptive recovery design in edge platforms rather than a fixed-policy recommendation.

**Publication record:** Published on December 31, 2025 in *Journal of The Korea Society of Computer and Information*, 30(12), 25-35 ([DOI](https://doi.org/10.9708/jksci.2025.30.12.025), [KCI article](https://journal.kci.go.kr/jksci/archive/articleView?artiId=ART003280297)).

---
<p class="news-date">December 5, 2025</p>

## S-iNAS: Performance-Centric Scaling for Ceph-Based Industrial Storage

We are pleased to share the publication of **S-iNAS** in the *Journal of Network and Systems Management*. The paper addresses a systems problem that matters directly to Industry 4.0 and digital twin deployments: how to keep Ceph-based industrial network-attached storage responsive when data streams become bursty, highly concurrent, and operationally uneven.

<figure>
  <img src="/images/news/251205/sinas-cover.webp" alt="Scientific illustration of adaptive Ceph scaling for industrial network-attached storage" width="1200" height="675" loading="lazy" decoding="async">
  <figcaption>Scientific illustration: SRN-based analysis of time-based and event-based scaling for Ceph-backed industrial storage.</figcaption>
</figure>

### What the paper contributes

- Introduces an SRN-based modeling framework that captures concurrent read and write workflows, replication overhead, and dynamic scaling triggers for Ceph Object Storage Daemons (OSDs).
- Compares two scaling policies head-to-head: scheduled time-based expansion and event-based expansion driven by workload thresholds.
- Studies the effect of arrival rate, client concurrency, VM instantiation delay, and read/write composition on throughput and latency.

### Why this matters

- The Springer abstract shows that time-based scaling stays stable under moderate load but can react too slowly when demand spikes abruptly.
- Event-based scaling adapts faster and helps reduce latency, though it may cause more frequent reconfigurations.
- The paper turns these trade-offs into actionable guidance for tuning storage services in industrial workflows and digital twin ecosystems.

**Publication record:** Published online on December 5, 2025 in *Journal of Network and Systems Management*, Volume 34, Article 34 ([DOI](https://doi.org/10.1007/s10922-025-10005-6), [Springer article](https://link.springer.com/article/10.1007/s10922-025-10005-6)).

---
<p class="news-date">November 1, 2025</p>

## Energy-Aware Kubernetes Autoscaling for Microservices

Our recent article in the *Journal of Network and Computer Applications* studies Kubernetes autoscaling from a more useful engineering perspective: not only whether a deployment stays responsive, but whether it does so without wasting electrical power. This is especially important for cloud and edge platforms that must balance service quality, infrastructure cost, and sustainability at the same time.

<figure>
  <img src="/images/news/251101/kubernetes-gspn-cover.webp" alt="Scientific illustration of energy-aware Kubernetes autoscaling for microservices" width="1200" height="675" loading="lazy" decoding="async">
  <figcaption>Scientific illustration: balancing response time and energy use with GSPN-based analysis.</figcaption>
</figure>

### What the paper contributes

- Builds a Generalized Stochastic Petri Net (GSPN) model for Kubernetes-orchestrated microservices that jointly represents Horizontal Pod Autoscaling (HPA), Cluster Autoscaling (CA), application behavior, and infrastructure capacity.
- Introduces the **Energy-Response Time Weighted Product (ERWP)** metric to evaluate performance and energy efficiency together rather than in isolation.
- Uses sensitivity analysis and realistic case studies to reveal which autoscaling parameters most strongly influence energy use, throughput, and response time.

### Why this matters

- The publisher abstract reports that higher autoscaling thresholds under low workloads can reduce electrical consumption by about **32%** without materially hurting performance.
- Under high arrival-rate conditions, the same choice can still cut consumption by about **37%**, but at the cost of a **175%** increase in response time.
- The result is a concrete workload-aware guide for tuning Kubernetes deployments instead of relying on heuristic trial and error.

**Publication record:** Published in November 2025 in *Journal of Network and Computer Applications*, Volume 243, Article 104287 ([DOI](https://doi.org/10.1016/j.jnca.2025.104287), [ScienceDirect article](https://www.sciencedirect.com/science/article/abs/pii/S1084804525001845)).

---
<p class="news-date">October 14, 2025</p>

## Maintenance-Centered Dependability for Urban Surveillance

This *Computing* article reframes smart-city surveillance as a maintenance problem as much as a sensing or analytics problem. Urban surveillance platforms may include cameras, edge resources, communication links, and repair workflows, and their dependability depends heavily on how failures are anticipated, prioritized, and handled over time.

<figure>
  <img src="/images/news/251014/urban-surveillance-maintenance-cover.webp" alt="Scientific illustration of maintenance-centered dependability for smart-city urban surveillance" width="1200" height="675" loading="lazy" decoding="async">
  <figcaption>Scientific illustration: stochastic Petri net evaluation of reactive, autonomous, and preventive maintenance strategies.</figcaption>
</figure>

### What the paper contributes

- Uses **Stochastic Petri Net (SPN)** models to compare reactive, autonomous, and preventive maintenance strategies in an edge-enabled surveillance environment.
- Integrates availability and reliability analysis into a unified maintenance-evaluation framework.
- Applies sensitivity analysis to identify which components matter most for system availability and therefore deserve the greatest maintenance focus.

### Why this matters

- The Springer abstract emphasizes that maintenance strategy has a direct effect on the dependability and efficiency of urban surveillance systems.
- It also highlights sensitivity analysis as the key mechanism for identifying high-impact components instead of spreading maintenance effort evenly.
- For smart-city operators, that means maintenance planning can be made more targeted, more resilient, and more cost-effective.

**Publication record:** Published on October 14, 2025 in *Computing*, Volume 107, Article 208 ([DOI](https://doi.org/10.1007/s00607-025-01561-5), [Springer article](https://link.springer.com/article/10.1007/s00607-025-01561-5)).

---
<p class="news-date">September 1, 2025</p>

## RT-VLM: Re-Thinking Vision-Language Robustness for Real-World Recognition

We are also excited to share **RT-VLM**, a new arXiv preprint focused on one of the most persistent problems in real-world perception: domain shift. When image statistics, viewing angles, occlusion patterns, or neighboring object classes change, recognition performance often drops sharply. RT-VLM tackles that problem by combining structured multimodal evidence with an explicit self-correction loop.

<figure>
  <img src="/images/news/250901/rt-vlm-cover.webp" alt="Scientific illustration of robust vision-language recognition using four structured clues" width="1200" height="675" loading="lazy" decoding="async">
  <figcaption>Scientific illustration: four-clue supervision and a two-stage re-thinking pipeline for more robust visual understanding.</figcaption>
</figure>

### What the paper contributes

- Introduces a synthetic dataset generation pipeline annotated with four structured clues: bounding boxes, class names, object-level captions, and a scene-level context caption.
- Uses parameter-efficient supervised tuning of **Llama 3.2 11B Vision Instruct** on that multimodal supervision.
- Applies a two-stage inference process in which the model first generates its own clues and then re-examines them as evidence to iteratively correct the final recognition result.

### Why this matters

- The arXiv abstract frames RT-VLM around four important sources of robustness failure: low-level image variation, pose and viewpoint change, partial occlusion, and confusion among nearby classes.
- The reported gains across robustness benchmarks suggest that structured evidence plus self-critique is a promising direction for more reliable real-world visual perception.
- This is particularly relevant for embodied AI, robotics, and safety-critical recognition settings where robustness matters more than single-dataset accuracy.

**Publication record:** Posted on September 1, 2025 as an arXiv preprint ([arXiv abstract](https://arxiv.org/abs/2509.05333), [DOI](https://doi.org/10.48550/arXiv.2509.05333)).

---
<p class="news-date">August 27, 2025</p>

## Aging Dependability for AAM Vehicle Digital Twins

This MetaCom 2025 short paper expands digital-twin evaluation beyond realism and integration into the question of long-running dependability. For advanced air mobility (AAM) platforms, a cloud-edge-in-the-loop simulation stack is only useful if it can stay dependable while synchronizing models, services, and data flows over time.

<figure>
  <img src="/images/news/250827/metacom-cloud-edge-cover.webp" alt="Scientific illustration of aging dependability in a cloud-edge AAM digital twin platform" width="1200" height="675" loading="lazy" decoding="async">
  <figcaption>Scientific illustration: aging-aware dependability analysis for a cloud-edge-in-the-loop simulation platform.</figcaption>
</figure>

### What the paper contributes

- Studies a **cloud-edge-in-the-loop** platform for an AAM vehicle digital twin rather than an isolated simulator component.
- Frames the core research problem around **aging dependability**, which is especially important for persistent, always-on metaverse and digital-twin systems.
- Positions dependability evaluation as part of digital-twin architecture design for aviation-oriented experimentation.

### Why this matters

- The official MetaCom record verifies the work as a 2025 short paper on metaverse cloud-edge computing for vehicle digital twins.
- This perspective is important because operational twin platforms degrade under sustained service time, not only under single-shot test conditions.
- It strengthens the bridge between digital-twin fidelity and trustworthy long-duration experimentation for AAM.

**Publication record:** Published on August 27, 2025 in the *Proceedings of the 2025 International Conference on Metaverse Computing, Networking and Applications (MetaCom)* ([DOI](https://doi.org/10.1109/metacom65502.2025.00020), [accepted papers](https://ieee-metacom.org/accept-papers.html)).

---
<p class="news-date">August 27, 2025</p>

## High-Availability Quantification for Metaverse Storage Backbones

Persistent metaverse environments depend on storage systems that keep state available across distributed services and users. This MetaCom 2025 paper brings formal availability modeling directly into that layer, asking how resilience in distributed storage should be quantified rather than assumed.

<figure>
  <img src="/images/news/250827/metacom-storage-cover.webp" alt="Scientific illustration of high-availability quantification for metaverse distributed storage" width="1200" height="675" loading="lazy" decoding="async">
  <figcaption>Scientific illustration: stochastic reward net analysis for resilient distributed storage services.</figcaption>
</figure>

### What the paper contributes

- Uses **Stochastic Reward Nets** to quantify high availability in metaverse-oriented distributed storage.
- Places storage dependability inside the architectural core of immersive systems instead of treating it as a backend afterthought.
- Extends the broader dependability modeling line into storage infrastructures designed for persistent virtual environments.

### Why this matters

- The official MetaCom program lists the paper in **Conference Session 1: Metaverse Computing, Architectures, and Applications**.
- That placement reflects the architectural significance of storage availability for immersive services, digital assets, and synchronized state.
- The result is a stronger basis for reasoning about resilience in metaverse infrastructures before deployment.

**Publication record:** Published on August 27, 2025 in the *Proceedings of the 2025 International Conference on Metaverse Computing, Networking and Applications (MetaCom)* ([DOI](https://doi.org/10.1109/metacom65502.2025.00039), [MetaCom program](https://ieee-metacom.org/program.html)).

---
<p class="news-date">August 27, 2025</p>

## Sim-to-Real Reinforcement Learning with ROS2 and Unreal Engine

This MetaCom 2025 workshop paper focuses on one of robotics' most practical bottlenecks: how to make virtual training transfer into physical behavior. By combining ROS2, Unreal Engine, and reinforcement learning for TurtleBot experimentation, the work treats metaverse-ready simulation as a deployment bridge rather than only a visualization environment.

<figure>
  <img src="/images/news/250827/metacom-sim2real-cover.webp" alt="Scientific illustration of sim-to-real reinforcement learning for TurtleBot robotics" width="1200" height="675" loading="lazy" decoding="async">
  <figcaption>Scientific illustration: ROS2, Unreal Engine, and reinforcement learning combined for metaverse-ready robotics.</figcaption>
</figure>

### What the paper contributes

- Couples a **ROS2 + Unreal Engine** stack with reinforcement learning for TurtleBot-based sim-to-real experimentation.
- Treats the metaverse as a controllable training and evaluation environment for robot behavior transfer.
- Connects virtual-world experimentation with physical navigation deployment in a concrete robotics workflow.

### Why this matters

- The official MetaCom program lists the paper in **Workshop Session 1**, confirming its role in testbed-oriented metaverse research.
- Sim-to-real transfer remains a central barrier in robotic learning systems, especially when moving from controlled simulation to messy physical environments.
- This paper makes the metaverse framing operational by tying it directly to deployable robot-control practice.

**Publication record:** Published on August 27, 2025 in the *Proceedings of the 2025 International Conference on Metaverse Computing, Networking and Applications (MetaCom)* ([DOI](https://doi.org/10.1109/metacom65502.2025.00008), [MetaCom program](https://ieee-metacom.org/program.html)).

---
<p class="news-date">August 27, 2025</p>

## LLM-Based Malicious Code Detection for Metaverse Security

As metaverse platforms become more programmable, security questions move closer to code generation, code review, and automated filtering pipelines. This MetaCom 2025 paper addresses that direction by studying malicious code detection with large language models and by treating token optimization as part of the detection design space.

<figure>
  <img src="/images/news/250827/metacom-malicious-code-cover.webp" alt="Scientific illustration of LLM-based malicious code detection through token optimization" width="1200" height="675" loading="lazy" decoding="async">
  <figcaption>Scientific illustration: LLM-based malicious code detection with token-level optimization.</figcaption>
</figure>

### What the paper contributes

- Frames malicious code detection as an **LLM-based security analysis** task.
- Uses **token optimization** as the main lever for improving code-oriented model behavior.
- Places code-security tooling squarely inside metaverse security research rather than outside it.

### Why this matters

- The official MetaCom program places the paper in **Conference Session 4: Security, Privacy, and Trust**.
- That positioning shows the work is not only about language models, but about securing programmable metaverse ecosystems.
- The paper therefore points toward a practical developer-security workflow for safer code handling in immersive platforms.

**Publication record:** Published on August 27, 2025 in the *Proceedings of the 2025 International Conference on Metaverse Computing, Networking and Applications (MetaCom)* ([DOI](https://doi.org/10.1109/metacom65502.2025.00057), [MetaCom program](https://ieee-metacom.org/program.html)).

---
<p class="news-date">August 27, 2025</p>

## Iterative Prompt Optimization for Diverse Metaverse Tasks

This workshop paper treats prompting not as a one-off instruction-writing trick, but as an adaptive optimization problem. In metaverse applications where tasks can vary widely across content generation, interaction, assistance, and moderation, that shift matters because prompt quality becomes part of system performance.

<figure>
  <img src="/images/news/250827/metacom-adaptive-prompting-cover.webp" alt="Scientific illustration of iterative prompt optimization for diverse metaverse tasks" width="1200" height="675" loading="lazy" decoding="async">
  <figcaption>Scientific illustration: iterative prompt optimization for diverse LLM-driven metaverse tasks.</figcaption>
</figure>

### What the paper contributes

- Proposes an **iterative prompt optimization** framework for improving LLM performance across diverse tasks.
- Reframes prompts as adaptive artifacts that can be refined through repeated feedback rather than fixed text strings.
- Extends LLM performance engineering into metaverse application workflows.

### Why this matters

- The MetaCom program confirms the work as part of **Workshop Session 1**, where experimental and framework-oriented systems were presented.
- In practice, metaverse tasks are heterogeneous, so prompt behavior often needs to be tuned across contexts instead of reused unchanged.
- This makes the paper especially relevant for robust, reusable LLM tooling in interactive virtual environments.

**Publication record:** Published on August 27, 2025 in the *Proceedings of the 2025 International Conference on Metaverse Computing, Networking and Applications (MetaCom)* ([DOI](https://doi.org/10.1109/metacom65502.2025.00009), [MetaCom program](https://ieee-metacom.org/program.html)).

---
<p class="news-date">August 27, 2025</p>

## PGELU for Stable and Scalable Metaverse Perception

This MetaCom 2025 paper introduces **PGELU**, a parametric GELU variant designed for recognition workloads that span both emotional signals and 3D object understanding. That combination is notable because metaverse perception often mixes human-centered and scene-centered recognition tasks in the same pipeline.

<figure>
  <img src="/images/news/250827/metacom-pgelu-cover.webp" alt="Scientific illustration of PGELU for stable emotion and 3D object recognition" width="1200" height="675" loading="lazy" decoding="async">
  <figcaption>Scientific illustration: activation-level design for stable emotion and 3D object recognition in metaverse pipelines.</figcaption>
</figure>

### What the paper contributes

- Proposes a **parametric GELU** formulation for metaverse-driven deep learning.
- Targets the stability and scalability of recognition pipelines for **emotion analysis** and **3D object recognition**.
- Highlights activation design itself as a useful lever in metaverse perception systems.

### Why this matters

- The official MetaCom program places the paper in **Conference Session 2: AI for the Metaverse**.
- That context underscores the paper's relevance to practical AI architectures in immersive environments.
- The work is therefore meaningful not only as a new activation variant, but as a systems-oriented attempt to stabilize mixed perception workloads.

**Publication record:** Published on August 27, 2025 in the *Proceedings of the 2025 International Conference on Metaverse Computing, Networking and Applications (MetaCom)* ([DOI](https://doi.org/10.1109/metacom65502.2025.00044), [MetaCom program](https://ieee-metacom.org/program.html)).

---
<p class="news-date">August 1, 2025</p>

## Queueing-Theoretic Performance Design for Cloud-Edge-Sensor Data Harvesting

Published in *ICT Express*, this paper studies how cloud-edge-sensor infrastructures can be sized and tuned for data harvesting systems, with agricultural monitoring as a motivating application. Rather than treating sensing pipelines as black boxes, the work uses queueing theory to expose where latency, overload, and under-provisioning emerge before costly infrastructure changes are made.

<figure>
  <img src="/images/news/250801/data-harvesting-cover.webp" alt="Scientific illustration of cloud-edge-sensor data harvesting and queueing-theoretic design" width="1200" height="675" loading="lazy" decoding="async">
  <figcaption>Scientific illustration: queueing-theoretic design guidance for scalable data harvesting systems.</figcaption>
</figure>

### What the paper contributes

- Models a Cloud-Edge-sensors architecture using **M/M/c/K** queueing theory to evaluate data-handling performance in sensing systems.
- Analyzes how configuration choices affect efficiency, scalability, and real-time data handling.
- Provides a predictive framework for identifying bottlenecks and adjusting parameters without immediately resorting to expensive structural overbuild.

### Why this matters

- According to the ScienceDirect abstract, the model achieved **more than 90% utilization** in both the cloud and edge layers while still serving as a useful planning instrument.
- The paper is positioned around precision agriculture, where real-time sensing quality directly affects downstream decisions.
- At the same time, the abstract notes that the framework is versatile enough to inform broader IoT scenarios that need efficient real-time analysis and resource management.

**Publication record:** Published in August 2025 in *ICT Express*, Volume 11, Issue 4, Pages 597-602 ([DOI](https://doi.org/10.1016/j.icte.2025.04.017), [ScienceDirect article](https://www.sciencedirect.com/science/article/pii/S2405959525000621)).

---
<p class="news-date">May 19, 2025</p>

## Smart Building Surveillance with Edge-Fog Capacity Planning

Another recent publication appeared in the **SBRC 2025** proceedings and focuses on intelligent camera surveillance in smart buildings. The core challenge is straightforward but operationally demanding: real-time video analytics requires significant compute resources, and poorly planned edge-fog pipelines can quickly become overloaded, slow, or wasteful.

<figure>
  <img src="/images/news/250519/smart-surveillance-cover.webp" alt="Scientific illustration of smart building surveillance with edge-fog capacity planning" width="1200" height="675" loading="lazy" decoding="async">
  <figcaption>Scientific illustration: SPN-based capacity planning for real-time camera analytics over edge and fog layers.</figcaption>
</figure>

### What the paper contributes

- Uses **Stochastic Petri Net (SPN)** models to evaluate mean response time, throughput, resource utilization, and drop probability in intelligent surveillance infrastructures.
- Shows how edge and fog resource allocation decisions influence service quality under different message arrival rates.
- Offers planning guidance for scaling video analytics infrastructure in a controlled and explainable way.

### Why this matters

- Crossref metadata for the paper reports that increasing the Fog layer to **10 processing cores** reduces drop probability to around **35%** at an arrival rate of **47.37 msg/ms**.
- The same abstract reports that mean response time stays below **10 ms** at moderate arrival rates up to about **29 msg/ms**.
- The official SBRC 2025 proceedings page notes that **74 full papers** were accepted from **203 submissions**, corresponding to a **36.5% acceptance rate**, underlining the competitiveness of the venue.

**Publication record:** Published on May 19, 2025 in the *Anais do XLIII Simposio Brasileiro de Redes de Computadores e Sistemas Distribuidos (SBRC 2025)* ([DOI](https://doi.org/10.5753/sbrc.2025.5744), [proceedings article](https://sol.sbc.org.br/index.php/sbrc/article/view/35119), [SBRC 2025 proceedings](https://sol.sbc.org.br/index.php/sbrc/index)).

---
<p class="news-date">April 2, 2025</p>

## Vehicle Digital Twin Integration under Steady Wind Conditions

This proceedings paper from the Korean Society for Aeronautical and Space Sciences focuses on a vehicle digital twin as an integrated engineering system rather than a visualization layer. The study reports preliminary flight-simulation behavior for an eVTOL platform under steady-wind conditions, linking digital-twin design to actual flight-dynamics response.

<figure>
  <img src="/images/news/250402/vehicle-digital-twin-cover.webp" alt="Scientific illustration of vehicle digital twin flight simulation under steady wind conditions" width="1200" height="675" loading="lazy" decoding="async">
  <figcaption>Scientific illustration: integrated flight simulation for the KADA KP2-c under steady-wind conditions.</figcaption>
</figure>

### What the paper contributes

- Integrates the subsystems of a **vehicle digital twin** and reports preliminary flight-simulation results.
- Studies the **KADA KP2-c eVTOL** in CTOL mode under light (**10 knots**) and moderate (**20 knots**) steady wind.
- Tracks how yaw-rate response changes under wind loading as part of the twin's dynamic behavior.

### Why this matters

- The official KSAS proceedings state that yaw-rate response varies significantly between **2.5** and **1.5 rad/s** under the tested wind conditions.
- The same proceedings record positions the twin around high-fidelity dynamics and control response rather than immersive visualization alone.
- This makes the study a solid engineering step toward validating flight-oriented twins with future flight-test data.

**Publication record:** Published on April 2, 2025 in the *Proceedings of the Korean Society for Aeronautical & Space Sciences Spring Conference 2025*, Pages 381-382 ([KSAS proceedings](https://ksas.or.kr/proceedings/2025a/data/%EC%B2%A8%EB%B6%804.%202025%EB%85%84%EB%8F%84%EC%B6%98%EA%B3%84%ED%95%99%EC%88%A0%EB%8C%80%ED%9A%8C_%EB%85%BC%EB%AC%B8%EC%A7%91_All.pdf), [DBpia record](https://www.dbpia.co.kr/pdf/pdfView.do?nodeId=NODE12340734)).

---
<p class="news-date">March 13, 2025</p>

## Correction Notice for the Container Migration Study

This publication record marks the formal correction linked to the container migration article published earlier in 2025. While shorter than a research paper, it still matters because dependable scholarship also depends on maintaining an accurate and transparent publication trail.

<figure>
  <img src="/images/news/250313/container-migration-correction-cover.webp" alt="Scientific illustration of a correction notice tied to the container migration performance study" width="1200" height="675" loading="lazy" decoding="async">
  <figcaption>Scientific illustration: correction notice tied to the container migration performance study.</figcaption>
</figure>

### What the paper contributes

- Establishes the official correction entry connected to the original container migration article.
- Keeps the corrected version and the original publication record explicitly linked.
- Preserves downstream citation clarity and metadata consistency.

### Why this matters

- The Springer correction record is part of the scholarly history of the article and should remain visible as such.
- Accurate change tracking is especially important for technical papers that may be reused in later comparative or modeling studies.
- This entry therefore supports the integrity of the broader research line, even though it is not a new experimental study by itself.

**Publication record:** Published on March 13, 2025 in *Computing*, Volume 107, Article 93 ([DOI](https://doi.org/10.1007/s00607-025-01447-6), [original article](https://doi.org/10.1007/s00607-025-01423-0)).

---
<p class="news-date">February 5, 2025</p>

## Comparative Performance Modeling for Container Migration

Container migration is one of the key mechanisms that allows cloud and edge services to remain available while workloads move, fail over, or rebalance. This *Computing* article studies that problem systematically using stochastic Petri net models instead of relying only on ad hoc operational trial and error.

<figure>
  <img src="/images/news/250205/container-migration-cover.webp" alt="Scientific illustration of comparative performance modeling for container migration strategies" width="1200" height="675" loading="lazy" decoding="async">
  <figcaption>Scientific illustration: stochastic comparison of Cold, PreCopy, PostCopy, and Hybrid strategies.</figcaption>
</figure>

### What the paper contributes

- Proposes **two SPN models**, one with an absorbing state and one without, to evaluate container migration performance.
- Compares **Cold**, **PreCopy**, **PostCopy**, and **Hybrid** migration strategies under realistic demand and capacity assumptions.
- Analyzes metrics including total migration time, migration rate, utilization, and discard probability, with additional sensitivity analysis for the Hybrid policy.

### Why this matters

- The Springer abstract reports that the **Cold** strategy achieves lower total migration time under higher migration-arrival pressure.
- The same abstract reports that **PostCopy** produces the lowest discard probability in high-demand scenarios.
- The paper therefore offers operators a structured way to choose migration policy based on workload conditions rather than intuition alone.

**Publication record:** Published on February 5, 2025 in *Computing*, Volume 107, Article 64 ([DOI](https://doi.org/10.1007/s00607-025-01423-0), [Springer article](https://link.springer.com/article/10.1007/s00607-025-01423-0)).

---
<p class="news-date">February 1, 2025</p>

## Transactional Dynamics in Hyperledger Fabric

We are pleased to highlight a new *ICT Express* publication on permissioned blockchain performance. The paper models transaction processing in **Hyperledger Fabric** using Stochastic Petri Nets, with the goal of helping administrators understand how configuration choices affect response time, throughput, and resource efficiency before deployment decisions become expensive.

<figure>
  <img src="/images/news/250205/hyperledger-cover.webp" alt="Scientific illustration of permissioned blockchain transactional dynamics and SPN performance modeling" width="1200" height="675" loading="lazy" decoding="async">
  <figcaption>Scientific illustration: SPN-based analysis of transactional flow, response time, and throughput.</figcaption>
</figure>

### What the paper contributes

- Develops an SPN-based transaction-flow model for permissioned Hyperledger Fabric environments.
- Uses sensitivity analysis to identify the configuration factors that most strongly affect mean response time and throughput.
- Validates the model against system behavior and provides a pre-deployment tool for more disciplined performance planning.

### Why this matters

- The ScienceDirect abstract reports a **95% confidence interval** for response-time analysis using the proposed model.
- Case studies show that block size can change throughput and response time by as much as **200%**, making configuration discipline essential.
- This turns the paper into a practical operations guide for enterprise blockchain administrators rather than a purely theoretical analysis.

**Publication record:** Published in February 2025 in *ICT Express*, Volume 11, Issue 1, Pages 87-92 ([DOI](https://doi.org/10.1016/j.icte.2024.10.009), [ScienceDirect article](https://www.sciencedirect.com/science/article/pii/S2405959524001383)).

---
<p class="news-date">February 1, 2025</p>

## Multi-Region IoT Disaster Detection with Stochastic Modeling

This *ICT Express* publication studies disaster detection as a geographically distributed systems problem rather than a single-site sensing setup. By combining LoRaWAN-oriented communication assumptions with cloud and fog resources, the paper examines how multi-region monitoring can be modeled before infrastructure is deployed at scale.

<figure>
  <img src="/images/news/250201/disaster-detection-cover.webp" alt="Scientific illustration of multi-region IoT disaster detection with cloud-fog monitoring" width="1200" height="675" loading="lazy" decoding="async">
  <figcaption>Scientific illustration: LoRaWAN-aware stochastic models for cloud-fog monitoring across multiple regions.</figcaption>
</figure>

### What the paper contributes

- Presents stochastic models for IoT disaster detection across **multiple geographic areas** using LoRaWAN, fog, and cloud resources.
- Uses **Stochastic Petri Nets** to analyze key performance indicators such as average response time and utilization.
- Positions the models as a planning tool for cost-efficient server and processing-capacity design.

### Why this matters

- The ScienceDirect highlights report that additional processing cores reduce **mean response time** and improve throughput.
- The abstract also frames the work around financial and technical barriers to building cost-effective automated systems in high-risk and secluded areas.
- This makes the paper directly relevant to resilient disaster-monitoring infrastructure, especially when coverage must extend beyond a single location.

**Publication record:** Published in February 2025 in *ICT Express*, Volume 11, Issue 1, Pages 34-40 ([DOI](https://doi.org/10.1016/j.icte.2024.09.005), [ScienceDirect article](https://www.sciencedirect.com/science/article/pii/S2405959524001085)).

---
<p class="news-date">January 21, 2025</p>

## mhmcTD3: Multi-Head DRL with Memory for End-to-End Navigation

This TechRxiv preprint presents **mhmcTD3**, a multi-head actor-critic reinforcement learning architecture for autonomous navigation in dynamic and cluttered environments. The work is especially compelling because it aims to preserve rich LiDAR information, temporal context, and real-world transferability at the same time instead of optimizing only one of those dimensions.

<figure>
  <img src="/images/news/250121/mhmctd3-cover.webp" alt="Scientific illustration of mhmcTD3 multi-head memory contextualized reinforcement learning for autonomous navigation" width="1200" height="675" loading="lazy" decoding="async">
  <figcaption>Scientific illustration: multi-head LiDAR fusion, memory contextualisation, and sim-to-real autonomous navigation.</figcaption>
</figure>

### What the paper contributes

- Introduces the **Multi-Head Memory Contextualising TD3 (mhmcTD3)** architecture with specialized heads for LiDAR fusion, LiDAR features, robot states, and LiDAR memory.
- Combines tailored LiDAR preprocessing, CNN-based feature extraction, an LSTM-based memory head, and the use of **SiLU** and **CoRE** for more stable learning.
- Evaluates the framework in **ROS2/Gazebo** simulation and on a **Turtlebot3 waffle pi** platform across multiple LiDAR resolutions.

### Why this matters

- The official TechRxiv PDF reports strong performance in dense and fast-changing environments, including better handling of small dynamic obstacles.
- The same preprint emphasizes that ablation studies confirm the importance of each head, showing that the architecture is not just larger, but meaningfully modular.
- This makes mhmcTD3 a strong sim-to-real navigation contribution for robotics settings where map-free adaptability matters.

**Publication record:** Posted on January 21, 2025 on *TechRxiv* ([DOI](https://doi.org/10.36227/techrxiv.173747402.29145488/v1)).

---
<p class="news-date">December 21, 2024</p>

## mhmcTD3: A Multi-Head DRL Architecture for Autonomous Navigation

This early News release introduced **mhmcTD3** as a multi-head, memory-enhanced deep reinforcement learning architecture for autonomous navigation. The work brings richer LiDAR representation, temporal context, and actor-critic learning into one architecture for robots that must react smoothly in dynamic environments.

<figure>
  <img src="/images/news/250121/mhmctd3-cover.webp" alt="Scientific illustration of mhmcTD3 multi-head memory contextualized reinforcement learning for autonomous navigation" width="1200" height="675" loading="lazy" decoding="async">
  <figcaption>Scientific illustration: LiDAR fusion, memory contextualisation, and multi-head actor-critic navigation.</figcaption>
</figure>

### What the paper contributes

- Presents a **multi-head actor-critic** design that separates LiDAR fusion, LiDAR feature extraction, robot-state reasoning, and temporal memory.
- Combines tailored LiDAR preprocessing with CNN and LSTM modules, making the policy more sensitive to dynamic obstacles and recent motion context.
- Validates the approach across ROS2/Gazebo simulation and Turtlebot3 experiments, giving the architecture a stronger sim-to-real footing.

### Why this matters

- Autonomous robots in cluttered environments fail when perception, memory, and control are treated too narrowly; mhmcTD3 makes those parts collaborate explicitly.
- The architecture is especially relevant for map-free navigation where small moving obstacles, sensor resolution, and fast local decisions all interact.
- The work helps connect architecture design, learning stability, and real-world transfer into one coherent autonomous-navigation contribution.

<div class="figure-grid figure-grid--two">
  <figure>
    <img src="/images/news/241221/mhmcTD3_architectutre.jpeg" alt="mhmcTD3 architecture for autonomous navigation" width="500">
    <figcaption>mhmcTD3 architecture for autonomous navigation.</figcaption>
  </figure>
  <figure>
    <img src="/images/news/241221/multi_head_actor_critic_networks.jpeg" alt="multi-head actor-critic network architectures" width="500">
    <figcaption>Multi-head actor-critic network architectures.</figcaption>
  </figure>
</div>

**Publication record:** Posted on January 21, 2025 on *TechRxiv* as *Multi-head Fusion-based Actor-Critic Deep Reinforcement Learning with Memory Contextualisation for End-to-End Autonomous Navigation* ([DOI](https://doi.org/10.36227/techrxiv.173747402.29145488/v1)).

---
<p class="news-date">December 12, 2024</p>

## Edge-Fog-Cloud Industrial Automation Performance Evaluation

This *Journal of Network and Systems Management* article studies industrial automation as a tiered cyber-physical system rather than a single compute placement problem. The work compares edge, fog, and cloud architectures so that latency, throughput, and resource behavior can be evaluated before a factory workflow is deployed at scale.

<figure>
  <img src="/images/news/241212/industrial-automation-edge-fog-cloud-cover.webp" alt="Scientific illustration of edge-fog-cloud industrial automation performance evaluation" width="1200" height="675" loading="lazy" decoding="async">
  <figcaption>Scientific illustration: industrial sensors, edge gateways, fog nodes, and cloud resources connected through model-driven performance flows.</figcaption>
</figure>

### What the paper contributes

- Frames industrial IoT automation as a layered edge-fog-cloud design problem with measurable performance consequences.
- Uses model-driven evaluation to compare how architecture choices affect service behavior in automation pipelines.
- Gives system designers a clearer basis for placing computation close to machines, near local fog resources, or in the cloud.

### Why this matters

- Industrial automation workloads are sensitive to both timing and reliability, so placement decisions cannot be treated as only a cost question.
- The paper makes edge/fog/cloud trade-offs visible in a way that supports capacity planning for Industry 4.0 deployments.
- It also extends the website's News coverage for late-2024 IoT and CPS publications.

**Publication record:** Published online on December 12, 2024 in *Journal of Network and Systems Management*, Volume 33, Article 15 ([DOI](https://doi.org/10.1007/s10922-024-09893-x), [Springer article](https://link.springer.com/article/10.1007/s10922-024-09893-x)).

---
<p class="news-date">December 8, 2024</p>

## Resilient and Efficient Microservices at GLOBECOM 2024

This IEEE GLOBECOM 2024 paper focuses on a hard operational balance: microservice platforms should recover quickly, but the recovery strategy must not waste energy or over-provision the infrastructure. The study uses stochastic modeling to connect recovery time and energy consumption within a single evaluation lens.

<figure>
  <img src="/images/news/241208/resilient-microservices-energy-recovery-cover.webp" alt="Scientific illustration of resilient microservices with energy and recovery-time modeling" width="1200" height="675" loading="lazy" decoding="async">
  <figcaption>Scientific illustration: microservice recovery paths, energy-aware operation, and stochastic infrastructure modeling.</figcaption>
</figure>

### What the paper contributes

- Quantifies energy consumption and recovery-time behavior in resilient microservice architectures.
- Uses stochastic models to move beyond informal resilience claims and compare recovery choices quantitatively.
- Connects service-continuity goals with efficiency goals, which are often tuned separately in cloud systems.

### Why this matters

- Cloud resilience mechanisms can become expensive if recovery policies keep too many resources active for too long.
- Energy-aware modeling helps operators reason about sustainability without weakening recovery objectives.
- The work fills a late-2024 gap between the News page's Kubernetes and disaster-survivability publication threads.

**Publication record:** Published on December 8, 2024 in *GLOBECOM 2024 - 2024 IEEE Global Communications Conference* ([DOI](https://doi.org/10.1109/GLOBECOM52923.2024.10901098), [IEEE Xplore record](https://ieeexplore.ieee.org/document/10901098)).

---
<p class="news-date">November 13, 2024</p>

## Multi-Fidelity Data Fusion for Real-Time Aerodynamic Modeling

This KSAS Fall Conference paper addresses a key aerospace modeling problem: flight data arrive from sources with different fidelity, sampling conditions, and uncertainty. A real-time aerodynamic model has to fuse those signals into a usable representation quickly enough to support analysis, validation, and control-oriented workflows.

<figure>
  <img src="/images/news/241113/aerodynamic-data-fusion-cover.webp" alt="Scientific illustration of multi-fidelity aerodynamic data fusion from flight data" width="1200" height="675" loading="lazy" decoding="async">
  <figcaption>Scientific illustration: flight-data streams, multi-fidelity model layers, and aerodynamic surfaces fused for real-time modeling.</figcaption>
</figure>

### What the paper contributes

- Presents a multi-fidelity data-fusion method for real-time aerodynamic modeling from flight data.
- Positions aerodynamic model generation as a data-integration problem rather than a single-source fitting task.
- Supports the broader aerospace systems line on flight dynamics, validation, and digital-model generation.

### Why this matters

- Real-time aerodynamic models are useful only when they can reconcile measurement quality, model fidelity, and operational speed.
- Multi-fidelity fusion helps bridge the gap between simulation, low-fidelity estimates, and flight-test evidence.
- The post adds the missing November 2024 aerospace publication milestone to the News chronology.

**Publication record:** Presented on November 13, 2024 in the *Proceedings of the Korean Society for Aeronautical & Space Sciences Fall Conference 2024* ([KSAS program record](https://ksas.or.kr/proceedings/2024b/data/2024%EB%85%84%EB%8F%84%20%EC%B6%94%EA%B3%84%20%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%A8%28%EC%95%88%29%20v9.pdf)).

---
<p class="news-date">October 16, 2024</p>

## AAM Vehicle Digital Twin with ePropulsion and Software Integration

This Aerospace Systems Engineering Society Fall Conference paper continues the AAM vehicle digital twin line by emphasizing integration strategy. Instead of treating propulsion, software, simulation, and certification artifacts as separate pieces, the work frames them as a coordinated virtual-certification workflow.

<figure>
  <img src="/images/news/241016/aam-digital-twin-epropulsion-cover.webp" alt="Scientific illustration of AAM vehicle digital twin ePropulsion and software integration" width="1200" height="675" loading="lazy" decoding="async">
  <figcaption>Scientific illustration: ePropulsion modules, digital-twin aircraft, software integration flows, and virtual-certification loops.</figcaption>
</figure>

### What the paper contributes

- Describes an AAM vehicle digital twin strategy connecting advanced ePropulsion and software integration.
- Supports virtual certification by organizing simulation, implementation, and validation concerns in one twin-centered workflow.
- Extends the AAM-VDT research direction from platform concept toward integration practice.

### Why this matters

- Advanced air mobility systems need credible virtual-certification pipelines before flight-test campaigns can scale safely.
- Integration strategy is as important as simulation fidelity because propulsion, software, and validation data must stay aligned.
- This post fills the October 2024 digital-twin publication gap in the News timeline.

**Publication record:** Published on October 16, 2024 in the *Proceedings of the Aerospace Systems Engineering Society Fall Conference 2024*, pages 719-722 ([DBpia record](https://www.dbpia.co.kr/journal/articleDetail?nodeId=NODE12058721)).

---
<p class="news-date">October 4, 2024</p>

## ULoRA for Universal Low-Rank Adaptation

The ULoRA OpenReview submission explores a practical question in modern deep learning: can low-rank adaptation be made more universal across diverse model architectures instead of being tuned narrowly for one network family? The work sits at the intersection of efficient fine-tuning, architectural transfer, and reusable adaptation modules.

<figure>
  <img src="/images/news/241004/ulora-cover.webp" alt="Scientific illustration of universal low-rank adaptation across deep learning architectures" width="1200" height="675" loading="lazy" decoding="async">
  <figcaption>Scientific illustration: lightweight adapter layers bridging multiple neural architectures through a shared low-rank adaptation space.</figcaption>
</figure>

### What the paper contributes

- Frames low-rank adaptation as a cross-architecture problem rather than only a task-specific fine-tuning trick.
- Studies how adapter-style modules can support diverse deep learning models under one adaptation principle.
- Adds an efficient learning systems thread to the News page's AI and autonomy coverage.

### Why this matters

- Parameter-efficient adaptation is important when models are too large to retrain for every downstream setting.
- A universal adaptation view can reduce engineering fragmentation across vision, language, and control workflows.
- The post records the October 2024 OpenReview submission in the publication chronology while clearly treating it as a submission record.

**Publication record:** Posted on October 4, 2024 as an *ICLR 2025 Conference withdrawn submission* on OpenReview ([OpenReview record](https://openreview.net/forum?id=bYsieh8LE2)).

---
<p class="news-date">September 14, 2024</p>

## Enhancing IoT Disaster Detection Systems with Stochastic Models Across Multiple Geographic Areas

This *ICT Express* publication studies disaster detection as a distributed cyber-physical system spanning **multiple geographic areas**. It combines LoRaWAN sensing, fog resources, and cloud processing with stochastic modeling so planners can reason about response time, utilization, and deployment capacity before building large-scale monitoring infrastructure.

<figure>
  <img src="/images/news/250201/disaster-detection-cover.webp" alt="Scientific illustration of multi-region IoT disaster detection with cloud-fog monitoring" width="1200" height="675" loading="lazy" decoding="async">
  <figcaption>Scientific illustration: LoRaWAN-aware stochastic models for cloud-fog monitoring across disaster-prone regions.</figcaption>
</figure>

### What the paper contributes

- Introduces **two Stochastic Petri Net models** for IoT disaster detection across geographically distributed monitoring regions.
- Evaluates key performance indicators including mean response time, drop probability, resource utilization, and server-processing capacity.
- Uses sensitivity analysis to show how fog and cloud resource choices affect responsiveness under large-scale disaster-monitoring demand.

### Why this matters

- Disaster-detection infrastructure must cover high-risk and often secluded areas without becoming prohibitively expensive.
- Modeling the system before deployment helps identify where additional cores, fog capacity, or communication resources actually improve service quality.
- The study gives disaster-response planners a more disciplined way to connect sensing coverage, computing capacity, and operational resilience.

<figure>
  <img src="/images/news/240914/IoT_Disaster_Detection_System_and_Stochastic_Models.png" alt="IoT Disaster Detection System and Stochastic Modeling" width="900" loading="lazy" decoding="async">
  <figcaption>Technical model detail: IoT disaster detection system and stochastic modeling structure.</figcaption>
</figure>

**Publication record:** Published in February 2025 in *ICT Express*, Volume 11, Issue 1, Pages 34-40 ([DOI](https://doi.org/10.1016/j.icte.2024.09.005), [ScienceDirect article](https://www.sciencedirect.com/science/article/pii/S2405959524001085)).

---
<p class="news-date">August 28, 2024</p>

## Efficient UAV Flights and Operational Performance in Delivery Services

This *IEEE Access* article examines UAV delivery as a battery-aware logistics system rather than a simple point-to-point flight problem. The study compares solo flights and cooperative package-transfer strategies through stochastic models, making it possible to reason about delivery time, charging policy, fleet coordination, and operational performance together.

<figure>
  <img src="/images/news/240828/uav-delivery-cover.webp" alt="Scientific illustration of cooperative UAV delivery performance modeling" width="1200" height="675" loading="lazy" decoding="async">
  <figcaption>Scientific illustration: battery-aware drone delivery, charging nodes, and cooperative package transfer.</figcaption>
</figure>

### What the paper contributes

- Develops stochastic models for UAV delivery operations with and without package transfer between drones.
- Studies how charging time, charging-station placement, fleet size, and package handoff influence end-to-end delivery performance.
- Provides a quantitative basis for comparing individual UAV missions against cooperative logistics strategies.

### Why this matters

- Drone delivery depends on energy constraints as much as path planning, so battery and charging assumptions must be visible in the model.
- Cooperative package transfer can reduce operational friction when one drone should not be forced to complete an entire delivery alone.
- The result is useful for logistics planning because route efficiency, battery limits, and cooperative operations are evaluated together.

<figure>
  <img src="/images/news/240828/Transport_system_with_without_considering_package_transfer.png" alt="Transport system with and without considering package transfer" width="900" loading="lazy" decoding="async">
  <figcaption>Technical model detail: transport system with and without package transfer.</figcaption>
</figure>

**Publication record:** Published in *IEEE Access*, Volume 12, Pages 144544-144564 ([DOI](https://doi.org/10.1109/ACCESS.2024.3449283), [IEEE Xplore](https://ieeexplore.ieee.org/document/10646335)).

---
<p class="news-date">July 29, 2024</p>

## SHANGUS: Redefining Autonomous Exploration with Deep Reinforcement Learning

This arXiv preprint presents **SHANGUS / FH-DRL**, a framework that connects frontier heuristics with deep reinforcement learning for faster autonomous exploration in unknown environments. The key idea is to let heuristic frontier selection guide where the robot should explore while DRL handles robust navigation through cluttered, dynamic space.

<figure>
  <img src="/images/news/240729/shangus-fhdrl-cover.webp" alt="Scientific illustration of SHANGUS and FH-DRL autonomous exploration" width="1200" height="675" loading="lazy" decoding="async">
  <figcaption>Scientific illustration: frontier heuristics, DRL navigation, and occupancy-grid exploration.</figcaption>
</figure>

### What the paper contributes

- Combines the adaptability of **deep reinforcement learning** with exponential-hyperbolic frontier heuristics for autonomous exploration.
- Separates frontier selection from DRL navigation, giving the system a clearer division between exploration strategy and local movement.
- Evaluates the approach in ROS2 and Gazebo environments against traditional baselines such as Nearest Frontier, CFE, and GDAE.

### Why this matters

- Exploration robots need to move quickly without wasting travel distance or getting trapped by local clutter.
- Hybridizing heuristic frontier selection with DRL makes the method easier to interpret than a fully opaque policy while still preserving adaptive navigation.
- The framework has natural applications in industrial automation, autonomous driving, household robotics, and space-oriented exploration tasks.

### Watch Our Demos

- **Simple World:** [Watch the demo](https://www.youtube.com/watch?v=XwZ63Wk4ATA)
- **Moderate Complex World:** [Watch the demo](https://www.youtube.com/watch?v=ZNepJp0hCFQ)
- **Most Complex World:** [Watch the demo](https://www.youtube.com/watch?v=Fm22Bq6hr68)

**Publication record:** Posted as *FH-DRL: Exponential-Hyperbolic Frontier Heuristics with DRL for accelerated Exploration in Unknown Environments* on arXiv ([arXiv abstract](https://arxiv.org/abs/2407.18892), [DOI](https://doi.org/10.48550/arXiv.2407.18892)).

---
<p class="news-date">July 20, 2024</p>

## Pilot-in-the-loop simulation with virtual reality (PILS-VR) running on top of cloud-in-the-loop simulation (CILS)

I am excited to share the progress our team has made in a short period. It was an honor to represent our group at the Conference on Automation, Control, and Robotics Engineering (CACRE 2024) in Jeju. Our collaboration with Korean students, combined with the relentless efforts of our Vietnamese team at KADA, has led to remarkable developments. 

In a short time, we have successfully expanded our Pilot-in-the-Loop Simulation (PILS) system by integrating it with Virtual Reality (VR) on the Cloud-in-the-Loop Simulation (CILS) platform. A special thanks to my colleagues: Dr. Vinh Vinh Phạm, Nghĩa, and Nguyễn Viết Nghĩa. Please excuse the rudimentary graphics as our focus wasn't on 3D development.

### PILS-VR System Overview

[Watch our video on the latest in aviation simulation technology: the Pilot-in-the-Loop Simulation with Virtual Reality (PILS-VR)](https://youtu.be/_kyAtntDHmc)

In this video, we showcase our innovative system developed at the Konkuk Aerospace Design Airworthiness Institute (KADA). We've successfully integrated PILS with our Cloud-in-the-Loop Simulation (CILS) system, built on the KP-2 platform for Future Advanced Air Mobility (AAM).

**Highlights of PILS-VR:**

- **Realistic VR Training:** Experience a highly immersive training environment that simulates real-world flight conditions and emergency scenarios.
- **Cloud-Based Flexibility:** Seamless integration with CILS enables remote access, real-time data analysis, and collaborative training, enhancing flexibility and efficiency.
- **Cost-Effective Solutions:** Reduce traditional training costs and increase accessibility with our advanced VR and cloud technologies.
- **Personalized Feedback:** Benefit from detailed performance tracking and tailored feedback to accelerate learning and improve skills.

Join us to see how PILS-VR is revolutionizing pilot training and setting new standards in aviation safety.

### Data Exchange Method Development

[Watch our video on the method to extract data exchanged between KFDS and PX4 during simulation run-time](https://www.youtube.com/watch?v=1BYQKzVgXeQ)

Using this method, we can input control signal data from pre-existing files into KFDS, which then loads these control data according to the predetermined times specified in the files. Subsequently, the flight state data generated by KFDS are recorded for validation or virtual certification purposes.

### (p/d) Twin Data Center

[Watch our video on Twin Data Center](https://youtu.be/byyYU9jCaTk)

All data from KFDS and PX4 are collected in run-time simulation for further analysis and prediction for future updates of digital twin models in the virtual world.

---
<p class="news-date">July 20, 2024</p>

## 2024 9th International Conference on Automation, Control and Robotics Engineering (CACRE 2024)

I am thrilled to share that I had the incredible opportunity to attend and present at the 2024 International Conference on Automation, Control, and Robotics Engineering (CACRE 2024) held on Jeju Island, South Korea, from July 18-20, 2024. This prestigious conference brought together leading experts, researchers, and practitioners in the fields of automation, control, and robotics from around the world.

As part of the conference, I presented our latest research from the Konkuk Aerospace Design-Airworthiness Institute (KADA). Our study, titled "AAM-VDT: Vehicle Digital Twin for Tele-Operations in Advanced Air Mobility," delves into the innovative use of digital twin technology for enhancing tele-operations in the realm of advanced air mobility. 

I am honored to share that our presentation received the Excellent Oral Presentation award in the Special Session IX: Modeling, Control, and AI for Autonomous Vehicles. This session was chaired by Sungjin Cho from Sunchon National University, South Korea, with Sangho Kim from Konkuk University, South Korea, serving as Vice Session Chair.

I am incredibly grateful to my professor and co-author, Professor Jae-Woo Lee, the Director of KADA, and all the contributors for their hard work and dedication to this project. A special thank you to the conference organizers and attendees for providing such a fantastic platform to share our work and engage with the global community.

Looking forward to the future collaborations and advancements in this exciting field!

<figure>
    <img src="/images/news/240720/CACRE_2024_Presentation.jpg" alt="Presentation at CACRE 2024">
    <figcaption>AAM-VDT Presentation at CACRE 2024</figcaption>
</figure>
<figure>
    <img src="/images/news/240720/CACRE_2024_Information.png" alt="CACRE 2024 Information">
    <figcaption>CACRE 2024 Information</figcaption>
</figure>

---
<p class="news-date">June 17, 2024</p>

## Disaster-Survivable Cloud Microservices with Energy-Aware Consolidation

This *Computing* article studies cloud microservices under disaster-survivability constraints. The central question is not simply whether a service can recover, but how consolidation and dynamic response strategies affect energy use, recovery behavior, and infrastructure efficiency during stressed operating conditions.

<figure>
  <img src="/images/news/240617/cloud-microservices-disaster-survivability-cover.webp" alt="Scientific illustration of disaster-survivable cloud microservices with energy-aware consolidation" width="1200" height="675" loading="lazy" decoding="async">
  <figcaption>Scientific illustration: cloud microservice consolidation, energy-aware response, and survivability rerouting under risk.</figcaption>
</figure>

### What the paper contributes

- Evaluates dynamic response and consolidation strategies for cloud microservice survivability.
- Connects disaster recovery behavior with energy-aware operation instead of analyzing them in isolation.
- Provides a quantitative foundation for choosing consolidation policies under disruption scenarios.

### Why this matters

- Disaster survivability is a capacity-planning problem as much as an availability problem.
- Energy-aware consolidation can improve efficiency, but aggressive consolidation may interact with recovery objectives.
- The paper strengthens the News page's infrastructure-dependability storyline between early 2024 cloud work and later Kubernetes autoscaling work.

**Publication record:** Published online on June 17, 2024 in *Computing*, Volume 106, pages 2737-2783 ([DOI](https://doi.org/10.1007/s00607-024-01305-x), [Springer article](https://link.springer.com/article/10.1007/s00607-024-01305-x)).

---
<p class="news-date">May 14, 2024</p>

## Advanced Air Mobility-Vehicle Digital Twin (AAM-VDT)

This AAM-VDT release presents a vehicle digital twin platform for tele-operations in **Advanced Air Mobility**. The work brings together cloud computing, AI-assisted operation, simulation, and flight-data exchange around the Konkuk Passenger Vehicle platform, turning the project from a demonstration stack into a research artifact with a clear publication trail.

<figure>
  <img src="/images/news/250402/vehicle-digital-twin-cover.webp" alt="Scientific illustration of an AAM vehicle digital twin for tele-operations" width="1200" height="675" loading="lazy" decoding="async">
  <figcaption>Scientific illustration: AAM vehicle digital twin, simulation loop, and tele-operation data flow.</figcaption>
</figure>

### What the paper contributes

- Integrates cloud-in-the-loop simulation, software-in-the-loop simulation, and operational digital twin components for AAM vehicle studies.
- Connects KP-2/KP2C simulation and flight-test data flows so future twin models can be updated from runtime behavior.
- Frames tele-operation as a safety-critical digital twin problem involving heterogeneous vehicles, real-time monitoring, and operational decision support.

### Why this matters

- AAM systems need validation environments where flight dynamics, operator decisions, and cloud infrastructure can be tested before expensive field operations.
- A vehicle digital twin gives researchers a shared backbone for virtual certification, multi-vehicle coordination, and safety-aware scenario design.
- The section now reads visually as a publication/project research story while retaining the original media and demonstration archive below.

### Media

- [VDT Simulation System](https://youtu.be/ePH-f1H2PH8)
- [VDT Concept Illustration](https://youtu.be/9effNK__aOU)
- [VDT Simulation in KU Map (01)](https://youtu.be/X20FuC0C7pM)
- [VDT Simulation in KU Map (02)](https://youtu.be/huKKna1OFjA)
- [VDT Simulation in Seoul Map (Fixed Wing)](https://youtu.be/luD0U2uVrgg)
- [VDT Simulation Scenarios](https://youtu.be/QfZZfo9YNls)
- [KP2C Real Flight Test](https://youtu.be/qfMXk1IYKFA)
- [KP2C es-DNLC Flight Test](https://youtu.be/u0xFRdc-97Q)
- [KP2C LQR Flight Test](https://youtu.be/FqyS67FReXo)

Special thanks to our diligent KADA engineers and researchers! Jeongseok Hyun, Minseok Jang, Taeho Kwag, Nghia Nguyen, Vinh Pham, AYE AYE MAW

Excited about the possibilities that lie ahead as we continue to innovate and drive advancements in advanced air mobility.

**Publication record:** Posted as *AAM-VDT: Vehicle Digital Twin for Tele-Operations in Advanced Air Mobility* on arXiv ([arXiv abstract](https://arxiv.org/abs/2404.09621), [DOI](https://doi.org/10.48550/arXiv.2404.09621)).

<figure>
    <img src="/images/news/240512/AAM-VDT/VDT Techs..jpg" alt="VDT Techs">
    <figcaption>VDT Technologies of KADA</figcaption>
</figure>
<figure>
    <img src="/images/news/240512/AAM-VDT/VDT Simulation System.jpg" alt="VDT Simulation System">
    <figcaption>VDT Simulation System for Demonstration</figcaption>
</figure>
<figure>
    <img src="/images/news/240512/AAM-VDT/VDT-CILS.jpg" alt="VDT-CILS">
    <figcaption> VDT Cloud in the loop simulation (CILS) </figcaption>
</figure>
<figure>
    <img src="/images/news/240512/AAM-VDT/VDT-Single-ODT.jpg" alt="VDT Single ODT">
    <figcaption>VDT Single Vehicle integrated with operational digital twin (ODT)</figcaption>
</figure>
<figure>
    <img src="/images/news/240512/AAM-VDT/VDT-SITL.jpg" alt="VDT SITL">
    <figcaption>VDT software in the loop simulation (SITL)</figcaption>
</figure>
<figure>
    <img src="/images/news/240512/AAM-VDT/VDT-SITL-Simplified.jpg" alt="VDT SITL Simplified">
    <figcaption>VDT PX4-KFDS SITL with Bridge</figcaption>
</figure>

---

<iframe src="https://www.youtube.com/embed/ePH-f1H2PH8" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
<iframe src="https://www.youtube.com/embed/9effNK__aOU" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
<iframe src="https://www.youtube.com/embed/X20FuC0C7pM" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
<iframe src="https://www.youtube.com/embed/huKKna1OFjA" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
<iframe src="https://www.youtube.com/embed/luD0U2uVrgg" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
<iframe src="https://www.youtube.com/embed/QfZZfo9YNls" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
<iframe src="https://www.youtube.com/embed/qfMXk1IYKFA" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
<iframe src="https://www.youtube.com/embed/u0xFRdc-97Q" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
<iframe src="https://www.youtube.com/embed/FqyS67FReXo" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

<div class="separator"></div>

<p class="news-date">May 10, 2024</p>

## IEEE/IFIP Network Operations and Management Symposium (NOMS 2024) - 6-10 May 2024 // Seoul, South Korea

[NOMS 2024 Symposium](https://noms2024.ieee-noms.org/)

I am excited to announce my attendance at the 2024 IEEE/IFIP Network Operations and Management Symposium (NOMS 2024), which took place from May 6 to May 10, 2024, at The-K Hotel in Seoul, South Korea. Returning to Korea after two decades, this symposium was a pivotal event for professionals in the network operations and management field. NOMS 2024 featured an extensive program with keynotes, technical sessions, panel discussions, and various workshops. The theme for this year was "Towards intelligent, reliable, and sustainable network and service management," focusing on the latest advancements in 5G and emerging 6G networks and their roles in supporting critical applications such as IoT, smart cities, and autonomous vehicles. This event gathered researchers, developers, service providers, and policymakers, offering a unique platform for knowledge exchange and collaboration in shaping the future of network management.

At NOMS 2024, we presented *Optimal Resource Utilization in Hyperledger Fabric: A Comprehensive SPN-Based Performance Evaluation Paradigm*. The paper studies permissioned blockchain performance through Stochastic Petri Nets, with special attention to endorsement, ordering, commit, resource utilization, and response-time sensitivity.

<figure>
  <img src="/images/news/250205/hyperledger-cover.webp" alt="Scientific illustration of Hyperledger Fabric transactional dynamics and SPN performance modeling" width="1200" height="675" loading="lazy" decoding="async">
  <figcaption>Scientific illustration: SPN-based Hyperledger Fabric transaction flow and performance evaluation.</figcaption>
</figure>

### What the paper contributes

- Develops an **SPN model** for evaluating Hyperledger Fabric performance under different transaction-arrival and block-size configurations.
- Breaks the blockchain transaction process into endorsement, ordering, and commit phases so bottlenecks can be analyzed with clearer structure.
- Uses case studies and sensitivity analysis to identify which configuration factors most strongly affect mean response time and throughput.

### Why this matters

- Permissioned blockchain systems often look reliable at the architectural level but become fragile when configuration choices overload transaction flow.
- A stochastic model gives administrators a pre-deployment way to test resource utilization and capacity planning before operational costs rise.
- The conference version established the performance-modeling foundation that later connects naturally with the journal publication on transactional dynamics.

**Publication record:** Published in *NOMS 2024 - 2024 IEEE Network Operations and Management Symposium*, Pages 1-7 ([DOI](https://doi.org/10.1109/NOMS59830.2024.10575284), [IEEE Xplore](https://ieeexplore.ieee.org/document/10575284)).

Special thanks to our Brazilian team, coordinated by [Francisco Airton Silva](https://iuresf.gitlab.io/pasid-site/airton.html), Laboratory of Applied Research to Distributed Systems (PASID), Federal University of Piauí (UFPI) (campus Picos), Teresina, Piauí, Brazil, for their collaboration in the research.

During the conference, I had the pleasure of meeting [Jin-Hee Cho](https://people.cs.vt.edu/~jicho/), a collaborator of my Ph.D. supervisor, [Dongseong Kim](https://researchers.uq.edu.au/researcher/23703). Jin-Hee Cho is now an Associate Professor in the Department of Computer Science at Virginia Tech. It was great to converse with her and attend her fascinating research presentation. It's remarkable how small and interconnected the world can be.

<figure>
    <img src="/images/news/240510/NOMS 2024/NOMS 2024 (01).jpg" alt="NOMS 2024 Photo 1">
    <figcaption>Our presentation at NOMS</figcaption>
</figure>
<figure>
    <img src="/images/news/240510/NOMS 2024/NOMS 2024 (02).jpg" alt="NOMS 2024 Photo 2">
    <figcaption>NOMS 2024 whole week schedule</figcaption>
</figure>
<figure>
    <img src="/images/news/240510/NOMS 2024/NOMS 2024 (03).jpg" alt="NOMS 2024 Photo 3">
    <figcaption> A system demonstration at NOMS 2024 </figcaption>
</figure>

---
<p class="news-date">April 1, 2024</p>

## Aerial Computing with UAV Data Bridges

This *ICT Express* article studies aerial computing as a way to extend mobile cloud computing with UAVs acting as data bridges. The contribution treats unmanned aerial vehicles as dependability-relevant infrastructure elements, not only as mobile carriers or isolated sensing platforms.

<figure>
  <img src="/images/news/240401/aerial-computing-uav-data-bridges-cover.webp" alt="Scientific illustration of UAV data bridges for aerial computing and mobile cloud dependability" width="1200" height="675" loading="lazy" decoding="async">
  <figcaption>Scientific illustration: UAVs relaying data between mobile users, edge stations, and cloud services through dependability-aware state transitions.</figcaption>
</figure>

### What the paper contributes

- Models UAV-assisted mobile cloud computing as an aerial data-bridge architecture.
- Uses Markov-chain-based dependability quantification to evaluate how UAV bridges affect service continuity.
- Connects mobile cloud performance with unmanned aerial systems and infrastructure reliability.

### Why this matters

- UAVs can expand connectivity, but they also introduce mobility, battery, and failure dynamics that must be modeled.
- Dependability quantification helps determine when aerial relays improve the system and when they add operational risk.
- This post adds the April 2024 aerial-computing publication into the News sequence.

**Publication record:** Published in April 2024 in *ICT Express*, Volume 10, Issue 2, pages 389-396 ([DOI](https://doi.org/10.1016/j.icte.2023.10.002), [ScienceDirect article](https://www.sciencedirect.com/science/article/pii/S2405959523001385)).

---
<p class="news-date">February 23, 2024</p>

## YOLOTransfer-DT for UAM Situation Awareness

This *Aerospace* article presents **YOLOTransfer-DT**, an operational digital twin framework for collision detection and situation awareness in urban aerial mobility. The work links deep learning, transfer learning, and simulated twin environments so perception models can be trained and evaluated around UAM safety requirements.

<figure>
  <img src="/images/news/240223/yolotransfer-dt-cover.webp" alt="Scientific illustration of YOLOTransfer-DT for urban aerial mobility situation awareness" width="1200" height="675" loading="lazy" decoding="async">
  <figcaption>Scientific illustration: UAM digital twin simulation, object-detection geometry, transfer-learning streams, and collision-awareness layers.</figcaption>
</figure>

### What the paper contributes

- Introduces a YOLOTransfer-DT framework for AI training in simulated UAM digital-twin environments.
- Applies deep and transfer learning to collision detection and situation awareness for aerial mobility operations.
- Treats the operational digital twin as a safety-oriented training and validation environment rather than only a visualization layer.

### Why this matters

- UAM vehicles need perception systems that can be stress-tested before dense urban deployment.
- Transfer learning can reduce the cost of building specialized detection models for new aerial scenarios.
- The paper gives the News timeline a dedicated post for one of the key early-2024 digital-twin journal publications.

**Publication record:** Published on February 23, 2024 in *Aerospace*, Volume 11, Issue 3, Article 179 ([DOI](https://doi.org/10.3390/aerospace11030179), [MDPI article](https://www.mdpi.com/2226-4310/11/3/179)).

---
<p class="news-date">February 20, 2024</p>

## Resource Redundancy for Smart City Dependability

This *Cluster Computing* article focuses on how redundancy choices influence smart city dependability. Instead of assuming extra resources always improve outcomes, the study uses a model-driven approach to quantify where redundancy helps, where it adds overhead, and how it changes the resilience of connected city services.

<figure>
  <img src="/images/news/240220/smart-city-resource-redundancy-cover.webp" alt="Scientific illustration of smart city resource redundancy and dependability modeling" width="1200" height="675" loading="lazy" decoding="async">
  <figcaption>Scientific illustration: redundant smart-city resources, mirrored service paths, and model-driven dependability loops.</figcaption>
</figure>

### What the paper contributes

- Quantifies the impact of resource redundancy on smart city system dependability.
- Uses a model-driven approach to connect infrastructure design choices with availability-oriented outcomes.
- Gives planners a way to compare redundancy strategies before deploying expensive city-scale infrastructure.

### Why this matters

- Smart-city systems depend on many interacting resources, so redundancy must be tuned rather than added blindly.
- Model-driven dependability analysis helps expose trade-offs between cost, resilience, and operational complexity.
- This post adds the missing February 2024 smart-city publication into the News page.

**Publication record:** Published online on February 20, 2024 in *Cluster Computing*, Volume 27, pages 6059-6079 ([DOI](https://doi.org/10.1007/s10586-023-04259-5), [Springer article](https://link.springer.com/article/10.1007/s10586-023-04259-5)).

---
<p class="news-date">January 1, 2024</p>

## Internet of Medical Things Performability Analysis

This *International Journal of Computer Applications in Technology* article studies the Internet of Medical Things as a performability problem. Medical sensing systems must remain available and responsive while handling constrained devices, edge/fog/cloud resources, and healthcare monitoring workflows that cannot tolerate avoidable bottlenecks.

<figure>
  <img src="/images/news/240101/internet-of-medical-things-cover.webp" alt="Scientific illustration of Internet of Medical Things performability analysis" width="1200" height="675" loading="lazy" decoding="async">
  <figcaption>Scientific illustration: medical sensors, edge/fog/cloud monitoring, queueing flows, and performability-oriented healthcare infrastructure.</figcaption>
</figure>

### What the paper contributes

- Evaluates Internet of Medical Things infrastructure through a performability and performance-analysis lens.
- Connects medical monitoring workloads with edge/fog/cloud capacity and service-continuity concerns.
- Adds a healthcare IoT publication milestone to the News chronology.

### Why this matters

- Healthcare monitoring systems need both performance and dependability; one without the other is not enough.
- Performability analysis helps identify bottlenecks before they affect medical information flows.
- The post broadens the News page's IoT coverage beyond smart-city and industrial automation systems.

**Publication record:** Published in 2024 in *International Journal of Computer Applications in Technology*, Volume 75, Issue 1, pages 35-47 ([DOI](https://doi.org/10.1504/IJCAT.2024.144667), [Inderscience record](https://www.inderscience.com/info/inarticle.php?artid=144667)).

---
<p class="news-date">January 1, 2024</p>

## Event-Based Moving Target Defense with VM Migration

This *IEEE Access* article studies moving target defense in cloud computing using virtual machine migration. The paper treats defense as a dynamic event-based mechanism: the system changes its attack surface over time, but those movements must be evaluated against migration overhead and service performance.

<figure>
  <img src="/images/news/240101/cloud-moving-target-defense-cover.webp" alt="Scientific illustration of event-based moving target defense with VM migration" width="1200" height="675" loading="lazy" decoding="async">
  <figcaption>Scientific illustration: VM migration, event-triggered moving target defense, and shielded cloud service continuity.</figcaption>
</figure>

### What the paper contributes

- Models event-based moving target defense in cloud environments using VM migration.
- Connects security adaptation with performance modeling so defense cost is visible.
- Provides a quantitative view of how migration-based defense can reshape exposure while preserving service behavior.

### Why this matters

- Moving target defense is only useful if the infrastructure can absorb the migration overhead.
- Performance modeling helps distinguish practical defense schedules from policies that protect security at the expense of service quality.
- This post strengthens the News page's cloud-security and VM-migration coverage.

**Publication record:** Published in 2024 in *IEEE Access*, Volume 12, pages 165539-165554 ([DOI](https://doi.org/10.1109/ACCESS.2024.3393998), [IEEE Xplore record](https://ieeexplore.ieee.org/document/10506158)).

---
<p class="news-date">January 1, 2024</p>

## Energy Consumption in Microservices Architectures

This *IEEE Access* article reviews energy consumption in microservices architectures. It gives the microservices research line a systematic baseline: before new autoscaling, migration, or consolidation mechanisms can be evaluated fairly, the field needs a clear map of how energy is measured, modeled, and reduced.

<figure>
  <img src="/images/news/240101/microservices-energy-slr-cover.webp" alt="Scientific illustration of energy consumption evidence mapping in microservices architectures" width="1200" height="675" loading="lazy" decoding="async">
  <figcaption>Scientific illustration: microservice modules, energy measurement paths, and evidence clusters for a systematic review.</figcaption>
</figure>

### What the paper contributes

- Surveys energy-consumption research across microservices architectures.
- Organizes measurement, modeling, and optimization evidence into a structured view of the field.
- Provides context for later work on energy-aware Kubernetes autoscaling and cloud microservice consolidation.

### Why this matters

- Microservices make systems easier to evolve, but they can also hide energy costs across many small services.
- A systematic review helps researchers avoid duplicated effort and identify where measurement evidence is still weak.
- This post adds the missing energy-focused review paper to the News archive as a dedicated story.

**Publication record:** Published in 2024 in *IEEE Access*, Volume 12, pages 186710-186729 ([DOI](https://doi.org/10.1109/ACCESS.2024.3389064), [IEEE Xplore record](https://ieeexplore.ieee.org/document/10498400)).

---
<p class="news-date">January 1, 2024</p>

## PIND-UAM for Physics-Informed eVTOL Digital Twins

This *Transportation Research Procedia* paper presents **PIND-UAM**, a physics-informed neural dynamics approach for boxed-wing eVTOL aircraft in UAM vehicle digital twins. The work connects neural modeling with physics structure so the digital twin can represent vehicle dynamics more credibly than a purely data-driven black box.

<figure>
  <img src="/images/news/240101/pind-uam-cover.webp" alt="Scientific illustration of physics-informed neural dynamics for boxed-wing eVTOL digital twins" width="1200" height="675" loading="lazy" decoding="async">
  <figcaption>Scientific illustration: boxed-wing eVTOL dynamics, physics-informed neural layers, aerodynamic flow, and digital-twin simulation surfaces.</figcaption>
</figure>

### What the paper contributes

- Applies physics-informed neural dynamics to boxed-wing eVTOL aircraft modeling.
- Positions the method inside a UAM vehicle digital twin workflow rather than as an isolated neural network.
- Connects aerodynamic behavior, vehicle dynamics, and digital-twin representation for future mobility systems.

### Why this matters

- Digital twins for UAM need models that are both learnable from data and constrained by physical behavior.
- Physics-informed dynamics can improve trust in twin behavior when flight-test data are limited or expensive.
- This post completes the early-2024 digital-twin publication cluster alongside YOLOTransfer-DT and AAM-VDT.

**Publication record:** Published in 2024 in *Transportation Research Procedia*, Volume 80, pages 30-37 ([DOI](https://doi.org/10.1016/j.trpro.2024.09.005), [ScienceDirect record](https://www.sciencedirect.com/science/article/pii/S2352146524004438)).

---

<p class="news-date">December 20, 2023</p>

## Hierarchical Kriging for Multi-Fidelity Aerodynamic Models

This *Aerospace* article presents an extended hierarchical kriging method for aerodynamic model generation when several low-fidelity datasets are available. The work targets a common aircraft-design problem: teams often have many inexpensive simulations with different fidelity levels, but need a reliable model that can support higher-confidence aerodynamic prediction.

<figure>
  <img src="/images/news/231220/hierarchical-kriging-aerodynamic-cover.webp" alt="Scientific illustration of hierarchical kriging for multi-fidelity aerodynamic model generation" width="1200" height="675" loading="lazy" decoding="async">
  <figcaption>Scientific illustration: layered low-fidelity aerodynamic datasets, kriging interpolation, uncertainty structure, and a refined aircraft response surface.</figcaption>
</figure>

### What the paper contributes

- Extends hierarchical kriging to incorporate multiple low-fidelity aerodynamic datasets.
- Uses multi-fidelity structure to improve model generation when high-fidelity aerodynamic evidence is limited or expensive.
- Adds a rigorous aerospace modeling milestone to the News chronology.

### Why this matters

- Aerodynamic design depends on trustworthy models built from uneven simulation evidence.
- Multi-fidelity kriging helps turn scattered analysis results into a coherent design surface.
- The dedicated cover replaces a generic archive visual with a publication-specific aerospace illustration.

**Publication record:** Published online on December 20, 2023 in *Aerospace*, Volume 11, Issue 1, Article 6 ([DOI](https://doi.org/10.3390/aerospace11010006), [MDPI article](https://www.mdpi.com/2226-4310/11/1/6)).

---
<p class="news-date">November 28, 2023</p>

## UAM Dependability with VANETs and VM Migration

This *Sensors* article studies Urban Advanced Mobility dependability through a model-based quantification of vehicular ad hoc networks with virtual machine migration. The paper links future mobility operations with the infrastructure behavior needed to keep connected services available under changing network and compute conditions.

<figure>
  <img src="/images/news/231128/uam-vanet-dependability-cover.webp" alt="Scientific illustration of UAM dependability modeling with VANET communication and virtual machine migration" width="1200" height="675" loading="lazy" decoding="async">
  <figcaption>Scientific illustration: UAM vehicles, VANET links, cloud-edge nodes, VM migration paths, and dependability-oriented service continuity.</figcaption>
</figure>

### What the paper contributes

- Quantifies dependability for UAM communication and compute infrastructure using a model-based approach.
- Connects VANET behavior with virtual machine migration, exposing how mobility and cloud decisions interact.
- Gives the News page a dedicated visual story for late-2023 UAM infrastructure research.

### Why this matters

- UAM services will rely on both aerial mobility and robust digital infrastructure.
- VM migration can improve continuity, but it also changes latency and availability behavior.
- A model-based view helps evaluate these trade-offs before deployment.

**Publication record:** Published online on November 28, 2023 in *Sensors*, Volume 23, Issue 23, Article 9485 ([DOI](https://doi.org/10.3390/s23239485), [MDPI article](https://www.mdpi.com/1424-8220/23/23/9485)).

---
<p class="news-date">November 15, 2023</p>

## Spiking Neural Networks for UAM Flight Dynamics Twins

This Korean Society for Aeronautical & Space Sciences Fall Conference paper introduces a digital-twin flight dynamics model for a UAM vehicle using a spiking neural network. The work frames flight dynamics digitalization through event-driven neural computation, connecting aircraft dynamics with more biologically inspired temporal modeling.

<figure>
  <img src="/images/news/231115/uam-spiking-digital-twin-cover.webp" alt="Scientific illustration of a UAM digital twin flight dynamics model using spiking neural networks" width="1200" height="675" loading="lazy" decoding="async">
  <figcaption>Scientific illustration: UAM vehicle dynamics, mirrored digital twin geometry, and spiking neural signals feeding a flight-dynamics model.</figcaption>
</figure>

### What the paper contributes

- Applies a spiking neural network to flight dynamics modeling for UAM vehicle digital twins.
- Positions event-driven neural dynamics as a way to represent temporal flight behavior.
- Adds conference coverage for the 2023 UAM digitalization research thread.

### Why this matters

- Digital twins need dynamic models that can follow changing vehicle states rather than static snapshots.
- Spiking neural networks offer a different computational lens for temporal system behavior.
- The new cover makes the UAM twin concept legible at News-page scale.

**Publication record:** Presented on November 15, 2023 in the *Proceedings of the Korean Society for Aeronautical & Space Sciences Fall Conference 2023*, pages 618-619 ([DBpia record](https://www.dbpia.co.kr/journal/articleDetail?nodeId=NODE11658014)).

---
<p class="news-date">November 15, 2023</p>

## Large Language Models for UAM Attitude Stabilization

This conference paper asks whether large language models can help stabilize the attitude of a UAM vehicle. As a preliminary study, it explores a provocative link between modern language-model reasoning interfaces and classical aerospace control questions, especially attitude stabilization in urban air mobility vehicles.

<figure>
  <img src="/images/news/231115/llm-uam-attitude-control-cover.webp" alt="Scientific illustration of large language model assisted attitude stabilization for a UAM vehicle" width="1200" height="675" loading="lazy" decoding="async">
  <figcaption>Scientific illustration: UAM attitude axes, stabilizing control signals, and an abstract language-model reasoning core coupled to flight control.</figcaption>
</figure>

### What the paper contributes

- Explores large language models as a preliminary component in UAM attitude stabilization research.
- Connects AI reasoning systems with flight-control workflows rather than treating them as separate domains.
- Adds an early LLM-and-control milestone to the News archive.

### Why this matters

- The question is important because autonomous mobility increasingly mixes learning systems with control systems.
- Early studies help clarify where LLMs may assist, supervise, or fail in safety-sensitive aerospace contexts.
- The illustration keeps the AI-control relationship scientific instead of turning it into a generic chatbot visual.

**Publication record:** Presented on November 15, 2023 in the *Proceedings of the Korean Society for Aeronautical & Space Sciences Fall Conference 2023*, pages 1411-1412 ([DBpia record](https://www.dbpia.co.kr/pdf/pdfView.do?nodeId=NODE11658488)).

---
<p class="news-date">October 19, 2023</p>

## Resource Redundancy in Smart City Dependability

This Research Square preprint studies how resource redundancy affects smart city system dependability through a model-driven approach. It treats redundancy as an engineering decision that must be quantified rather than assumed: adding resources may improve availability, but it can also introduce operational complexity and cost.

<figure>
  <img src="/images/news/231019/smart-city-redundancy-preprint-cover.webp" alt="Scientific illustration of smart city resource redundancy and dependability quantification" width="1200" height="675" loading="lazy" decoding="async">
  <figcaption>Scientific illustration: duplicated smart-city resources, backup service paths, model-driven dependability layers, and urban infrastructure continuity.</figcaption>
</figure>

### What the paper contributes

- Quantifies the impact of resource redundancy on smart city dependability.
- Uses a model-driven approach to compare redundancy choices before deployment.
- Establishes the preprint version of the work later represented as a journal publication.

### Why this matters

- Smart cities combine sensing, communication, cloud, and edge services into tightly coupled systems.
- Redundancy has to be placed and scaled carefully to improve dependability without waste.
- This entry keeps the preprint milestone visible in chronological order.

**Publication record:** Posted on October 19, 2023 as a *Research Square* preprint, rs-3427536 ([DOI](https://doi.org/10.21203/rs.3.rs-3427536/v1), [Research Square record](https://www.researchsquare.com/article/rs-3427536/v1)).

---
<p class="news-date">October 17, 2023</p>

## PIGD-TL for Transferable Physics-Informed Dynamics

This ICCAS 2023 paper presents **PIGD-TL**, a physics-informed generative dynamics method with transfer learning. The work sits at the intersection of learning-based dynamics, physics constraints, and reusable modeling knowledge, which is especially relevant when full flight-test or high-fidelity simulation data are limited.

<figure>
  <img src="/images/news/231017/pigd-tl-cover.webp" alt="Scientific illustration of physics-informed generative dynamics with transfer learning" width="1200" height="675" loading="lazy" decoding="async">
  <figcaption>Scientific illustration: source and target dynamics manifolds, transfer-learning bridge, physics constraints, and generated trajectory fields.</figcaption>
</figure>

### What the paper contributes

- Combines generative dynamics modeling with physics-informed structure.
- Uses transfer learning to move modeling knowledge between related dynamics domains.
- Provides another step toward credible data-driven dynamics for aerospace digital twins.

### Why this matters

- Purely data-driven models can drift when data are sparse or conditions change.
- Physics-informed transfer learning can improve reuse while preserving physically plausible behavior.
- The cover highlights the paper's dynamics-transfer theme instead of generic neural-network imagery.

**Publication record:** Presented on October 17, 2023 at *ICCAS 2023 - 23rd International Conference on Control, Automation and Systems*, pages 590-595 ([DOI](https://doi.org/10.23919/ICCAS59377.2023.10316820), [IEEE Xplore record](https://ieeexplore.ieee.org/document/10316820)).

---
<p class="news-date">July 9, 2023</p>

## eVTOL Tilt Angle Planning with Trim Analysis

This Aerospace Europe Conference paper focuses on tilt angle control planning for eVTOL vehicles using trim analysis. The study addresses a core transition-flight question: how a vehicle should coordinate tilt angle changes so that hover, transition, and cruise behavior remain physically consistent and controllable.

<figure>
  <img src="/images/news/230709/evtol-tilt-angle-trim-cover.webp" alt="Scientific illustration of eVTOL tilt angle control planning with trim analysis" width="1200" height="675" loading="lazy" decoding="async">
  <figcaption>Scientific illustration: eVTOL tiltrotor positions, trim-equilibrium surface, transition trajectory, and aerodynamic streamlines.</figcaption>
</figure>

### What the paper contributes

- Uses trim analysis to support tilt angle control planning for an eVTOL vehicle.
- Connects vehicle configuration changes with equilibrium and transition behavior.
- Adds a dedicated visual entry for the EUCASS-CEAS 2023 publication.

### Why this matters

- Transition flight is one of the defining technical challenges for eVTOL aircraft.
- Trim-based planning helps expose feasible tilt schedules before flight testing.
- The image emphasizes the actual tilt-control problem rather than a generic aircraft scene.

**Publication record:** Presented on July 9, 2023 at *Aerospace Europe Conference 2023: Joint 10th EUCASS - 9th CEAS Conference* in Lausanne, Switzerland ([DOI](https://doi.org/10.13009/EUCASS2023-525), [EUCASS record](https://doi.org/10.13009/EUCASS2023-525)).

---
<p class="news-date">July 1, 2023</p>

## Adaptive Data Fusion for Non-Uniform Aerodynamic Data

This *Chinese Journal of Aeronautics* article proposes an adaptive data fusion framework for modeling non-uniform aerodynamic data. The paper responds to a realistic modeling problem: aerodynamic datasets are often uneven, with dense evidence in some regions and sparse observations in others.

<figure>
  <img src="/images/news/230701/nonuniform-aerodynamic-data-fusion-cover.webp" alt="Scientific illustration of adaptive data fusion for non-uniform aerodynamic data modeling" width="1200" height="675" loading="lazy" decoding="async">
  <figcaption>Scientific illustration: non-uniform aerodynamic point clouds, adaptive fusion pathways, wing response surfaces, and uncertainty-aware data modeling.</figcaption>
</figure>

### What the paper contributes

- Builds an adaptive data fusion framework for non-uniform aerodynamic datasets.
- Supports aerodynamic modeling when measurements or simulations are unevenly distributed.
- Strengthens the News page's aerospace modeling storyline between kriging and control-planning work.

### Why this matters

- Non-uniform data can bias models if sparse and dense regions are treated the same way.
- Adaptive fusion helps preserve useful detail while smoothing across gaps.
- A publication-specific cover makes the data-fusion problem visually clear.

**Publication record:** Published in 2023 in *Chinese Journal of Aeronautics* ([DOI](https://doi.org/10.1016/j.cja.2023.05.012), [ScienceDirect record](https://www.sciencedirect.com/science/article/pii/S1000936123001576)).

---
<p class="news-date">June 6, 2023</p>

## Boxed-Wing eVTOL Transition Control Optimization

This ICUAS 2023 paper studies transition control planning and optimization for a boxed-wing eVTOL tiltrotor vehicle using trim analysis. It extends the eVTOL control-planning thread by focusing on a specific vehicle architecture and the optimization needed to move from hover to forward flight.

<figure>
  <img src="/images/news/230606/boxed-wing-transition-control-cover.webp" alt="Scientific illustration of boxed-wing eVTOL tiltrotor transition control optimization with trim analysis" width="1200" height="675" loading="lazy" decoding="async">
  <figcaption>Scientific illustration: boxed-wing tiltrotor transition states, optimized trim trajectory, control surface, and airflow structure.</figcaption>
</figure>

### What the paper contributes

- Plans and optimizes transition control for a boxed-wing eVTOL tiltrotor vehicle.
- Uses trim analysis to keep transition behavior tied to feasible flight conditions.
- Adds a dedicated ICUAS 2023 milestone to the UAM aircraft-control sequence.

### Why this matters

- Boxed-wing tiltrotor vehicles bring different geometry and control constraints than conventional configurations.
- Optimization helps select transition paths that remain stable and efficient.
- The new cover communicates the boxed-wing architecture and transition envelope at a glance.

**Publication record:** Presented on June 6, 2023 at the *2023 IEEE International Conference on Unmanned Aircraft Systems (ICUAS)*, pages 1128-1135 ([DOI](https://doi.org/10.1109/ICUAS57906.2023.10156619), [IEEE Xplore record](https://ieeexplore.ieee.org/document/10156619)).

---
<p class="news-date">May 6, 2023</p>

## Personal Key Recovery for Self-Sovereign Identity

This ICACI 2023 paper proposes an efficient personal key recovery approach for self-sovereign identity environments. The work addresses a practical challenge in decentralized identity: users need control over their own credentials, but they also need robust recovery when keys are lost or compromised.

<figure>
  <img src="/images/news/230506/self-sovereign-key-recovery-cover.webp" alt="Scientific illustration of personal key recovery in self-sovereign identity environments" width="1200" height="675" loading="lazy" decoding="async">
  <figcaption>Scientific illustration: decentralized identity nodes, encrypted recovery shards, protected key capsule, and privacy-preserving recovery paths.</figcaption>
</figure>

### What the paper contributes

- Designs an efficient personal key recovery mechanism for self-sovereign identity.
- Balances user ownership of identity credentials with practical recovery needs.
- Adds a cybersecurity and identity-management publication to the News chronology.

### Why this matters

- Self-sovereign identity can fail in practice if key loss becomes unrecoverable.
- Recovery mechanisms must preserve trust, privacy, and user control.
- The cover visualizes recovery as a secure distributed process rather than a simple lock icon.

**Publication record:** Presented on May 6, 2023 at the *2023 15th International Conference on Advanced Computational Intelligence (ICACI)*, pages 1-8 ([DOI](https://doi.org/10.1109/ICACI58115.2023.10146166), [IEEE Xplore record](https://ieeexplore.ieee.org/document/10146166)).

---
<p class="news-date">May 6, 2023</p>

## iNAV-drlSLAM for Indoor Self-Driving Robots

This ICACI 2023 paper presents **iNAV-drlSLAM**, an improved indoor self-driving framework for mobile robots using deep reinforcement learning integrated with SLAM. It connects mapping, localization, and learned navigation so robots can reason about indoor movement while building or using spatial structure.

<figure>
  <img src="/images/news/230506/inav-drlslam-cover.webp" alt="Scientific illustration of indoor self-driving robot navigation with deep reinforcement learning and SLAM" width="1200" height="675" loading="lazy" decoding="async">
  <figcaption>Scientific illustration: indoor robot, SLAM map geometry, obstacle-aware trajectory, and reinforcement-learning decision paths.</figcaption>
</figure>

### What the paper contributes

- Integrates deep reinforcement learning with SLAM for indoor mobile robot navigation.
- Improves indoor self-driving behavior by combining learned policy decisions with spatial mapping.
- Adds a robotics entry to the 2023 News sequence.

### Why this matters

- Indoor robots need more than path planning; they must interpret changing spatial evidence.
- SLAM provides structure, while reinforcement learning supports adaptive decisions.
- The cover shows navigation, mapping, and policy behavior as one connected system.

**Publication record:** Presented on May 6, 2023 at the *2023 15th International Conference on Advanced Computational Intelligence (ICACI)*, pages 1-8 ([DOI](https://doi.org/10.1109/ICACI58115.2023.10146173), [IEEE Xplore record](https://ieeexplore.ieee.org/document/10146173)).

---
<p class="news-date">May 6, 2023</p>

## QR-GAN: Generative Models Meet Quantile Regression

This ICACI 2023 paper introduces **QR-GAN**, bringing generative adversarial networks together with quantile regression. The work connects generative modeling with distribution-aware prediction, highlighting uncertainty structure rather than reducing the problem to a single expected value.

<figure>
  <img src="/images/news/230506/qr-gan-cover.webp" alt="Scientific illustration of generative adversarial networks combined with quantile regression" width="1200" height="675" loading="lazy" decoding="async">
  <figcaption>Scientific illustration: adversarial neural structures, generated data distributions, and layered quantile-regression bands.</figcaption>
</figure>

### What the paper contributes

- Combines GAN-style generative learning with quantile regression.
- Represents uncertainty through multiple quantile bands instead of only point predictions.
- Adds a machine-learning methods paper to the News page's publication coverage.

### Why this matters

- Many AI systems need calibrated distributional behavior, not only plausible generated samples.
- Quantile regression helps expose the spread and asymmetry of outcomes.
- The cover gives the paper a probability-focused visual identity instead of a generic AI graphic.

**Publication record:** Presented on May 6, 2023 at the *2023 15th International Conference on Advanced Computational Intelligence (ICACI)*, pages 1-8 ([DOI](https://doi.org/10.1109/ICACI58115.2023.10146143), [IEEE Xplore record](https://ieeexplore.ieee.org/document/10146143)).

---
<p class="news-date">February 18, 2023</p>

## UAMDynCon-DT for Data-Driven UAM Dynamics and Control

This ICMCR 2023 paper presents **UAMDynCon-DT**, a data-driven dynamics and robust control framework for UAM vehicle digitalization. It combines dynamics modeling, control behavior, and digital-twin representation to support future urban air mobility aircraft development.

<figure>
  <img src="/images/news/230218/uamdyncon-dt-cover.webp" alt="Scientific illustration of data-driven dynamics and robust control for UAM vehicle digital twins" width="1200" height="675" loading="lazy" decoding="async">
  <figcaption>Scientific illustration: UAM vehicle digital twin, data-driven dynamics streams, robust control core, and stability envelope.</figcaption>
</figure>

### What the paper contributes

- Builds a framework for UAM vehicle digitalization through data-driven dynamics and robust control.
- Links digital-twin modeling with controller-oriented vehicle behavior.
- Adds an early 2023 UAM digital-twin milestone to the News page.

### Why this matters

- UAM digitalization needs both accurate models and control-aware interpretation.
- Robust control helps keep learned or data-driven representations useful in uncertain operating conditions.
- The cover pairs the vehicle and its twin so the system idea is immediately visible.

**Publication record:** Presented on February 18, 2023 at the *2023 International Conference on Mechatronics, Control and Robotics (ICMCR)*, pages 81-85 ([DOI](https://doi.org/10.1109/ICMCR56776.2023.10181072), [IEEE Xplore record](https://ieeexplore.ieee.org/document/10181072)).

---
<p class="news-date">February 18, 2023</p>

## SLAM-DRLnav for Indoor Self-Driving Navigation

This ICMCR 2023 paper presents **SLAM-DRLnav**, a SLAM-enhanced deep reinforcement learning navigation framework for indoor self-driving. It is closely related to the later ICACI indoor navigation entry, emphasizing how mapping and learned control can be integrated for indoor autonomous movement.

<figure>
  <img src="/images/news/230218/slam-drlnav-cover.webp" alt="Scientific illustration of SLAM-enhanced deep reinforcement learning navigation for indoor self-driving" width="1200" height="675" loading="lazy" decoding="async">
  <figcaption>Scientific illustration: indoor self-driving robot, SLAM occupancy geometry, explored trajectories, and learned navigation policy.</figcaption>
</figure>

### What the paper contributes

- Enhances deep reinforcement learning navigation with SLAM-derived spatial information.
- Targets indoor self-driving scenarios where localization, mapping, and control interact.
- Adds the February 2023 robotics conference record as a dedicated story.

### Why this matters

- Indoor autonomy depends on making navigation decisions under partial and evolving maps.
- SLAM-enhanced learning can reduce blind policy behavior by grounding actions in spatial structure.
- The illustration distinguishes this paper from generic robot imagery through map-and-policy visual cues.

**Publication record:** Presented on February 18, 2023 at the *2023 International Conference on Mechatronics, Control and Robotics (ICMCR)*, pages 44-48 ([DOI](https://doi.org/10.1109/ICMCR56776.2023.10181042), [IEEE Xplore record](https://ieeexplore.ieee.org/document/10181042)).

---
<p class="news-date">January 19, 2023</p>

## Robust Attitude Control for PAVs with DNN and CLF

This AIAA SCITECH 2023 paper studies robust attitude control for personal air vehicles using a deep neural network with exponentially stabilizing control Lyapunov functions. The work links neural control with stability guarantees, a crucial concern for flight systems where learning alone is not enough.

<figure>
  <img src="/images/news/230119/pav-robust-attitude-control-cover.webp" alt="Scientific illustration of robust attitude control for personal air vehicles using DNN and control Lyapunov functions" width="1200" height="675" loading="lazy" decoding="async">
  <figcaption>Scientific illustration: PAV attitude axes, neural controller layers, Lyapunov stability basin, and converging control trajectory.</figcaption>
</figure>

### What the paper contributes

- Uses DNN-based control together with exponentially stabilizing control Lyapunov functions.
- Focuses on robust attitude control for personal air vehicle applications.
- Adds an AIAA control-theory milestone to the News chronology.

### Why this matters

- Neural controllers must be connected to stability arguments before they can be trusted in flight.
- Control Lyapunov functions provide a language for convergence and robustness.
- The cover visualizes stability as a physical control landscape rather than as abstract equations.

**Publication record:** Presented on January 19, 2023 at *AIAA SCITECH 2023 Forum*, AIAA 2023-1443 ([DOI](https://doi.org/10.2514/6.2023-1443), [AIAA record](https://arc.aiaa.org/doi/10.2514/6.2023-1443)).

---
<p class="news-date">January 11, 2023</p>

## Performability of Video Streaming on Demand

This *Applied Sciences* article evaluates the performability and sensitivity of a video streaming on demand architecture. Instead of considering performance and dependability separately, the study treats the streaming service as an architecture whose user-facing behavior depends on both service speed and availability under different conditions.

<figure>
  <img src="/images/news/230111/video-streaming-performability-cover.webp" alt="Scientific illustration of performability evaluation and sensitivity analysis for video streaming architecture" width="1200" height="675" loading="lazy" decoding="async">
  <figcaption>Scientific illustration: cloud video pipeline, edge delivery nodes, streaming service paths, sensitivity surface, and performability flow.</figcaption>
</figure>

### What the paper contributes

- Evaluates performability for a video streaming on demand architecture.
- Adds sensitivity analysis so important parameters and bottlenecks are visible.
- Connects media-delivery infrastructure with reliability and performance modeling.

### Why this matters

- Streaming systems fail users when either performance or availability degrades.
- Sensitivity analysis helps prioritize which architecture parameters deserve attention.
- The cover makes performability tangible through cloud, edge, and service-flow motifs.

**Publication record:** Published online on January 11, 2023 in *Applied Sciences*, Volume 13, Issue 2, Article 998 ([DOI](https://doi.org/10.3390/app13020998), [MDPI article](https://www.mdpi.com/2076-3417/13/2/998)).

---
<p class="news-date">January 3, 2023</p>

## Software Aging in Kubernetes for UAM Digital Twins

This *Drones* article studies software aging effects on Kubernetes in container orchestration systems for digital twin cloud infrastructures of Urban Air Mobility. It brings cloud-native dependability into the UAM digital-twin context, asking how long-running container orchestration behavior may affect service quality over time.

<figure>
  <img src="/images/news/230103/kubernetes-aging-uam-digital-twin-cover.webp" alt="Scientific illustration of software aging effects on Kubernetes-based UAM digital twin cloud infrastructure" width="1200" height="675" loading="lazy" decoding="async">
  <figcaption>Scientific illustration: cloud-native container clusters, aging traces, rejuvenation paths, and UAM digital twin infrastructure.</figcaption>
</figure>

### What the paper contributes

- Analyzes software aging in Kubernetes-based container orchestration.
- Places cloud infrastructure dependability inside the UAM digital-twin setting.
- Adds the January 2023 *Drones* publication as a dedicated News entry.

### Why this matters

- Digital twins depend on cloud services that must remain healthy over long operation periods.
- Software aging can degrade systems gradually, making proactive analysis important.
- The image connects container orchestration with UAM instead of treating Kubernetes as a generic backend.

**Publication record:** Published online on January 3, 2023 in *Drones*, Volume 7, Issue 1, Article 35 ([DOI](https://doi.org/10.3390/drones7010035), [MDPI article](https://www.mdpi.com/2504-446X/7/1/35)).

---
<p class="news-date">January 1, 2023</p>

## Kubernetes Cloud-Fog Dependability and Power Quantification

This *IEEE Access* article quantifies dependability and power consumption for Kubernetes-based cloud-fog continuum systems using a model-driven approach. The paper studies how containerized services behave across cloud, fog, and edge-like infrastructure while making both availability and energy visible in the analysis.

<figure>
  <img src="/images/news/230101/kubernetes-cloud-fog-dependability-cover.webp" alt="Scientific illustration of model-driven dependability and power consumption quantification in Kubernetes cloud-fog continuum systems" width="1200" height="675" loading="lazy" decoding="async">
  <figcaption>Scientific illustration: cloud-fog-edge service continuum, containerized workloads, dependability paths, and energy-aware system surfaces.</figcaption>
</figure>

### What the paper contributes

- Quantifies dependability and power consumption for Kubernetes-based cloud-fog continuum infrastructure.
- Uses model-driven analysis to evaluate service behavior across distributed compute layers.
- Completes the 2023 dedicated News batch with a cloud-infrastructure systems article.

### Why this matters

- Cloud-fog systems must balance availability with energy consumption.
- Kubernetes makes deployment flexible, but it also creates new modeling challenges across distributed layers.
- The cover turns this infrastructure trade-off into a clear scientific visual.

**Publication record:** Published in 2023 in *IEEE Access*, Volume 11, pages 140826-140852 ([DOI](https://doi.org/10.1109/ACCESS.2023.3340195), [IEEE Xplore record](https://ieeexplore.ieee.org/document/10373755)).

---

## Publication Visual Briefing Archive

The long-form News entries above highlight selected research releases, conference activities, project milestones, media, demonstrations, and publication updates. The visual briefing archive below completes the publication coverage with publication story blocks for records from the Publications page that do not yet have a dedicated long-form News entry: each entry includes a large scientific illustration, contribution notes, impact notes, and the publication record.

{% include publication_news_missing.html %}
