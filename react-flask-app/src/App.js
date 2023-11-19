import { useState, useEffect } from 'react';
import FormGroup from './components/FormGroup';
import Headers from './components/Headers';

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
      <h1>Welcome to p-wikiracer!</h1>
      <Headers/>
      <FormGroup/>
    </div>
  );
}

export default App;