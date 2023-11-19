import React from 'react'
import "./Hero.css"
import {HiLocationMarker} from 'react-icons/hi'
import CountUp from 'react-countup'
import {motion} from 'framer-motion'
const Hero = () => {
  return (
    <section className="hero-wrapper">
        <div className="paddings innerWidth flexCenter hero-container">

            {/* Left Side */}
            <div className="flexColStart hero-left">
                <div className="hero-title">
                    <div className="orange-circle" />
                    <motion.h1
                    initial = {{y: "2rem", opacity: 0}}
                    animate={{y:0, opacity:1}}
                    transition={{
                        duration: 2,
                        type: "spring"
                    }}
                    
                    
                    >
                    <h1>Scribble <br />  Sense</h1>
                    </motion.h1>
                </div>



                <div className="flexColStart hero-des">
                    <span className="secondaryText">An Effective Measure of Recognition</span>
                    <span className="secondaryText"> of Handwritten Multilingual Texts</span>
                </div>

                {/* <div className="flexCenter upload-file">
                    <input type="file"/>
                    <button className="button">Upload</button>
                </div> */}

                <div className="flexCenter stats">

                    <div className="flexColCenter stat">
                        <span>
                            <CountUp start = {0} end = {20} duration = {4}/>
                            <span>+</span>
                        </span>
                        <span className = "secondaryText">Users</span>
                    </div>

                    <div className="flexColCenter stat">
                        <span>
                            <CountUp start = {0} end = {15} duration = {4}/>
                            <span>+</span>
                        </span>
                        <span className = "secondaryText">Total Files</span>
                    </div>

                    <div className="flexColCenter stat">
                        <span>
                            <CountUp start = {0} end = {15} duration = {4}/>
                            <span>+</span>
                        </span>
                        <span className = "secondaryText">90%+ Accuracy</span>
                    </div>



                </div>

          



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
                    <img src="text_to_text.png" alt="" />
                    </motion.div>
                
            </div>
        </div>
    </section>
  )
}

export default Hero



//ScribbleSense
//An Effective Measure of Recognition of Handwritten Multilingual Texts
//Users
//Total Files
//90%+ Accuracy
