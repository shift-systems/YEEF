import React from 'react';

const Left = props => {
    return (
        <div id="left">
            <div className="spacer">

            </div>
            <div className="signin">
                <div className="wrapper">
                    <div className="logo">
                        <img src="/images/logo.png" alt="Yeef Fundation" />
                    </div>
                    <form action="/id/" class="signInForm" id="passwordSignInForm" method="post">
                        <input name="__RequestVerificationToken" type="hidden" value="" />
                        <input id="RedirectUrl" name="RedirectUrl" type="hidden" value="/id/dashboard" />
                        <div>
                            <label class="text-input__label" for="Username">Email or Username</label>
                            <input class="text-input__field text-input__field--appearance-subtle" autocapitalize="none" autocorrect="off" data-val="true" data-val-required="The Email or Username field is required." id="Username" name="Username" type="text" value="" />
                        </div>
                        <div>
                            <label class="text-input__label" for="Password">Password</label>
                            <input class="text-input__field text-input__field--appearance-subtle" data-val="true" data-val-maxlength="Password must not exceed 128 characters" data-val-maxlength-max="128" data-val-required="The Password field is required." id="Password" name="Password" type="password" />
                        </div>
                        <input id="ShowCaptcha" name="ShowCaptcha" type="hidden" value="False" />
                        <input id="ReCaptchaSiteKey" name="ReCaptchaSiteKey" type="hidden" value="6LeVIgoTAAAAAIhx_TOwDWIXecbvzcWyjQDbXsaV" />                    <button type="submit" id="login" class="button button--size-medium">
                            Sign in
                            </button>
                    </form>




                    <div className="links">
                        <a className="link link--appearance-default" href="/id/ForgotPassword">Forgot password?</a>
                        <a className="link link--appearance-default" href="/id/signin/sso?redirectTo=%2fid%2fdashboard">Sign in with company or school</a>
                    </div>
                    <div className="or">
                        <hr className="bar" />
                        <span>OR</span>
                        <hr className="bar" />
                    </div>
                    <a href="" id="create-account-link" className="button button--appearance-stroke">
                        <span className="button__text">Create an account</span>
                    </a>
                </div>
                <footer id="footer">
                    Copyright © 2019 Yeef. All rights reserved.
                <div>
                        <a className="link link--appearance-subtle" href="">Terms of Use</a>
                        | <a className="link link--appearance-subtle" href="">Privacy Policy</a>
                    </div>
                </footer>
            </div>
        </div>
    );
};

export default Left;
