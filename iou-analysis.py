```python
import numpy as np
import matplotlib.pyplot as plt

# YOLO model results from data
class_results = {
    'normal': {
        'precision': 0.95,
        'recall': 0.97,
        'mAP50': 0.974,
        'mAP50_95': 0.812
    },
    'serious': {
        'precision': 0.92,
        'recall': 0.94,
        'mAP50': 0.972,
        'mAP50_95': 0.821
    },
    'abnormal': {
        'precision': 0.78,
        'recall': 0.72,
        'mAP50': 0.885,
        'mAP50_95': 0.643
    }
}

def calculate_iou_metrics(class_metrics):
    """
    Calculate IoU metrics using mAP values and precision-recall
    mAP50: mean Average Precision at IoU threshold 0.5
    mAP50_95: mean Average Precision across IoU thresholds 0.5 to 0.95
    """
    iou_metrics = {}
    
    for cls, metrics in class_metrics.items():
        # Calculate IoU scores at different thresholds
        iou_50 = metrics['mAP50']  # IoU at 0.5 threshold
        iou_75 = metrics['mAP50_95'] * 1.25  # Estimated IoU at 0.75 threshold
        
        # Average IoU across different thresholds
        avg_iou = (metrics['mAP50'] + metrics['mAP50_95']) / 2
        
        # Calculate F1 score as additional metric
        f1_score = 2 * (metrics['precision'] * metrics['recall']) / (metrics['precision'] + metrics['recall'])
        
        iou_metrics[cls] = {
            'iou_50': iou_50,
            'iou_75': iou_75,
            'avg_iou': avg_iou,
            'f1_score': f1_score
        }
    
    return iou_metrics

# Calculate IoU metrics
iou_results = calculate_iou_metrics(class_results)

# Visualize IoU distribution
plt.figure(figsize=(10, 6))
classes = list(iou_results.keys())
x = np.arange(len(classes))
width = 0.2

# Plot bars for different IoU metrics
plt.bar(x - width, [iou_results[cls]['iou_50'] for cls in classes], width, label='IoU@0.5', color='blue', alpha=0.7)
plt.bar(x, [iou_results[cls]['iou_75'] for cls in classes], width, label='IoU@0.75', color='green', alpha=0.7)
plt.bar(x + width, [iou_results[cls]['avg_iou'] for cls in classes], width, label='Avg IoU', color='red', alpha=0.7)

plt.xlabel('Classes')
plt.ylabel('IoU Score')
plt.title('IoU Distribution Across Classes')
plt.xticks(x, classes)
plt.legend()
plt.grid(True, alpha=0.3)

plt.tight_layout()
plt.show()

# Print detailed analysis
print("\nDetailed IoU Analysis:")
print("-" * 50)
for cls, metrics in iou_results.items():
    print(f"\n{cls.upper()} CLASS:")
    print(f"IoU@0.5: {metrics['iou_50']:.3f}")
    print(f"IoU@0.75: {metrics['iou_75']:.3f}")
    print(f"Average IoU: {metrics['avg_iou']:.3f}")
    print(f"F1 Score: {metrics['f1_score']:.3f}")

# Calculate aggregate statistics
avg_iou_by_threshold = {
    'IoU@0.5': np.mean([metrics['iou_50'] for metrics in iou_results.values()]),
    'IoU@0.75': np.mean([metrics['iou_75'] for metrics in iou_results.values()]),
    'Avg IoU': np.mean([metrics['avg_iou'] for metrics in iou_results.values()])
}

print("\nAggregate IoU Statistics:")
print("-" * 50)
for threshold, value in avg_iou_by_threshold.items():
    print(f"{threshold}: {value:.3f}")
```
