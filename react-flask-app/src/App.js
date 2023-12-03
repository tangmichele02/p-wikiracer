import { useState, useEffect } from 'react';
import FormGroup from './components/FormGroup';
import Headers from './components/Headers';
import Car from './components/Car';

document.body.style = 'background: #C3DBF5;';

function App() {
  const [message, setMessage] = useState('');
  const [error, setError] = useState('');

  useEffect(() => {
    fetch('/api')
      .then(response => {
        if (!response.ok) {
          throw new Error('Network response was not ok');
        }
        return response.json();
      })
      .then(data => setMessage(data.message))
      .catch(error => setError(error.message));
  }, []);

  return (
    <div>
      <div>
        <h1>Welcome to p-wikiracer!</h1>
        {/* <Headers/> */}
        <FormGroup/>
        <Car/>
      </div>
    </div>
    
  );
}

export default App;