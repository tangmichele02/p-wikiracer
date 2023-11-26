import './components.css'
import React, { useState } from 'react';
import TextField from '@mui/material/TextField';
import Autocomplete from '@mui/material/Autocomplete';
import AsyncAutocomplete from './AsyncAutocomplete.js'



function handleClick(inputText, outputText) {
  const requestOptions = {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ inputtext: inputText,
                            outputtext: outputText})
  };
  fetch('http://127.0.0.1:5000/api/alg', requestOptions)
    .then(response => {
      if (!response.ok) {
        throw new Error('Network response was not ok');
      }
      const response_value = response.json();
      console.log(response_value);
    });
  // return (
  //   <div>
  //     <p>Hi</p>
  //   </div>
  // )
}

// function displayPath(response) {
//   return (
//     <div>
//       <p>{response}</p>
//     </div>
//   );
// }

// const [inputText, setInputText] = useState("");
  // const [outputText, setOutputText] = useState("");
  //return  (
    {/*<div>
    <div class="form-group">
          <div class="start-field">
              <input type="text" name = "start" onChange={(e) => setInputText(e.target.value)}/>
          </div>
          <div class="end-field">
            <input type="text" name = "end" onChange={(e) => setOutputText(e.target.value)}/>
          </div>
      </div>
      <div class = "submit-button">
        <input class="btn" type="submit" value="submit" onClick={() => handleClick(inputText, outputText)}/>
      </div>
      

    </div>*/}
  //);

function FormGroup() {

  var searchNames1 = ['Sydney', 'Melbourne', 'Brisbane', 
  'Adelaide', 'Perth', 'Hobart'];

  var searchNames2 = ['Apple', 'Pear', 'Banana', 
    'Arbalest', 'Crossbow', 'Trebuchet'];

  return  (
    
    <div class="form-group">

      <AsyncAutocomplete title="Start Page"/>
      <AsyncAutocomplete title="End Page"/>
      {/* <Autocomplete
        disablePortal
        id="combo-box-demo1"
        options={searchNames1}
        sx={{ width: 300 }}
        renderInput={(params) => <TextField {...params} label="Start" />}
      /> */}

    {/* <Autocomplete
      disablePortal
      id="combo-box-dem2"
      options={searchNames2}
      sx={{ width: 300 }}
      renderInput={(params) => <TextField {...params} label="End" />}
    /> */}
    
        {/* <div class="start-field">
            <input type="text" name = "start"/>
        </div>
        <div class="end-field">
            <input type="text" name = "end"/>
  */}</div>
  )
  
}

export default FormGroup;