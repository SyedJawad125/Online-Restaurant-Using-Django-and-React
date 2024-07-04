import React from 'react'
import img4 from '../images/4.jpg'
import img5 from '../images/5.jpg'
import img6 from '../images/6.jpg'
import '../App.css'

const About = () => {
  return (
    <div class='container' style={{ marginLeft: '200px' }}  >
                
        <div class="about-section">
            <h1>About Us Page</h1>
            <p>Some text about who we are and what we do.</p>
            <p>Resize the browser window to see that this page is responsive by the way.</p>
        </div>

        <h2 style={{textAlign: "center" }}>Our Team</h2>
        <div class="row">
          <div class="column">
            <div class="card" >
              <img src={img4} alt="Jane" style={ {width: '70%'} } />
              <div class="container">
                <h2>Jane Doe</h2>
                <p class="title">CEO & Founder</p>
                <p>Some text that describes me lorem ipsum ipsum lorem.</p>
                <p>jane@example.com</p>
                <p><button class="button">Contact</button></p>
              </div>
            </div>
          </div>

          <div class="column">
            <div class="card">
              <img src={img5} alt="Mike" style={ {width: '70%'} } />
              <div class="container">
                <h2>Mike Ross</h2>
                <p class="title">Art Director</p>
                <p>Some text that describes me lorem ipsum ipsum lorem.</p>
                <p>mike@example.com</p>
                <p><button class="button">Contact</button></p>
              </div>
            </div>
          </div>

          <div class="column">
            <div class="card">
              <img src={img6} alt="John" style={ {width: '70%'} } />
              <div class="container">
                <h2>John Doe</h2>
                <p class="title">Designer</p>
                <p>Some text that describes me lorem ipsum ipsum lorem.</p>
                <p>john@example.com</p>
                <p><button class="button">Contact</button></p>
              </div>
            </div>
          </div>
       </div>
    </div>
  )
}

export default About