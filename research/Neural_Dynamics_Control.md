---
layout: archive
title: "Neural Dynamics and Control"
permalink: /research/Neural_Dynamics_Control
author_profile: true
---

# <span style="color:blue"> es-DNLC: A Deep Neural Network Control with Exponentially Stabilizing Control Lyapunov Functions for Attitude Stabilization of PAV </span>

### Abstract

Attitude stabilization is of paramount importance in the flight control of personal aerial vehicle (PAV) in the future urban air mobility (UAM). This study proposes to adopt a deep neural network (DNN) with exponentially stabilizing control Lyapunov functions (es-CLF) as a control framework (called, es-DNLC) for the stabilization of a KP-1 eVTOL PAV in multi-copter mode. The es-DNLC uses exponentially stabilizing control Lyapunov Function(es-CLF) as a learning policy in the DNN training to guarantee the robustness against disturbances. The robustness is enhanced and verified by an area increase of region of attraction (ROA) after adopting the trained DNN into the KP-1 control system. We implemented the proposed control framework in an open source autopilot system (PX4) along with software in the loop (SITL) in Gazebo simulator in which a wind gust is injected as a sudden disturbance in the simulation. A wind tunnel test was performed to increase the accuracy of the Gazebo simulation by utilizing high-fidelity propulsion data of the KP-1's motors. The effectiveness of the adopted control framework is compared with linear quadratic regulator (LQR) which is also the initial control of es-DNLC before training. The finding of this study shows that es-DNLC compared to LQR can guarantee a higher level of robustness of the system against disturbances and aerodynamic uncertainties.