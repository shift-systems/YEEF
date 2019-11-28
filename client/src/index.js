import React from 'react';
import ReactDom from 'react-dom';
import App from './app';
import './styles/main.scss';
import 'react-dates/initialize';
import 'react-dates/lib/css/_datepicker.css';
ReactDom.render(<App />, document.getElementById('app'));
