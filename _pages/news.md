---
layout: archive
title: "News"
permalink: /news/
author_profile: true
header:
  og_image: "collaborators/ecdf.png"
---

<span style="font-family: times, serif; font-size:10pt; font-style:italic; color:red"> May 12, 2024 </span>

# <span style="font-family: times, serif; font-size:18pt; font-style:bold; color:blue"> Advanced Air Mobility-Vehicle Digital Twin (AAM-VDT) </span>

Excited to share our achievements after a year of leading the AAM-VDT project at Konkuk Aerospace Design-Airworthiness Institute (KADA). We've made significant progress in developing an integrated simulation platform for the Konkuk Passenger Vehicle (KP-2) digital twin in the Advanced Air Mobility (AAM) sector. Our focus on cutting-edge technologies has paved the way for a revolutionary system in urban air mobility.

The Advanced Air Mobility-Vehicle Digital Twin (AAM-VDT) project integrates cloud computing, artificial intelligence, and simulation to manage heterogeneous vehicles in real-time. Our collaboration within the KADA Research Groups - Design and Analysis, Simulation and Control, and AI Applications - has been instrumental in achieving our goals.

Our key features include cloud server integration, AI-driven operations, digital twin technology, and a strong emphasis on operational safety and management. By utilizing digital twin dynamics, ensuring safety and reliability, and implementing multi-vehicle coordination, we are shaping the future of AAM operations.

## Medias

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

Excited about the possibilities that lie ahead as we continue to innovate and drive advancements in the realm of Advanced Air Mobility. #AAM #UAM #DigitalTwin #AI #CloudComputing

<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Gallery with Thumbnails</title>
    <style>
        body {
            font-family: Arial, sans-serif;
        }
        .gallery {
            display: flex;
            flex-wrap: wrap;
            gap: 10px;
            justify-content: center;
        }
        .thumbnail {
            width: 150px;
            height: 100px;
            overflow: hidden;
            cursor: pointer;
            border: 2px solid #ddd;
            transition: 0.3s;
        }
        .thumbnail img {
            width: 100%;
            height: auto;
        }
        .thumbnail:hover {
            border-color: #333;
        }
        /* The Modal (background) */
        .modal {
            display: none;
            position: fixed;
            z-index: 1;
            left: 0;
            top: 0;
            width: 100%;
            height: 100%;
            overflow: auto;
            background-color: rgba(0,0,0,0.9);
            justify-content: center;
            align-items: center;
        }
        /* Modal Content (image) */
        .modal-content {
            max-width: 90%;
            max-height: 90%;
            margin: auto;
            display: block;
        }
        /* Caption of Modal Image */
        .caption {
            margin: auto;
            display: block;
            width: 80%;
            max-width: 700px;
            text-align: center;
            color: #ccc;
            padding: 10px 0;
        }
        /* The Close Button */
        .close {
            position: absolute;
            top: 20px;
            right: 35px;
            color: #f1f1f1;
            font-size: 40px;
            font-weight: bold;
            transition: 0.3s;
        }
        .close:hover,
        .close:focus {
            color: #bbb;
            text-decoration: none;
            cursor: pointer;
        }
    </style>
</head>
<body>

<h1>Gallery with Thumbnails</h1>

<div class="gallery">
    <div class="thumbnail">
        <img src="../images/news/VDT Simulation System.jpg" alt="VDT Simulation System" onclick="openModal(this)">
    </div>
    <div class="thumbnail">
        <img src="../images/news/VDT Techs..jpg" alt="VDT Techs" onclick="openModal(this)">
    </div>
    <div class="thumbnail">
        <img src="../images/news/VDT-CILS-Rezied.jpg" alt="VDT-CILS Resized" onclick="openModal(this)">
    </div>
    <div class="thumbnail">
        <img src="../images/news/VDT-CILS.jpg" alt="VDT-CILS" onclick="openModal(this)">
    </div>
    <div class="thumbnail">
        <img src="../images/news/VDT-Single-ODT.jpg" alt="VDT Single ODT" onclick="openModal(this)">
    </div>
    <div class="thumbnail">
        <img src="../images/news/VDT-SITL-Simplified.jpg" alt="VDT SITL Simplified" onclick="openModal(this)">
    </div>
    <div class="thumbnail">
        <img src="../images/news/VDT-SITL.jpg" alt="VDT SITL" onclick="openModal(this)">
    </div>
</div>

<!-- The Modal -->
<div id="myModal" class="modal" onclick="closeModal(event)">
    <span class="close" onclick="closeModal()">&times;</span>
    <img class="modal-content" id="img01">
    <div class="caption" id="caption"></div>
</div>

<script>
    function openModal(element) {
        var modal = document.getElementById('myModal');
        var modalImg = document.getElementById('img01');
        var captionText = document.getElementById('caption');

        modal.style.display = "flex";
        modalImg.src = element.src;
        captionText.innerHTML = element.alt;
    }

    function closeModal(event) {
        var modal = document.getElementById('myModal');
        if (event.target === modal || event.target.className === 'close') {
            modal.style.display = "none";
        }
    }
</script>

    <!-- Embedded YouTube Videos -->
    <iframe src="https://www.youtube.com/embed/ePH-f1H2PH8" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
    <iframe src="https://www.youtube.com/embed/9effNK__aOU" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
    <iframe src="https://www.youtube.com/embed/X20FuC0C7pM" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
    <iframe src="https://www.youtube.com/embed/huKKna1OFjA" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
    <iframe src="https://www.youtube.com/embed/luD0U2uVrgg" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
    <iframe src="https://www.youtube.com/embed/QfZZfo9YNls" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
    <iframe src="https://www.youtube.com/embed/qfMXk1IYKFA" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
    <iframe src="https://www.youtube.com/embed/u0xFRdc-97Q" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
    <iframe src="https://www.youtube.com/embed/FqyS67FReXo" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

</body>
</html>

------------------

<span style="font-family: times, serif; font-size:1pt; font-style:italic; color:red"> May 10, 2024 </span>

# <span style="font-family: times, serif; font-size:18pt; font-style:bold; color:blue"> IEEE/IFIP Network Operations and Management Symposium </span>
