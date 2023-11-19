import React from 'react'
import './Header.css'
const Header = () => {
  return (
    <section className="h-wrapper">
        <div className="flexCenter paddings innerWidth h-container">

            <img src="images.jpeg" alt="logo" width = {90} height={70} id="circular-image"/>


            <div className="flexCenter h-menu">
         
                <a href="#Languages">Languages Trained</a>
                <a href="">Contact Us</a>
                <a href="">Get Started</a>
                <button className="button">
                <a href="">Sign In</a>
                </button>
            </div>

        </div>
    </section>
  )
}

export default Header