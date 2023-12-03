import './components.css'
import redcar from './rightcar.png'
import bluecar from './bluecar.png'
import greencar from './greencar.png'

function Car() {
  return  (
    <div>
        <div class="red rcar">
            <img src={redcar} />
        </div>
        <div class="blue bcar">
            <img src={bluecar} />
        </div>
        <div class="green gcar">
            <img src={greencar} />
        </div>
    </div>
  );

}

export default Car;