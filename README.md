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


---

## 🛠️ Tech Stack

- Python 3.8
- TensorFlow / Keras
- Librosa (audio processing)
- OpenCV (image resizing)
- Scikit-learn (clustering)
- FSD50K Dataset

---

## 📈 Results

| Feature Extractor     | Clustering Type   | Distance Metric | Silhouette Score |
|-----------------------|------------------|-----------------|------------------|
| VGG-16 (Target-trained)   | K-Means            | Euclidean        | **0.83**           |
| VGG-16 (Standard)     | K-Means            | Euclidean        | 0.74              |
| MobileNetV2 (Target-trained) | K-Means        | Cosine           | 0.65              |
| MobileNetV2 (Standard) | K-Means           | Cosine           | 0.51              |

---

## 📚 Future Work

- Explore **autoencoders** and **contrastive learning** for better feature embeddings
- Replace K-means with **Gaussian Mixture Models (GMMs)**
- Build a **real-time passive acoustic monitoring system**
- Extend to other domains lacking labeled data

---

## 🐈‍⬛ Acknowledgements

Dedicated to my late pet cat **Mathai**, and his sibling **Rappai**, who inspired this project.  
Grateful to Dr. Catherine Mulwa (Supervisor), Eduardo Fonseca (FSD50K), and the Sound of AI community.

---

## 📜 License

This project is for academic and non-commercial use. Please cite appropriately if referencing.

---

## 📎 Links

- 🔗 [FSD50K Dataset](https://zenodo.org/record/4060432)



