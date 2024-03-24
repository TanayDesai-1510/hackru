import React, { useState, useEffect } from "react";
import {
  Card,
  CardContent,
  Typography,
  ButtonBase,
  Grid,
} from "@mui/material";
import { makeStyles } from "@mui/styles";
import ProfessorCard from "./ProfessorCard";

const useStyles = makeStyles({
  card: {
    width: 275,
    margin: "20px",
    transition: "transform 0.3s",
    "&:hover": {
      transform: "scale(1.05)",
    },
  },
  cardContent: {
    height: 200, // Adjust the height as needed
    overflow: "auto", // Add overflow to allow scrolling if content exceeds height
  },
});

const Display = () => {
  const classes = useStyles();
  const [classesData, setClassesData] = useState([]);
  const [selectedClass, setSelectedClass] = useState(null);
  const [professorData, setProfessorData] = useState(null);

  useEffect(() => {
    fetch("http://127.0.0.1:5000/classtrial")
      .then((response) => {
        if (!response.ok) {
          throw new Error(`HTTP error ${response.status}`);
        }
        return response.json();
      })
      .then((data) => {
        setClassesData(Object.values(data));
      })
      .catch((error) => {
        console.error("Error fetching data:", error);
      });
  }, []);

  const handleCardClick = (classInfo) => {
    setSelectedClass(classInfo);
  };

  const handleClose = () => {
    setSelectedClass(null);
  };

  return (
    <div>
      <h1>Class Trial</h1>
      <Grid container spacing={3}>
        {classesData.map((classInfo) => (
          <Grid item xs={12} sm={6} md={4} lg={3} key={classInfo.id}>
            <ButtonBase
              component="div"
              className={classes.card}
              onClick={() => handleCardClick(classInfo)}
            >
              <Card>
                <CardContent className={classes.cardContent}>
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
            </ButtonBase>
          </Grid>
        ))}
      </Grid>
      {selectedClass && (
        <ProfessorCard
          classInfo={selectedClass}
          onClose={handleClose}
          professorData={professorData}
        />
      )}
    </div>
  );
};

export default Display;
