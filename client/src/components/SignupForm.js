import React from 'react';
import { Link } from 'react-router-dom';

const SignupForm = props => (
  <div className="form-box">
    <form className="form" onSubmit={props.handleSubmit}>
      {props.errors &&
        props.errors.map(error => <p className="form__error">{error}</p>)}
      <input
        type="text"
        placeholder="username"
        autoFocus
        className="text-input"
        value={props.state.username}
        onChange={props.onUsernameChange}
      />
      <input
        type="text"
        placeholder="mobile number"
        className="text-input"
        value={props.state.mobile_number}
        onChange={props.onMobileNumberChange}
      />

      <input
        type="text"
        placeholder="email"
        className="text-input"
        name="email"
        value={props.state.email}
        onChange={props.onEmailChange}
      />

      <input
        type="text"
        placeholder="confirm email"
        className="text-input"
        name="confirmEmail"
        value={props.state.confirmEmail}
        onChange={props.onEmailChange}
      />

      <input
        type="text"
        placeholder="password"
        className="text-input"
        value={props.state.password}
        onChange={props.onPasswordChange}
      />

      <div>
        <button className="button">Continue</button>
      </div>
    </form>

    <div className="form-box__option ">
      <Link to="/reset_password">
        <small>Already have an account?</small>
      </Link>

      <div className="or-text">
        <hr className="or-text__bar" />
        <span className="or-text__text">OR</span>
        <hr className="or-text__bar" />
      </div>

      <button className="button">Login</button>
    </div>
  </div>
);

export default SignupForm;
