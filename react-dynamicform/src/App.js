import React, { Component } from 'react';
import ReactDOM from 'react-dom';
import DynamicForm from './components/DynamicForm';
import axios from 'axios';
import './App.css';
const JsonTable = require('ts-react-json-table');

class App extends Component {
  state = {
    data: [
      {id: 'V3G4', name: "John Jones", sandwich:"Veggie", drink:"Coke", snack:"Lays",creditcard:35232,address:"123 Street", delivery: true},
      {id: '56G4', name: "Lucky One", sandwich:"Chicken", drink:"Sprite", snack:"Cookie",creditcard:22433,address:"456 Ave", delivery: false},
      {id: 'R3U4', name: "Craig Scratchley", sandwich:"Beef", drink:"Nestea", snack:"Pringles",creditcard:34324,address:"420 Place", delivery: true},
    ],
    current: {},
  }

   projectionQuery(){
    var val = document.getElementById("proj").value;
    return axios.post('http://127.0.0.1:8000/ordering/', {
    attr: this.val, query: 'projection'}).then(function (response) {
        console.log(response);
        ReactDOM.render( <JsonTable className="table" rows = {response.data} / > ,
          document.getElementById('container')
        );
      })
  }

   selectionQuery(){
     var val = Number(document.getElementById("sel").value);

    return axios.post('http://127.0.0.1:8000/ordering/', {
    attr: this.val, query: 'selection'}).then(function (response) {
        console.log(response);
        ReactDOM.render( <JsonTable className="table" rows = {response['data']}/> ,
          document.getElementById('container')
        );
      })
  }

   joinQuery(){
     var val = document.getElementById("join").value;

    return axios.post('http://127.0.0.1:8000/ordering/', {
    attr: this.val, query: 'join'}).then(function (response) {
        console.log(response);
        ReactDOM.render( <JsonTable className="table" rows = {response['data']}/> ,
          document.getElementById('container')
        );
      })
  }

   aggregationQuery(){
    return axios.post('http://127.0.0.1:8000/ordering/', {
    query: 'aggregation'}).then(function (response) {
        console.log(response['data']);
        ReactDOM.render( <JsonTable className="table" rows = {response['data']}/> ,
          document.getElementById('container')
        );
      })
  }


   groupbyQuery(){
    return axios.post('http://127.0.0.1:8000/ordering/', {
    query: 'nested_aggregation'}).then(function (response) {
        console.log(response['data']);
        ReactDOM.render( <JsonTable className="table" rows = {response['data']}/> ,
          document.getElementById('container')
        );
      })
  }


   updateOp(){
     var val = (Number(document.getElementById("update").value));
    return axios.post('http://127.0.0.1:8000/ordering/', {
    attr: this.val, query:'update'}).then(function (response) {
        console.log(response);
        ReactDOM.render( <JsonTable className="table" rows = {response['data']}/> ,
          document.getElementById('container')
        );
      })
  }


   deleteOp(){
     var val = document.getElementById("delete").value;
    return axios.post('http://127.0.0.1:8000/ordering/', {
    attr: this.val, query: 'delete'}).then(function (response) {
        console.log(response);
        ReactDOM.render( <JsonTable className="table" rows = {response['data']}/> ,
          document.getElementById('container')
        );
      })
  }

   divisionQuery(restaurantID){
    return axios.post('http://127.0.0.1:8000/ordering/', {
    query: 'division'}).then(function (response) {
        console.log(response['data']);
        ReactDOM.render( <JsonTable className="table" rows = {response['data']}/> ,
          document.getElementById('container')
        );
      })
  }

  render() {

    return (
      <div className="App">
      <header className="App-header">
        <img src='http://www.clker.com/cliparts/d/6/b/9/11949852831476265676tramezzino.svg.thumb.png' className="App-logo" alt="logo" />
        <h1 className="App-title">SubAvenue Inc</h1>
      </header>

        <div align="left">
          <div>
            Projection query: Find
             <select id = 'proj'>
                <option value="menuItemID">menuItemID</option>
                <option value="Description">Description</option>
                <option value="Price">Price</option>
              </select>
                   from table menuItems
                   <button onClick={this.projectionQuery}>Submit</button>

          </div>
          <br/>
          <div>
            Selection query: Find menuitems from table menuItems where price > <input id = 'sel' type="number" name="fname"></input> <button onClick={this.selectionQuery}>Submit</button>
          </div>
            <br/>
          <div>
            Join query: Find employee IDS who work at
            <select id="join">
               <option value="123 Toasted Street, Vancouver BC">123 Toasted Street, Vancouver BC</option>
               <option value="67A Whole Wheat Place, Vancouver BC">67A Whole Wheat Place, Vancouver BC</option>
               <option value="500 Mayo Drive, Burnaby BC">500 Mayo Drive, Burnaby BC</option>
               <option value="32G Lettuce Street, Vancouver BC">32G Lettuce Street, Vancouver BC</option>
               <option value="13 Ketchup Court, Delta BC">13 Ketchup Court, Delta BC</option>
             </select>
             <button onClick={this.joinQuery}>Submit</button>
          </div>
            <br/>
          <div>
            Aggregation query: Find most expensive sandwich on menu   <button onClick={this.aggregationQuery}>Submit</button>
          </div>
            <br/>
          <div>
            Nested Aggregation query: Find the average order total for a customer who has placed more than 2 orders <button onClick={this.groupbyQuery}>Submit</button>
          </div>
            <br/>
          <div>
            Update query: Increase price of menu items by $<input id='update' type="number" name="fname"></input>  <button onClick={this.updateOp}>Submit</button>
          </div>
            <br/>
          <div>
            Delete query: Delete sandwiches of the size
            <select id="delete">
               <option value="H">Half</option>
               <option value="F">Full</option>
           </select>
            <button onClick={this.deleteOp}>Submit</button>
          </div>
            <br/>
          <div>
            Division query: Find the customers who have ordered from all restaurant locations <button onClick={this.divisionQuery}>Submit</button>
          </div>
        </div>

        <div id="container">

        </div>

      </div>
    );
  }
}

export default App;
