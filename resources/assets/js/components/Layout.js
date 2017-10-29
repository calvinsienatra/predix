import React, { Component } from 'react';
import ReactDOM from 'react-dom';
import Login from './components/Login';


export default class Layout extends Component {
    render() {
        return (
            <div className="container">
                <div className="row">
                    <div className="col-lg-12">
                        {this.props.children}
                    </div>
                </div>
            </div>
        );
    }
}

if (document.getElementById('layout')) {
    ReactDOM.render(<Layout />, document.getElementById('layout'));
}
