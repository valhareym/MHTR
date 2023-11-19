import React from 'react'
import { Link } from 'react-router-dom';
import {Swiper, SwiperSlide, useSwiper} from 'swiper/react'
import "swiper/css"
import "./Hospitals.css"
import data from'../../utils/slider.json'
import { sliderSettings } from '../../utils/common'
const Hospitals = () => {
  return (
   
    <section className="r-wrapper">
        <div className="paddings innerWidth r-container">
            <div className="r-head flexColStart">
                <span className="orangeText">CNN (Convolutional Neural Network) Algorithm is used  </span>
                <span className="primaryText">Languages:</span>
            </div>

            <Swiper {...sliderSettings}>
               <SliderButtons></SliderButtons> 
                {
                    data.map((card, i) => (
                        <SwiperSlide key={i}>
                             
                            <div className="flexCentre r-card">
                                <img src= {card.image} alt="Home" />

                                <span className="secondaryText r-price">
                                    <span style={{color : "blue"}}> </span>
                                </span>
                                <span class="primaryText">{card.name}</span> <br />
                            </div>
                         
                        </SwiperSlide>
                        


                    ))
                }
            </Swiper>
        </div>
    </section>
    
  )
}


export default Hospitals

const SliderButtons = () => {
    const swiper = useSwiper();
    return (
        <div className="flexCenter r-buttons">
            <button onClick = {()=> swiper.slidePrev()}>&lt;</button>
            <button onClick = {()=> swiper.slideNext()}>&gt;</button>
            
        </div>
    )
}
