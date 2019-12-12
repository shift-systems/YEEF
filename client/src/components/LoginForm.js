import React from 'react';
import { Link } from 'react-router-dom';

const LoginForm = props => (
  <div className="form-box">
    <form className="form" onSubmit={props.handleSubmit}>
      {props.error && (
        <p className="form__error">{props.error.non_field_errors}</p>
      )}

      <input
        type="text"
        placeholder="email"
        className="text-input"
        name="email"
        value={props.state.email}
        onChange={props.handleChange}
      />

      <input
        type="text"
        placeholder="password"
        className="text-input"
        name="password"
        value={props.state.password}
        onChange={props.handleChange}
      />
      <button className="button">Continue</button>
    </form>

    <div className="form-box__option ">
      <Link to="/reset_password">
        <small>Forgot password?</small>
      </Link>

      <div className="or-text">
        <hr className="or-text__bar" />
        <span className="or-text__text">OR</span>
        <hr className="or-text__bar" />
      </div>

      <button className="button"> Create an account</button>
    </div>
  </div>
);

export default LoginForm;
