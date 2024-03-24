import React, { useState } from 'react';
import { FormControl, InputLabel, Select, MenuItem, TextField, Button, Paper } from '@mui/material';
import { styled } from '@mui/material/styles';

const majorOptions = [
  "Africana Studies - 013",
  "Africana Studies - 014",
  "American Studies - 050",
  "Anthropology - 070",
  "Art History - 082",
  "Asian Studies - 098",
  "Astrophysics - 105",
  "Agriculture and Environmental Science - 015",
  "Catalan - 145",
  "Chinese - 165",
  "Classical Humanities - 190",
  "Classics in Ancient Greek - 490",
  "Classic in Latin - 580",
  "Criminal Justice - 202",
  "Dance - 203",
  "Dance - 206",
  "East Asia Language and Area Studies - 214",
  "Education - 300",
  "English - 350",
  "English - 353",
  "English - 354",
  "English - 355",
  "European Studies - 360",
  "Excerise Science and Sport Studies - 377",
  "French - 420",
  "Geography - 450",
  "Geological Sciences - 460",
  "German - 470",
  "Modern Greek Studies - 489",
  "Marine Sciences - 628",
  "Meteorology - 670",
  "Microbiology - 680",
  "Hindi - 505",
  "Cognitive Science - 185",
  "Computer Science - 198",
  "Economics - 220",
  "History - 506",
  "History - 508",
  "History - 510",
  "History - 512",
  "Hungarian - 535",
  "Italian - 560",
  "Japanese - 565",
  "Mathematics - 640",
  "Medical Technology - 660",
  "Labor Studies - 575",
  "Latin American Studies - 590",
  "Statistics - 960",
  "Sociology - 960",
  "Religion - 840",
  "Philosophy - 790",
  "Political Science - 790",
  "Women's and Gender Studies - 988",
  "Cinema Studies - 175",
  "Finance - 390",
  "Marketing - 630",
  "Accounting - 010",
  "Management - 620",
  "Management Science and Information Systems - 623",
  "Information Technology and Informatics - 189",
  "Journalism and Media Studies - 567",
  "Communication - 192",
  "Planning and Public Policy - 762",
  "Public Health - 832"
];

const yearOptions = ["Freshman", "Sophomore", "Junior", "Senior"];

const Container = styled('div')({
  display: 'flex',
  flexDirection: 'column',
  alignItems: 'center',
  justifyContent: 'flex-start',
  height: '80vh',
  textAlign: 'center',
  marginTop: '20vh'
});

const CardContainer = styled(Paper)({
  padding: '20px',
  width: '80%', // Increased width
  maxWidth: '400px', // Maximum width
  border: '2px solid #ccc', // Increased border
  borderRadius: '8px', // Rounded corners
  display: 'flex',
  flexDirection: 'column',
  alignItems: 'center',
});

function Form() {
  const [major, setMajor] = useState('');
  const [year, setYear] = useState('');
  const [gpa, setGpa] = useState('');

  const handleSubmit = (event) => {
    event.preventDefault();
    console.log({ major, year, gpa });
    // Submit your form data here
  };

  return (
    <Container>
      <CardContainer elevation={3}>
        <FormControl fullWidth margin="normal">
          <InputLabel id="major-label">Major</InputLabel>
          <Select
            labelId="major-label"
            id="major"
            value={major}
            label="Major"
            onChange={e => setMajor(e.target.value)}
          >
            {majorOptions.map((option) => (
              <MenuItem key={option} value={option}>{option}</MenuItem>
            ))}
          </Select>
        </FormControl>
        
        <FormControl fullWidth margin="normal">
          <InputLabel id="year-label">Year</InputLabel>
          <Select
            labelId="year-label"
            id="year"
            value={year}
            label="Year"
            onChange={e => setYear(e.target.value)}
          >
            {yearOptions.map((option) => (
              <MenuItem key={option} value={option}>{option}</MenuItem>
            ))}
          </Select>
        </FormControl>

        <TextField
          fullWidth
          margin="normal"
          id="gpa"
          label="GPA"
          value={gpa}
          onChange={e => setGpa(e.target.value)}
        />

        <Button type="submit" variant="contained" style={{ marginTop: '10px', backgroundColor: '#cc0033' }} margin="normal" onClick={handleSubmit}>
          Submit
        </Button>
      </CardContainer>
    </Container>
  );
}

export default Form;
