// import AsyncAutocomplete from './AsyncAutocomplete';
import './components.css'
import React, { useState } from 'react';
// import { useHistory } from "react-router-dom"

function FormGroup() {
  const [startVal, setStartVal] = useState("");
  const [endVal, setEndVal] = useState("");
  const [pathStr, setpathstr] = useState("");
  // let history = useHistory();

  function handleClick(inputText, outputText) {
    const requestOptions = {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ inputtext: startVal,
                              outputtext: endVal})
    };
    fetch('http://127.0.0.1:5000/api/alg', requestOptions)
      .then(response => {
        if (!response.ok) {
          throw new Error('Network response was not ok');
        }
        const response_value = response.json();
        response_value
          .then((value) => {
            console.log(value);
            setpathstr(value);
          })
        console.log(response_value);
      });

      // history.push("/results");
      return (
        <div>
          {pathStr}
        </div>
      )
    }

  return  (
    <div>
      <div class="form-group">
        {/* <AsyncAutocomplete title="Start Page" setValue={setStartVal}/>
        <AsyncAutocomplete title="End Page" setValue={setEndVal}/> */}
            <div class="start-field">
                <input type="text" name = "start" onChange={(e) => setStartVal(e.target.value)}/>
            </div>
            <div class="end-field">
              <input type="text" name = "end" onChange={(e) => setEndVal(e.target.value)}/>
            </div>
        </div>
        <div class = "submit-button">
          <input class="btn" type="submit" value="submit" onClick={() => handleClick(startVal, endVal)}/>
        </div>
    </div>
  );

}

export default FormGroup;