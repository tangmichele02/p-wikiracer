import './components.css'
import React, { useState } from 'react';
import TextField from '@mui/material/TextField';
import Autocomplete from '@mui/material/Autocomplete';
import AsyncAutocomplete from './AsyncAutocomplete.js'



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
        </div> */}
    </div>
  );
}

export default FormGroup;