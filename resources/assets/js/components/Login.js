import React, { Component } from 'react';
import ReactDOM from 'react-dom';

export default class Login extends Component {
    constructor(props){
        super(props);
        this.state = {inputURL: ""};
    }
    handleSubmit(e) {
        var inputURL = this.state.inputURL;
        if(!inputURL){
            alert('You must fill in your LinkedIn Profile URL');
            return;
        }
        var token = $('meta[name="csrf-token"]').attr('content');
        console.log('URL: ' + inputURL);
        $.ajax({
            type:'POST',
            url:"/inputurl",
            dataType: 'JSON',
            data: {
                "_method": 'POST',
                "_token": token,
                "inputURL": inputURL,
                },
            success:function(data){
            console.log('Achieved!');
            console.log(data);
            },
            error:function(){

            },
        });

    }
    handleonChange(e){
        var inputURL = e.target.value;
        this.setState({inputURL: inputURL});
    }

    render() {
        return (
            <div className="container">
                <div className="row">
                    <div className="col-lg-8 overlay">
                        <img src="img/logo.png" className="logo" />
                    </div>
                    <div className="col-lg-4 login-wrapper">
                        <div className="wrapper-login">
                            <h2>Welcome to Predix,</h2>
                            <h4>figure out what you need to improve! ;)</h4>
                            <form className="form-login">
                                <div className="form-group">
                                    <input type="text" onChange={this.handleonChange.bind(this)} className="form-control" id="inputURL" name="inputURL" aria-describedby="emailHelp" placeholder="LinkedIn Profile URL" />
                                </div>
                                <select class="selectpicker">
                                  <option>Uber</option>
                                  <option>Lyft</option>
                                  <option>Airbnb</option>
                                  <option>Google</option>
                                </select>

                            <button type="button" className="btn btn-outline-primary submit-btn" onClick={this.handleSubmit.bind(this)}>Let's Go!</button>
                            </form>
                        </div>
                    </div>
                </div>
            </div>
        );
    }
}

if (document.getElementById('login')) {
    ReactDOM.render(<Login />, document.getElementById('login'));
}

