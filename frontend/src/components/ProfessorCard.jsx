import React, { useEffect, useState } from "react";
import {
  Typography,
  Button,
  Dialog,
  DialogTitle,
  DialogContent,
  DialogActions,
  Grid,
  ButtonBase,
  Card,
  CardContent,
} from "@mui/material";

const ProfessorCard = ({ classInfo, onClose, professorData }) => {
  const [profData, setProfData] = useState([]);

  useEffect(() => {
    if (!professorData) {
      (async () => {
        try {
          const response = await fetch("http://127.0.0.1:5000/proftrial");
          if (!response.ok) {
            return;
          }
          const data = await response.json();
          const dataArray = Object.values(data); // Convert object to array
          setProfData(dataArray);
        } catch (error) {
          console.error("Error fetching data:", error);
        }
      })();
    } else {
      setProfData(professorData);
    }
  }, [professorData]);

  return (
    <Dialog open onClose={onClose}>
      <DialogTitle>{classInfo.class}</DialogTitle>
      <DialogContent>
        <Grid container direction="column" spacing={3}>
          {profData.map((pd, index) => (
            <Grid item key={index}>
              <ButtonBase component="div">
                <Card>
                  <CardContent>
                    <Typography variant="h5" component="h2">
                      {pd.class}
                    </Typography>
                    <Typography color="textSecondary">
                      Department: {pd.dept}
                    </Typography>
                    <Typography color="textSecondary">
                      Professor: {pd.professor}
                    </Typography>
                    <Typography color="textSecondary">
                      School: {pd.school}
                    </Typography>
                    <Typography color="textSecondary">
                      Rating: {pd.rating}
                    </Typography>
                  </CardContent>
                </Card>
              </ButtonBase>
            </Grid>
          ))}
        </Grid>
      </DialogContent>
      <DialogActions>
        <Button onClick={onClose}>Close</Button>
      </DialogActions>
    </Dialog>
  );
};

export default ProfessorCard;
