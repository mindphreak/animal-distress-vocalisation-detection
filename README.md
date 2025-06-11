# 🐾 Identification of Distressed Animal Vocalisations using Deep Transfer Clustering

**Author**: Midhun Satheesan  
**Affiliation**: MSc Data Analytics, National College of Ireland (2020)  
**Supervisor**: Dr. Catherine Mulwa

---

## 🎯 Project Overview

This project presents a novel deep learning approach to identify **distressed animal vocalisations** using a **hybrid supervised-unsupervised pipeline**. By leveraging **transfer learning** on audio spectrograms and applying **k-means clustering**, the system effectively separates distress vocalisations from other animal sounds — without the need for large-scale labeled data.

> 🧠 This work contributes to the emerging field of **bioacoustics** with potential applications in **animal welfare**, **passive acoustic monitoring**, and **AI for social good**.

---

## 📌 Highlights

- ✔️ Used **VGG-16** and **MobileNetV2** pre-trained on ImageNet for feature extraction
- ✔️ Fine-tuned models using distress-related audio (screams, sirens, sobbing) from the **FSD50K** dataset
- ✔️ Converted audio clips into **log-mel spectrograms** for model input
- ✔️ Applied **k-means clustering** (cosine and Euclidean) to group unlabeled animal vocalisations
- ✔️ Achieved improved clustering performance using **targeted transfer learning**, with silhouette scores ≈ **0.8+**
- ✔️ Identified vocal patterns similar to **distress calls** across species

---



