import React from 'react';
import { connect } from 'react-redux';
import { startLogin } from '../actions/auth';

const Burner = ({ startLogin }) => (
  <div className="box-layout">
    <div className="box-layout__box">
      <h1 className="box-layout__title">YEEF</h1>
      <p>It's time to get your expenses under control.</p>
    </div>
  </div>
);

export default Burner;
