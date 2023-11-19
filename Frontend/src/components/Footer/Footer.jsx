import { color } from 'framer-motion';
import React from 'react';

const Footer = () => {
  return (
    <footer style={styles.footer}>
      <div style={styles.container}>
        <div style={styles.newsletter}>
          <h3>Suggest us Languages</h3><br />
          <form>
            <input
              type="email"
              placeholder="Language..."
              style={styles.input}
            />
            <button type="submit" style={styles.button}>
              Submit
            </button>
          </form>
        </div>
        <div style={styles.address}>
          <h3>Contact Us</h3><br />
          <p>Email: valhareym@gmail.com</p>
          
        </div>

        <div style={styles.address}>
          <h3>Developers</h3><br />
          <p>Aditya S Varanasi</p>
          <p>Shreyas S</p>
          <p>Deep Chakraborty</p>
          <p >Harshvardhan Singh</p>
          
        </div>
      </div>
      <div style={styles.copyRight}>
        <p>&copy; 2023 ScribbleSense. All rights reserved.</p>
      </div>
    </footer>
  );
};

const styles = {
  footer: {
    backgroundColor: '#000', // Set the background color to black
    color: '#fff',
    padding: '20px 0',
    textAlign: 'center',
  },
  container: {
    display: 'flex',
    justifyContent: 'space-around',
    alignItems: 'flex-start',
    flexWrap: 'wrap',
  },
  newsletter: {
    maxWidth: '400px',
    marginBottom: '20px',
  },
  input: {
    width: '100%',
    padding: '10px',
    marginBottom: '10px',
    borderRadius: '5px',
    border: 'none',
  },
  button: {
    width: '100%',
    padding: '10px',
    backgroundColor: '#3498db',
    color: '#fff',
    border: 'none',
    borderRadius: '5px',
    cursor: 'pointer',
  },
  address: {
    maxWidth: '400px',
    marginBottom: '20px',
  },
  copyRight: {
    marginTop: '20px',
  },
};

export default Footer;
