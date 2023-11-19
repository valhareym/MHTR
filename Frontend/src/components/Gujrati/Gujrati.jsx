import React from 'react'
import "./Gujrati.css"
import {HiLocationMarker} from 'react-icons/hi'
import CountUp from 'react-countup'
import {motion} from 'framer-motion'
const Hero = () => {
  return (
    <section className="hero-wrap">
        <div className="paddings innerWidth flexCenter hero-container">

            {/* Left Side */}
            <div className="flexColStart her-left">
                <div className="hero-title">
                    <div className="circle" />
                    
                    <motion.h1
                    initial = {{y: "2rem", opacity: 0}}
                    animate={{y:0, opacity:1}}
                    transition={{
                        duration: 2,
                        type: "spring"
                    }}
                    
                    
                    >
                    <h1>Gujrati <br /> Recognition</h1>
                    </motion.h1>
                </div>



                <div className="flexColStart hero-des">
                    <span className="secondaryText">Your File Goes Here</span>
                   
                </div>

                <div className="flexCenter upload-file">
                    <input type="file"/>
                    <button className="button" id="submitBtn">Upload</button>
                </div>

                <p id="predictionResult"></p>


               
          



            </div>

            {/* Right Side */}
            <div className="flexCenter hero-right">
                <motion.div
                initial={{x: "7rem", opacity:0}}
                animate={{x: "0", opacity:1}}
                transition={{
                    duration: 2,
                    type: "spring"
                }}
                className="image-container">
                    <img src="gujrati.png" alt="" />
                    </motion.div>
                
            </div>
        </div>
    </section>
  )
}

document.getElementById('submitBtn').addEventListener('click', async function() {
    var imageInput = playstation.png;
    if(imageInput.files.length == 0) {
        alert('Please select an image file.');
        return;
    }

    var file = imageInput.files[0];
    var formData = new FormData();
    formData.append("file", file);

    try {
        const response = await fetch('http://localhost:8000/predict/', {
            method: 'POST',
            body: formData
        });

        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }

        const result = await response.json();
        document.getElementById('predictionResult').innerText = 'Predicted Label: ' + result.character;
    } catch (error) {
        console.error('Error:', error);
        alert('Error sending image to server.');
    }
});

export default Hero



