import React from 'react';
import PropTypes from 'prop-types';
import Right from './right';
import Left from './Left';

const Login = (props) => {
    const {
        onSubmit,
        onChange,
        email,
        password
    } = props;

    return (

        <div>

            {/* <div className="main"> */}
                <Left />
                <Right />
                {/* <div className="login">
                    <div className="logo">
                        <img source="/images" alt="Yeef Enterprise"/>
                    </div>
                    <div id="title">
                        <div id="error"></div>
                        <h3>Yeef Savings Application</h3>
                    </div>
                    <form id="SignInForm" onSubmit={onSubmit}>
                        <h1>Please Login</h1>
                        <div>
                            <label class="psds-text-input__label" for="Username">Email or Username</label>
                            <input className="" autocapitalize="none" autocorrect="off" data-val="true" data-val-required="The Email or Username field is required." id="Username" name="Username" type="text" value={email} onChange={onChange}></input>
                        </div>

                        <div>
                            <label class="psds-text-input__label" for="Password">Password</label>
                            <input type="password" id="userPass" placeholder="Enter Password" value={password} name="password" onChange={onChange} />
                            <input type="submit" id="accept-btn" value="Login" />
                        </div>

                    </form>
                    <div>
                        <a class="" href="/ForgotPassword">Forgot password?</a>
                    </div>
                    <p><a href="/register" className="grey-text darken-2-text">I don't have an account</a></p>
                </div>
                <div className="footer">
                    
                Copyright © 2019 Yeef. All rights reserved.
                
                </div> */}
            {/* </div> */}



        </div>
    );
}

Login.propTypes = {
    onSubmit: PropTypes.func,
    onChange: PropTypes.func,
};
export default Login;