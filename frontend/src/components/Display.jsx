import React, { useState, useEffect } from "react";
import { Typography, List, ListItem, ListItemText } from "@mui/material";
import { makeStyles } from "@mui/styles";
import { useNavigate } from "react-router-dom";
import { useMyContext } from "../Context";

const useStyles = makeStyles({
  listItem: {
    width: "100%",
    padding: "10px",
    borderBottom: "1px solid #ccc",
    transition: "background-color 0.3s",
    "&:hover": {
      backgroundColor: "#f0f0f0", // Change to desired hover color
    },
  },
});

const Display = ({ netId }) => { // Accept netId as prop
  const classes = useStyles();
  const [classesData, setClassesData] = useState({});

  const navigate = useNavigate();

  const {signIn} = useMyContext();
  if (!signIn) {
    navigate('/');
  }

  useEffect(() => {
    fetch(`http://127.0.0.1:5000/dashboard/${netId}`) // Use netId in the URL
      .then((response) => {
        if (!response.ok) {
          throw new Error(`HTTP error ${response.status}`);
        }
        return response.json();
      })
      .then((data) => {
        setClassesData(data);
        console.log(classesData);
      })
      .catch((error) => {
        console.error("Error fetching data:", error);
      });
  }, [netId]); // Include netId in dependency array

  return (
    <div>
      <Typography variant="h3">
        {classesData.Name} - {classesData.NetID}
      </Typography>
      <br />
      <Typography variant="h4"> Major - {classesData.Major} </Typography>{" "}
      <br />
      <Typography variant="h4">Courses Taken</Typography>
      <br />
      <List>
        {Object.entries(classesData.Courses || {}).map(
          ([courseId, [courseName, courseGrade]]) => (
            <ListItem key={courseId} className={classes.listItem}>
              <ListItemText
                primary={courseName}
                secondary={
                  <>
                    <Typography variant="body2" color="textSecondary">
                      ID: {courseId}
                    </Typography>
                    <Typography variant="body2" color="textSecondary">
                      Grade: {courseGrade}
                    </Typography>
                  </>
                }
              />
            </ListItem>
          )
        )}
      </List>
    </div>
  );
};

export default Display;
