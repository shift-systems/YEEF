import actionTypes from './actionTypes';

export const loginSuccess = response => ({
  type: actionTypes.LOGIN_SUCCESS,
  payload: response.user
});

export const loginFail = response => ({
  type: actionTypes.LOGIN_FAIL,
  payload: response.user
});

export const logout = () => ({
  type: 'LOGOUT'
});

export const signupSuccess = response => ({
  type: actionTypes.SIGNUP_SUCCESS,
  payload: response.user
});

export const signupFail = response => {
  return {
    type: actionTypes.SIGNUP_FAIL,
    payload: response.user
  };
};

export const startSignup = data => {
  return dispatch => {
    fetch(`http://127.0.0.1:8000/api/v1.0/register`, {
      method: 'POST',
      headers: {
        'content-type': 'application/json'
      },
      CORS: 'no-cors',
      body: JSON.stringify({ user: data })
    })
      .then(res => res.json())
      .then(response => {
        if (response.user.id) {
          dispatch(signupSuccess(response));
        } else {
          dispatch(signupFail(response));
        }
      })
      .catch(err => {
        console.log(err, 'This error is from auth action');
      });
  };
};

export const startLogin = data => {
  return dispatch => {
    fetch(`http://127.0.0.1:8000/api/v1.0/login`, {
      method: 'POST',
      headers: {
        'content-type': 'application/json'
      },
      CORS: 'no-cors',
      body: JSON.stringify({ user: data })
    })
      .then(res => res.json())
      .then(response => {
        console.log(response.status, 'check status code');
        if (response.user.token) {
          dispatch(loginSuccess(response));
        } else {
          dispatch(loginFail(response));
        }
      })
      .catch(error => {
        console.log(error, 'From auth action');
      });
  };
};

export const startLogout = () => {
  return () => {
    return firebase.auth().signOut();
  };
};
