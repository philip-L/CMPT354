import React, { Component } from 'react';
import logo from './logo.svg';
import './App.css';

class App extends Component {
  render() {
    return (
      <div className="App">
        <header className="App-header">
          <img src='http://www.clker.com/cliparts/d/6/b/9/11949852831476265676tramezzino.svg.thumb.png' className="App-logo" alt="logo" />
          <h1 className="App-title">SubAvenue Inc</h1>
        </header>
        <div className="shopping-list">
        <div class="tab">
          <button class="tablinks">Sandwiches</button>
          <button class="tablinks">Beverages</button>
          <button class="tablinks">Snacks</button>
        </div>
    </div>
        <p className="App-intro">
        </p>
      </div>
    );
  }
}

export default App;

// function openCity(cityName) {
//     // Declare all variables
//     var i, tabcontent, tablinks;
//
//     // Get all elements with class="tabcontent" and hide them
//     tabcontent = document.getElementsByClassName("tabcontent");
//     for (i = 0; i < tabcontent.length; i++) {
//         tabcontent[i].style.display = "none";
//     }
//
//     // Get all elements with class="tablinks" and remove the class "active"
//     tablinks = document.getElementsByClassName("tablinks");
//     for (i = 0; i < tablinks.length; i++) {
//         tablinks[i].className = tablinks[i].className.replace(" active", "");
//     }
//
//     // Show the current tab, and add an "active" class to the button that opened the tab
//     document.getElementById(cityName).style.display = "block";
//     evt.currentTarget.className += " active";
// }
