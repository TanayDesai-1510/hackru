import React, { useState, useEffect } from 'react';
import { Card, CardContent, Typography } from '@mui/material';

const Display = () => {
  const [classesData, setClassesData] = useState([]);

  useEffect(() => {
    fetch('http://127.0.0.1:5000/classtrial')
      .then(response => {
        if (!response.ok) {
          throw new Error(`HTTP error ${response.status}`);
        }
        return response.json();
      })
      .then(data => {
        setClassesData(Object.values(data));
      })
      .catch(error => {
        console.error('Error fetching data:', error);
      });
  }, []);

  return (
    <div>
      <h1>Class Trial</h1>
      <div style={{ display: 'flex', flexWrap: 'wrap' }}>
        {classesData.map(classInfo => (
          <Card key={classInfo.id} style={{ maxWidth: 345, margin: '20px', transition: 'transform 0.3s' }}>
            <CardContent>
              <Typography variant="h5" component="h2">
                {classInfo.class}
              </Typography>
              <Typography color="textSecondary">
                ID: {classInfo.id}
              </Typography>
              <Typography color="textSecondary">
                Department: {classInfo.dept}
              </Typography>
              <Typography color="textSecondary">
                School: {classInfo.school}
              </Typography>
              <Typography color="textSecondary">
                Credits: {classInfo.credits}
              </Typography>
            </CardContent>
          </Card>
        ))}
      </div>
    </div>
  );
};

export default Display;
