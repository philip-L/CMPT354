import React, { Component } from 'react';
import DynamicForm from './components/DynamicForm';
import './App.css';

class App extends Component {
  state = {
    data: [
      {id: 'V3G4', name: "John Jones", sandwich:"Veggie", drink:"Coke", snack:"Lays",creditcard:35232,address:"123 Street", delivery: true},
      {id: '56G4', name: "Lucky One", sandwich:"Chicken", drink:"Sprite", snack:"Cookie",creditcard:22433,address:"456 Ave", delivery: false},
      {id: 'R3U4', name: "Craig Scratchley", sandwich:"Beef", drink:"Nestea", snack:"Pringles",creditcard:34324,address:"420 Place", delivery: true},
    ],
    current: {}
  }

  onSubmit = (model) => {
    let data = [];

    let newMod = JSON.parse(JSON.stringify(model))

    if (newMod.id) {
      data = this.state.data.filter((d) => {
        return d.id != newMod.id
      });
    } else {
      newMod.id = Math.random().toString(36).substr(2, 4);
      data = this.state.data.slice();
    }
    this.setState({
      data: [newMod, ...data],
    });

    model.name = ''
    model.id = ''
    model.creditcard = ''
    model.address = ''
    model.sandwich = ''
    model.snack = ''
    model.drink = ''


  }

  onEdit = (id) => {
    let record = this.state.data.find((d) => {
      return d.id == id;
    });
    alert(JSON.stringify(record));
    this.setState({
      current: record
    })
  }

  render() {
    let data = this.state.data.map((d) => {
      return (
        <table>
          <tr>
            <th>Order ID</th>
            <th>Name</th>
            <th>Sandwich</th>
            <th>Drink</th>
            <th>Snack</th>
            <th>Credit Card</th>
            <th>Address</th>
            <th>Delivery</th>
            <th>Edit your order</th>
            <th>Delete your order</th>
          </tr>
          <tr key={d.id}>
              <td>{d.id}</td>
              <td>{d.name}</td>
              <td>{d.sandwich}</td>
              <td>{d.drink}</td>
              <td>{d.snack}</td>
              <td>{d.creditcard}</td>
              <td>{d.address}</td>
              <td>{d.delivery.toString()}</td>
              <td><button onClick={()=>{this.onEdit(d.id)}}>edit</button></td>
              <td><button>Delete</button></td>
          </tr>
        </table>
      );
    });

    return (
      <div className="App">
      <header className="App-header">
        <img src='http://www.clker.com/cliparts/d/6/b/9/11949852831476265676tramezzino.svg.thumb.png' className="App-logo" alt="logo" />
        <h1 className="App-title">SubAvenue Inc</h1>
        <button>Switch to admin mode</button>
      </header>
        <DynamicForm className="form"
          title = "Place your order!"
          defaultValues = "hello!"
          model={[
            // {key: "id", label: "ID", props: {required: true}},
            {key: "name",label: "Name", type: "string"},
            {key: "sandwich",label: "Sandwich", type: "string"},
            {key: "drink",label: "Drink", type: "string", props:{min:0,max:5}},
            {key: "snack",label: "Snack", type:"string"},
            {key: "creditcard",label: "CreditCard", type:"number"},
            {key: "address",label: "Address", type:"string"},
            {key: "delivery",label: "Delivery?", type:"radio",options:[
              {key:"true",label:"Yes",name:"delivery",value:"true"},
              {key:"false",label:"No, pick up",name: "delivery",value:"false"}
          ]}
        ]}
          onSubmit = {(model) => {this.onSubmit(model)}}
        />

        <table border="1">
          <tbody>{data}</tbody>
        </table>

      </div>
    );
  }
}

export default App;
