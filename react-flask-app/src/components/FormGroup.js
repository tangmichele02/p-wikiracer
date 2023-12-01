import './components.css'
import React, { useState } from 'react';

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
  const [inputText, setInputText] = useState("");
  const [outputText, setOutputText] = useState("");
  const [pathstr, setpathstr] = useState("");


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
        response_value
          .then((value) => {
            console.log(value);
            setpathstr(value);
          })
        console.log(response_value);
      });
    

  return  (
    <div>
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
        <div>
          {pathstr}
        </div>
      </div>
    </div>
  );

}

export default FormGroup;