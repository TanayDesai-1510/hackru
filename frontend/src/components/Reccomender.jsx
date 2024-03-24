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
  Box,
} from "@mui/material";
import { useNavigate, useParams } from "react-router-dom";
import { useMyContext } from "../Context";


const Reccomender = () => {
  const [profData, setProfData] = useState([]);
  const navigate = useNavigate();
  const {netId} = useParams();

  const {signIn} = useMyContext();
  if (!signIn) {
    navigate('/');
  }
  useEffect(() => {
    // if (!professorData) {
      (async () => {
        try {
          const response = await fetch(`http://127.0.0.1:5000/class-netid/${netId}`);
          if (!response.ok) {
            return;
          }
          const data = await response.json();
          const dataArray = Object.values(data); // Convert object to array
          setProfData(dataArray);
        console.log(dataArray)
        } catch (error) {
          console.error("Error fetching data:", error);
        }
    })();
    // } else {
    // //   setProfData(professorData);
    // }
  }, [netId]);

  return (
    <Box sx={{ marginTop: '4rem', display: 'flex', flexDirection: 'column', gap: '1rem', width: '100%' }}>{profData.map((pd, index) => (
        <Grid item key={index} sx={{width: '100%', flexGrow: '1'}}>
          <ButtonBase component="div" sx={{width: '100%'}}>
            <Card sx={{width: '100%'}}>
              <CardContent>
                <Typography variant="h5" component="h2">
                  {pd.class}
                </Typography>
                <Typography color="textSecondary">
                  ID: {pd.id}
                </Typography>
                <Typography color="textSecondary">
                  Description: {pd.description}
                </Typography>
                <Typography color="textSecondary">
                  School: {pd.school}
                </Typography>
              </CardContent>
            </Card>
          </ButtonBase>
        </Grid>
      ))}
      </Box>
  );
};

export default Reccomender;
