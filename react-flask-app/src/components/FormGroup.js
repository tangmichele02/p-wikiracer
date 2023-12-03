import AsyncAutocomplete from './AsyncAutocomplete';
import './components.css'
import React, { useState } from 'react';
import axios from 'axios';

function FormGroup() {
  const [startVal, setStartVal] = useState("");
  const [endVal, setEndVal] = useState("");
  const [pathstr, setpathstr] = useState("");


  function handleClick(startVal, endVal) {
    axios.get("http://127.0.0.1:5000/api/alg?startValue=" + startVal + "&endValue=" + endVal)
      .then(response => {
        setpathstr(response.data.path)
      })
      .catch(error => {
        console.error('Error fetching data:', error);
      });
    }
    

  return  (

    <div class="form-container">
      <div class="form-group">
        <div class="header-field-group">
          <div class="start-header">
              <div class="rectangle">Start</div>
          </div>
          <div class="start-field">
            <AsyncAutocomplete title="" setValue={setStartVal}/>
          </div>
        </div>
      </div>
      
      <div class="form-group">
        <div class="header-field-group">
          <div class="start-header">
              <div class="rectangle">End</div>
          </div>
          <div class="start-field">
            <AsyncAutocomplete title="" setValue={setStartVal}/>
          </div>
        </div>
      </div>

      <div class="submit-button">
        <input class="btn" type="submit" value="submit" onClick={() => handleClick(startVal, endVal)}/>
      </div>

      <div class="result-path">
        {pathstr}
      </div>
    </div>

  );


    // <div>
    //   <div class="headers">
    //     <div class="start-header">
    //       <AsyncAutocomplete title="Start Page" setValue={setStartVal}/>
    //     </div>
    //     <div class="input-separator"></div>
    //     <div class="end-header">
    //       <AsyncAutocomplete title="End Page" setValue={setEndVal}/>
    //     </div>
        
    //   </div>

    //   <div class="submit-button">
    //       <input class="btn" type="submit" value="submit" onClick={() => handleClick(startVal, endVal)}/>
    //   </div>

    //   <div class="result-path">
    //     {pathstr}
    //   </div>
    // </div>
  // );


}

export default FormGroup;