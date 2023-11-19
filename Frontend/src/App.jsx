import Header from "./components/Header/Header";
import Hero from "./components/Hero";
import './App.css'
import Hospitals from "./components/Hospitals/Hospitals";
import Value from "./components/Footer/Footer"
import Contact from "./components/Contact/Contact"
import NewsletterForm from "./components/Footer/Footer";
import English from "./components/English/English"
import Arabic from "./components/Arabic/Arabic"
import Devnagri from "./components/Devnagri/Devnagri";
import Gujrati from "./components/Gujrati/Gujrati";
import Footer from "./components/Footer/Footer";
function App() {
  return (
    <div className = "App">

      <div>
        <div className="white-gradient"/>
        <Header/>
        <Hero/>

      </div>
      <Hospitals/>
      <English/>
      <Arabic/>
      <Devnagri/>
      <Gujrati/>
     <Footer/>
      
     
     
    </div>
  );
}
export default App;
