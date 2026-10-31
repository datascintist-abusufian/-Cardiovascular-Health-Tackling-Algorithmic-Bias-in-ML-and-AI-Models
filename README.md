# Cardiovascular Health: Tackling Algorithmic Bias in ML and AI Models

Experiments on fairness and explainability in cardiovascular AI. The repository covers a tabular risk model and image-based cardiac detection models. It audits them for subgroup bias, applies bias mitigation and explains predictions with LIME, SHAP and Grad-CAM.

## Data

| Data | Source | In repo |
| --- | --- | --- |
| Cardiovascular disease risk table (70,000 records) | [Kaggle Cardiovascular Disease dataset](https://www.kaggle.com/datasets/sulianova/cardiovascular-disease-dataset) | `cardio_train.csv` |
| Chest radiographs with heart bounding boxes | [RSNA Pneumonia Detection Challenge](https://www.kaggle.com/competitions/rsna-pneumonia-detection-challenge) and [RSNA cardiac detection labels](https://www.kaggle.com/datasets/vivekprajapati2048/rsnacardiacdetectionlabels) | No (download separately) |
| Cardiac MRI slices with YOLO labels (left ventricle, myocardium, right ventricle) | [Roboflow heart-segmentation-2](https://universe.roboflow.com/memoire/heart-segmentation-2/dataset/1), CC BY 4.0 | `heart_dataset_sup.zip` |
| Calcium-scoring CT (DICOM) | [Cardiac Atlas Project](https://www.cardiacatlas.org/) | No |

## What the notebooks do

| Notebook | Purpose |
| --- | --- |
| `Smoker (1).ipynb`, `adversialedited.ipynb` | Fairness metrics with [AIF360](https://aif360.readthedocs.io/); in-processing bias mitigation by adversarial debiasing |
| `LIMEANDHYPERPARAMETER1.ipynb`, `Updated_LIME_.ipynb` | Random forest risk model with class rebalancing, hyperparameter tuning and LIME/SHAP explanations |
| `Heatmap_Analysis.ipynb`, `scir (1).ipynb`, `sir (2).ipynb` | Exploratory analysis of the risk table |
| `project-bias-edited (2).ipynb` | Heart detection on chest radiographs with PyTorch Lightning |
| `ResNet (1).ipynb`, `gradCAM.ipynb` | ResNet image models and Grad-CAM saliency |
| `Yoooooooloooooooo (1).ipynb` | YOLO annotation and detection workflow |
| `GroundTruth.ipynb`, `LIMEIIMAGES.ipynb`, `Patient ID.ipynb` | DICOM reading, unsupervised heart segmentation, LIME on images |
| `sensitivity_analysis.ipynb`, `iou-analysis.py` | Sensitivity and IoU analysis of detection results |
| `performance-analysis.tex` | Performance tables for the write-up |

## Running it

The notebooks were written in Google Colab and read files from `/content/`. Install the main libraries with:

```bash
pip install pandas numpy scikit-learn imbalanced-learn lime shap aif360 torch torchvision pytorch-lightning pydicom opencv-python
```

## Licence

No licence has been declared yet. Each dataset keeps its own licence and terms of use.

## Author

Md Abu Sufian - ORCID [0009-0007-3503-6942](https://orcid.org/0009-0007-3503-6942)
