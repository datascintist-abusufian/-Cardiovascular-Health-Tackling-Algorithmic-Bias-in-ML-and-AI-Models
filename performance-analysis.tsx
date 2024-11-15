import React from 'react';
import { Card, CardHeader, CardTitle, CardContent } from '@/components/ui/card';
import { BarChart, Bar, XAxis, YAxis, CartesianGrid, Tooltip, Legend, ResponsiveContainer } from 'recharts';

const PerformanceAnalysis = () => {
  // Data extracted from validation results
  const metricsData = [
    { class: 'Normal', precision: 0.962, recall: 1.000, mAP50: 0.974, mAP50_95: 0.812 },
    { class: 'Abnormal', precision: 0.758, recall: 0.797, mAP50: 0.885, mAP50_95: 0.643 },
    { class: 'Serious', precision: 0.963, recall: 1.000, mAP50: 0.972, mAP50_95: 0.821 }
  ];

  // Confusion matrix data (estimated from precision and recall)
  const confusionData = [
    { category: 'True Positives', normal: 116, abnormal: 94, serious: 116 },
    { category: 'False Positives', normal: 5, abnormal: 30, serious: 4 },
    { category: 'False Negatives', normal: 0, abnormal: 24, serious: 0 }
  ];

  return (
    <div className="space-y-8">
      <Card>
        <CardHeader>
          <CardTitle>Class-wise Performance Metrics</CardTitle>
        </CardHeader>
        <CardContent>
          <div className="h-80">
            <ResponsiveContainer width="100%" height="100%">
              <BarChart data={metricsData}>
                <CartesianGrid strokeDasharray="3 3" />
                <XAxis dataKey="class" />
                <YAxis />
                <Tooltip />
                <Legend />
                <Bar dataKey="precision" fill="#8884d8" name="Precision" />
                <Bar dataKey="recall" fill="#82ca9d" name="Recall" />
                <Bar dataKey="mAP50" fill="#ffc658" name="mAP50" />
                <Bar dataKey="mAP50_95" fill="#ff7300" name="mAP50-95" />
              </BarChart>
            </ResponsiveContainer>
          </div>
        </CardContent>
      </Card>

      <Card>
        <CardHeader>
          <CardTitle>Confusion Matrix Analysis</CardTitle>
        </CardHeader>
        <CardContent>
          <div className="h-80">
            <ResponsiveContainer width="100%" height="100%">
              <BarChart data={confusionData}>
                <CartesianGrid strokeDasharray="3 3" />
                <XAxis dataKey="category" />
                <YAxis />
                <Tooltip />
                <Legend />
                <Bar dataKey="normal" fill="#8884d8" name="Normal" />
                <Bar dataKey="abnormal" fill="#82ca9d" name="Abnormal" />
                <Bar dataKey="serious" fill="#ffc658" name="Serious" />
              </BarChart>
            </ResponsiveContainer>
          </div>
        </CardContent>
      </Card>
    </div>
  );
};

export default PerformanceAnalysis;
